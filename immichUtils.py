import io
import discord
import uuid
from datetime import datetime
from dotenv import load_dotenv

from immich_client.api.assets import upload_asset
from immich_client.models import AssetMediaCreateDto
from immich_client.types import File
from immich_client.api.memories import search_memories

# This might be re-added later depending on if it is needed
# however I do not think it is needed since it can be passed in by
# references and just instances of interactions, attachnents... ect
# load_dotenv()
# try:
#     # Load in enviorment variables for use
#     IMMICH_KEY = os.environ["IMMICH_KEY"]
#     LOCAL_IP = os.environ["LOCAL_IP"]
#     TAILSCALE_IP = os.environ["TAILSCALE_IP"]
# except KeyError as e:
#     print(f"Missing enviorment variable {e}")

async def list_memories(self, date):

    date_obj = datetime.strptime(date, "%Y-%m-%d")


    try:
        if self.client is None:
            return "Not connected to the client", False

        memories = search_memories.sync(
            client=self,
            for_=date
        )

        if not memories:
            return f"No memories returned for {date_obj}"

        memory_list = []
        for memory in memories:
            memory_list.append(memory)

        return memory_list, True

    except Exception as e:
        return e, False
        
    
async def upload_image(self, photo: discord.Attachment):
    """
        upload_image
            self: The bot client in this reference it has access to the immich
                api and is logged in to a instance.

            photo: discord attachment that is used to upload to immich

            Checks to see if the client is actually connected or not and if it is
            then it creates some content that can be uploaded to immich. Via the
            Dto given by immich-client (generated API)

            DTO:
                asset_data (File):
                device_asset_id (str):
                device_id (str):
               file_created_at (datetime.datetime):
                file_modified_at (datetime.datetime):
                duration (str | Unset):
                filename(str | Unset):

                OPTIONALS:
                is_favorite (bool | Unset):
                live_photo_video_id (UUID | Unset):
                metadata(list | Unset):
                visibility(AssetVisibility | Unset):

            Might implement is_favorite later for fun features.
    """
    try:
        # Default check to see if we are actually connected or not
        if self.client is None:
            return "Not connected to the client", False

        # Read in the photo and convert it to bytes and it's stream
        file_bytes = await photo.read()
        file_stream = io.BytesIO(file_bytes)

        # Attach a device asset ID for identification
        device_asset_id = f"discord-{photo.id}-{uuid.uuid4()}"

        # Create the immich file with its content type
        immich_file = File(
            payload=file_stream,
            file_name=photo.filename,
            mime_type=photo.content_type or "image/jpeg"        
        )

        # Create the dto body for upload
        body = AssetMediaCreateDto(
            asset_data=immich_file,
            device_asset_id=device_asset_id,
            device_id="discord-bot",
            file_created_at=datetime.now(),
            file_modified_at=datetime.now()
        )

        # If the client is not connected
        response = upload_asset.sync(
            client=self.client,
            body=body
        )

        # Check if it sync'd properlly and uploaded
        if response:
            return f"Successfuly uploaded photo: {photo.filename} "
        else:
            return "Upload failed, no response from Immich."

    except Exception as e:
        return e

def check_immich_connection(self):
    if not self.client:
        return "Error: Not connected to Immich."
    else:
        return f"Connected to {self.client._base_url}"
