import aiohttp
from bs4 import BeautifulSoup
from typing import Optional
from .base import ProductInfo

class GenericHTMLRetailer:
    def __init__(self, name: str, url: str, in_stock_text: str = "En stock"):
        self.name = name
        self.url = url
        self.in_stock_text = in_stock_text

    async def check(self, session: aiohttp.ClientSession) -> ProductInfo:
        async with session.get(self.url, timeout=10) as resp:
            text = await resp.text()
        soup = BeautifulSoup(text, 'html.parser')
        title = soup.title.string if soup.title else self.name
        in_stock = self.in_stock_text.lower() in text.lower()
        return ProductInfo(name=title.strip(), url=self.url, price=None, in_stock=in_stock)
