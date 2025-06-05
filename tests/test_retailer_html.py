import aiohttp
import asyncio
import pytest
from aiohttp import web
from pkmn_restocker.retailers.generic_html import GenericHTMLRetailer

@pytest.mark.asyncio
async def test_generic_html_retailer_in_stock(unused_tcp_port):
    async def handler(request):
        return web.Response(text='<html><title>Hi</title>En stock</html>')
    app = web.Application()
    app.router.add_get('/', handler)
    runner = web.AppRunner(app)
    await runner.setup()
    port = unused_tcp_port
    site = web.TCPSite(runner, 'localhost', port)
    await site.start()

    retailer = GenericHTMLRetailer('test', f'http://localhost:{port}', 'En stock')
    async with aiohttp.ClientSession() as session:
        info = await retailer.check(session)
    await runner.cleanup()
    assert info.in_stock
    assert info.name == 'Hi'
