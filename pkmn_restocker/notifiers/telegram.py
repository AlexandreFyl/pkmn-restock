import requests
from dataclasses import dataclass

@dataclass
class TelegramNotifier:
    bot_token: str
    chat_id: str

    def send(self, message: str) -> None:
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        data = {"chat_id": self.chat_id, "text": message}
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()
