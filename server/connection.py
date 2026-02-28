import os
import httpx
from dotenv import load_dotenv
from immich_client import AuthenticatedClient

load_dotenv()

class ConnectionManager:
    def __init__(self):
        self.immich_client = None
        # jellyfin
        # paperless

        self.local_ip = os.getenv("LOCAL_IP", "")
        self.tailscale_ip = os.getenv("TAILSCALE_IP", "")
        self.immich_key = os.getenv("IMMICH_KEY", "")

    async def connect_all(self):
        print("- - - Server Connection Start - - -")
        await self.connect_immich()
        # await self.connect_jellyfin()
        # await self.connect_paperless()
        print("- - - Connection Setup Complete - - -")

    async def check_connection(self, url):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, timeout=2.0)
                if response.status_code == 200:
                    return True
        except Exception:
            return False

        return False

    async def connect_immich(self):
        local_url = f"http://{self.local_ip}:2283"
        print(f"Attempting local connection: {local_url}")
        
        local_attempt = await self.check_connection(f"{local_url}/server-info/ping")

        if local_attempt:
            self.immich_client = AuthenticatedClient(
                base_url=local_url + "/api",
                token=self.immich_key
            )
            print("Connected to Immich through Local Address.")
            return

        print("Local Address did not find Immich. Trying Tailscale...")
        tailscale_url = f"http://{self.tailscale_ip}:2283"
        vpn_attempt = await self.check_connection(f"{tailscale_url}/server-info/ping")

        if vpn_attempt:
            self.immich_client = AuthenticatedClient(
                base_url=tailscale_url + "/api",
                token=self.immich_key,
                auth_header_name="x-api-key",
                prefix=""
            )
            print("Connected to Immich through Tailscale.")
        else:
            print("Did not connect to Immich.")
            self.immich_client = None

    async def connect_jellyfin(self):
        pass

    async def connect_paperless(self):
        pass

    def get_all_statuses(self):
        return {
            "Immich": self._get_client_url(self.immich_client),
            "Jellyfin": "Not implemented",
            "Paperless": "Not implemented"
        }

    def _get_client_url(self, client):
        if not client:
            return "Disconnected"

        url = getattr(client, 'base_url', getattr(client, '_base_url', 'Unknown'))
        if "Unknown" in url:
            return "Connected (Unknown URL)"
        return f"Connected ({url})"
