import yaml
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class RetailerConfig:
    name: str
    url: str
    in_stock_text: str = "En stock"

@dataclass
class NotifierConfig:
    discord_webhook: str = ""
    telegram_bot_token: str = ""
    telegram_chat_id: str = ""

@dataclass
class Config:
    retailers: List[RetailerConfig]
    notifiers: NotifierConfig

    @staticmethod
    def load(path: Path) -> 'Config':
        data = yaml.safe_load(path.read_text())
        retailers = [RetailerConfig(**r) for r in data.get('retailers', [])]
        notifiers = NotifierConfig(**data.get('notifiers', {}))
        return Config(retailers=retailers, notifiers=notifiers)
