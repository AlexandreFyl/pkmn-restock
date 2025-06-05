import requests
from dataclasses import dataclass

@dataclass
class DiscordNotifier:
    webhook_url: str

    def send(self, message: str) -> None:
        data = {"content": message}
        response = requests.post(self.webhook_url, json=data, timeout=10)
        response.raise_for_status()
