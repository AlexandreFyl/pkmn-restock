from pathlib import Path
from pkmn_restocker.config import Config

def test_load_config(tmp_path):
    text = """
retailers:
  - name: test
    url: https://example.com
notifiers:
  discord_webhook: http://hook
"""
    path = tmp_path / 'c.yaml'
    path.write_text(text)
    config = Config.load(path)
    assert config.retailers[0].name == 'test'
    assert config.notifiers.discord_webhook == 'http://hook'
