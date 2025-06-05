from pathlib import Path
import argparse
import asyncio
import aiohttp
from .config import Config
from .retailers.generic_html import GenericHTMLRetailer
from .notifiers.discord import DiscordNotifier
from .notifiers.telegram import TelegramNotifier

async def check_retailer(session, retailer_cfg, notifiers):
    retailer = GenericHTMLRetailer(retailer_cfg.name, retailer_cfg.url, retailer_cfg.in_stock_text)
    info = await retailer.check(session)
    if info.in_stock:
        message = f"{info.name} available at {info.url}"
        for n in notifiers:
            n.send(message)
        print(message)

async def main(config_path='config.yaml', disable_notifications: bool = False):
    config = Config.load(Path(config_path))
    notifiers = []
    if not disable_notifications:
        if config.notifiers.discord_webhook:
            notifiers.append(DiscordNotifier(config.notifiers.discord_webhook))
        if config.notifiers.telegram_bot_token and config.notifiers.telegram_chat_id:
            notifiers.append(TelegramNotifier(config.notifiers.telegram_bot_token, config.notifiers.telegram_chat_id))

    async with aiohttp.ClientSession() as session:
        tasks = [check_retailer(session, r, notifiers) for r in config.retailers]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('config', nargs='?', default='config.yaml')
    parser.add_argument('--disable-notifications', action='store_true', help='do not send messages')
    args = parser.parse_args()
    asyncio.run(main(args.config, disable_notifications=args.disable_notifications))
