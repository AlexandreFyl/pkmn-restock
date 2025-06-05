import asyncio
import pytest
from pkmn_restocker.monitor import main
from pkmn_restocker.retailers.generic_html import GenericHTMLRetailer
from pkmn_restocker.retailers.base import ProductInfo

@pytest.mark.asyncio
async def test_monitor_disable_notifications(tmp_path, monkeypatch):
    cfg = tmp_path / 'c.yaml'
    cfg.write_text('''
retailers:
  - name: test
    url: https://example.com
notifiers:
  discord_webhook: http://hook
''')
    async def dummy_check(self, session):
        return ProductInfo(name='test', url='https://example.com', price=None, in_stock=True)
    monkeypatch.setattr(GenericHTMLRetailer, 'check', dummy_check)
    called = False
    class DummyNotifier:
        def __init__(self, url):
            pass
        def send(self, message):
            nonlocal called
            called = True
    monkeypatch.setattr('pkmn_restocker.monitor.DiscordNotifier', DummyNotifier)
    await main(str(cfg), disable_notifications=True)
    assert not called
