import discord
import httpx
import os
import io
import uuid
from datetime import datetime, timezone

from paperless_client.types import File
from paperless_client.models import (
    PostDocumentRequest
)

from paperless_client.api.documents import documents_post_document_create

SUPPORTED_EXTENSIONS = {
    ".pdf", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".tif", ".tiff", 
    ".txt", ".csv", ".md", ".eml", ".msg", 
    ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    ".odt", ".ods", ".odp"
}

async def upload_document(self, document: discord.Attachment):
    try:
        if self.client is None:
            return "Not connected to Paperless client."

        file_ext = os.path.splitext(document.filename)[1].lower()
        
        if file_ext not in SUPPORTED_EXTENSIONS:
            return f"Unsupported file type '{file_ext}'. Paperless-ngx accepts PDFs, images, Office documents, and plain text."
        
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
            created=datetime.now(timezone.utc)
        )

        response = await documents_post_document_create.asyncio_detailed(
            client=self.client,
            body=body
        )

        if response.status_code not in (200, 201, 202):
            error_msg = response.content.decode("utf-8") if response.content else "No content"
            return f"Upload rejected by Paperless (Status {response.status_code}): {error_msg}"

        return response, f"Successfully uploaded: {document.filename}"
    
    except httpx.HTTPError as e:
        return f"Network error during upload: {e}"

    except Exception as e:
        return f"Upload Error: {e}"
