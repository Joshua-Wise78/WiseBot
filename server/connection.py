import os
import httpx
from dotenv import load_dotenv
from immich_client import AuthenticatedClient as ImmichClient
from paperless_client import AuthenticatedClient as PaperlessClient
from paperless_client.api.status import status_retrieve

load_dotenv()


class ConnectionManager:
    def __init__(self):
        self.use_tailscale_only = False
        self.immich_client = None
        self.paperless_client = None
        # jellyfin

        self.local_ip = os.getenv("LOCAL_IP", "")
        self.tailscale_ip = os.getenv("TAILSCALE_IP", "")
        self.immich_key = os.getenv("IMMICH_KEY", "")
        self.paperless_key = os.getenv("PAPERLESS_KEY", "")

    async def connect_all(self):
        print("- - - Server Connection Start - - -")
        await self.connect_immich()
        await self.connect_paperless()
        print("- - - Connection Setup Complete - - -")

    async def check_connection(self, url, headers=None):
        try:
            async with httpx.AsyncClient(follow_redirects=True) as client:
                response = await client.get(url, headers=headers, timeout=2.0)
                if response.status_code == 200:
                    return True
                else:
                    print(
                        f"Warning: {url} returned status code {response.status_code}"
                    )
        except Exception as e:
            print(f"Warning: Exception when connecting to {url}: {e}")
            return False

        return False

    async def connect_immich(self):
        local_url = f"http://{self.local_ip}:2283"
        if not self.use_tailscale_only:
            print(f"Attempting local connection: {local_url}")

            local_attempt = await self.check_connection(
                f"{local_url}/server-info/ping"
            )

            if local_attempt:
                self.immich_client = ImmichClient(
                    base_url=local_url + "/api", token=self.immich_key
                )
                print("Connected to Immich through Local Address.")
                return

        print("Local Address did not find Immich. Trying Tailscale...")

        tailscale_url = f"http://{self.tailscale_ip}:2283"
        vpn_attempt = await self.check_connection(
            f"{tailscale_url}/server-info/ping"
        )

        if vpn_attempt:
            self.immich_client = ImmichClient(
                base_url=tailscale_url + "/api",
                token=self.immich_key,
                auth_header_name="x-api-key",
                prefix="",
            )
            print("Connected to Immich through Tailscale.")
        else:
            print("Did not connect to Immich.")
            self.immich_client = None

    async def connect_jellyfin(self):
        pass

    async def connect_paperless(self):
        headers = {}

        if self.use_tailscale_only:
            local_url = f"http://{self.local_ip}:8000"
            print(f"Attempting local connection: {local_url}")

            headers = {"Authorization": f"Token {self.paperless_key}"}
            local_attempt = await self.check_connection(
                f"{local_url}/api/", headers=headers
            )

            if local_attempt:
                self.paperless_client = PaperlessClient(
                    base_url=local_url,
                    token=self.paperless_key,
                    auth_header_name="Authorization",
                    prefix="Token",
                )
                print("Connected to Paperless through Local Address.")
                return

        print("Local Address did not find Paperless. Trying Tailscale...")

        tailscale_url = f"http://{self.tailscale_ip}:8000"
        vpn_attempt = await self.check_connection(
            f"{tailscale_url}/api/", headers=headers
        )

        if vpn_attempt:
            self.paperless_client = PaperlessClient(
                base_url=tailscale_url,
                token=self.paperless_key,
                auth_header_name="Authorization",
                prefix="Token",
            )
            print("Connected to Paperless through Tailscale.")
        else:
            print("Did not connect to Paperless.")
            self.paperless_client = None

    def get_all_status(self):
        return {
            "Immich": self._get_client_url(self.immich_client),
            "Jellyfin": "Not implemented",
            "Paperless": self._get_client_url(self.paperless_client),
        }

    def _get_client_url(self, client):
        if not client:
            return "Disconnected"

        url = getattr(
            client, "base_url", getattr(client, "_base_url", "Unknown")
        )
        if "Unknown" in url:
            return "Connected (Unknown URL)"
        return f"Connected ({url})"
