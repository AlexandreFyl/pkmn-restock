from dataclasses import dataclass
from typing import Optional

@dataclass
class ProductInfo:
    name: str
    url: str
    price: Optional[float]
    in_stock: bool

async def fetch_json(session, url):
    async with session.get(url, timeout=10) as resp:
        resp.raise_for_status()
        return await resp.json()
