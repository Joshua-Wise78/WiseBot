import io
import os
import discord
import uuid
import httpx
from datetime import datetime
from dotenv import load_dotenv

from immich_client.models import AssetMediaCreateDto, MetadataSearchDto
from immich_client.types import File

from immich_client.api.assets import upload_asset
from immich_client.api.search import search_assets
from immich_client.api.assets import view_asset

load_dotenv()
IMMICH_KEY = os.getenv("IMMICH_KEY")

class SimpleAsset:
    def __init__(self, data):
        if hasattr(data, "id"):
            self.id = data.id
            self.original_file_name = getattr(data, "original_file_name", None)
            created_at = getattr(data, "file_created_at", None)
            exif = getattr(data, "exif_info", None)
            
        else:
            self.id = data.get('id')
            self.original_file_name = data.get('originalFileName')
            created_at = data.get('fileCreatedAt')
            exif = data.get('exifInfo')

        # Name fallback
        if not self.original_file_name:
            self.original_file_name = f"{self.id}.jpg"

        # Date Parsing
        if isinstance(created_at, datetime):
            self.file_created_at = created_at
        elif isinstance(created_at, str):
            try:
                self.file_created_at = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
            except ValueError:
                self.file_created_at = datetime.now()
        else:
            self.file_created_at = datetime.now()

        self.location = "Unknown Location"
        
        if exif:
            print(f"DEBUG EXIF for {self.id}: {exif}")

            def get_val(obj, attr):
                if isinstance(obj, dict): 
                    return obj.get(attr)
                return getattr(obj, attr, None)

            city = get_val(exif, 'city')
            state = get_val(exif, 'state')
            country = get_val(exif, 'country')
            lat = get_val(exif, 'latitude')
            long_ = get_val(exif, 'longitude')

            loc_parts = [p for p in [city, state, country] if p]
            
            if loc_parts:
                self.location = ", ".join(loc_parts)
            elif lat is not None and long_ is not None:
                self.location = f"{lat:.4f}, {long_:.4f}"

async def random_image(self):
    return "Not implemented"

async def get_asset_thumbnail(self, asset_id):
    if self.client is None:
        return None, "Client not connected"

    try:
        real_uuid = asset_id
        if isinstance(asset_id, str):
            real_uuid = uuid.UUID(asset_id)

        response_file = await view_asset.asyncio(
            client=self.client,
            id=real_uuid
        )

        if response_file and response_file.payload:
            return response_file.payload.read(), None
        else:
            return None, "Error downloading thumbnail"

    except Exception as e:
        return None, f"Error downloading thumbnail: {e}"
            

async def convert_search_response_dto(search_result):
    if not search_result:
        return None, "No search result to convert."

    try:
        # The API returns a SearchResponseDto -> assets -> items
        assets_wrapper = getattr(search_result, 'assets', None)
        
        if assets_wrapper and hasattr(assets_wrapper, "items"):
            return [SimpleAsset(item) for item in assets_wrapper.items], None
            
        return None, "Could not locate asset list in response structure."

    except Exception as e:
        return None, f"Unexpected error converting assets: {e}"


async def list_memories(self, date):
    print(f"Searching memories for date: {date}")
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return None, "Invalid format for date. YYYY-MM-DD"

    try:
        if self.client is None:
            return None,  "Not connected to the client."

        local_tz = datetime.now().astimezone().tzinfo
        start_local = date_obj.replace(hour=0, minute=0, second=0, tzinfo=local_tz)
        end_local = date_obj.replace(hour=23, minute=59, second=59, tzinfo=local_tz)

        body = MetadataSearchDto(
            taken_after=start_local,
            taken_before=end_local,
        )

        response = await search_assets.asyncio(
            client=self.client, 
            body=body
        )
        
        return response, None

    except TypeError as e:
        return None, f"Model Schema Error: {e}"
    except Exception as e:
        return None, f"Error searching memories: {e}"

    
async def upload_image(self, photo: discord.Attachment):
    try:
        if self.client is None:
            return "Not connected to the client", False

        file_bytes = await photo.read()
        file_stream = io.BytesIO(file_bytes)

        device_asset_id = f"discord-{photo.id}-{uuid.uuid4()}"

        immich_file = File(
            payload=file_stream,
            file_name=photo.filename,
            mime_type=photo.content_type or "image/jpeg"        
        )

        body = AssetMediaCreateDto(
            asset_data=immich_file,
            device_asset_id=device_asset_id,
            device_id="discord-bot",
            file_created_at=datetime.now(),
            file_modified_at=datetime.now()
        )

        response = await upload_asset.asyncio(
            client=self.client,
            body=body
        )

        if response:
            return f"Successfuly uploaded photo: {photo.filename} "
        else:
            return "Upload failed, no response from Immich."

    except Exception as e:
        return f"Upload Error: {e}"
