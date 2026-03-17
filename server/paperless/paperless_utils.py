import discord
import httpx
import os
import io
import uuid
from datetime import datetime

from paperless_client.types import File
from paperless_client.models import (
    PostDocumentRequest
)

from paperless_client.api.documents import documents_post_document_create

async def upload_document(self, document: discord.Attachment):
    try:
        if self.client is None:
            return None, "Not connected to Paperless client."
        
        file_bytes = await document.read()
        file_stream = io.BytesIO(file_bytes)

        device_asset_id = f"discord-{document.id}-{uuid.uuid4()}"

        paperless_document = File(
            payload=file_stream,
            file_name=document.filename,
            mime_type=document.content_type or "application/octet-stream"
        )

        body = PostDocumentRequest(
            document=paperless_document,
            created=datetime.now(),
        )

        response = await documents_post_document_create.asyncio(
            client=self.client,
            body=body
        )

        return response, f"Successfully uploaded: {document.filename}"
    
    except httpx.HTTPError as e:
        return None, f"Network error during upload: {e}"

    except Exception as e:
        return None, f"Upload Error: {e}"
