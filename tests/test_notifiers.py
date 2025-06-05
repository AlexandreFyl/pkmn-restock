import pkmn_restocker.notifiers.discord as discord
import pkmn_restocker.notifiers.telegram as telegram

class DummyResponse:
    def __init__(self):
        self.status_code = 200
    def raise_for_status(self):
        pass

class DummyRequests:
    def __init__(self):
        self.called = False
        self.args = None
        self.kwargs = None
    def post(self, *args, **kwargs):
        self.called = True
        self.args = args
        self.kwargs = kwargs
        return DummyResponse()

def test_discord_notifier(monkeypatch):
    dummy = DummyRequests()
    monkeypatch.setattr(discord, 'requests', dummy)
    n = discord.DiscordNotifier('http://example.com')
    n.send('hi')
    assert dummy.called
    assert dummy.args[0] == 'http://example.com'

def test_telegram_notifier(monkeypatch):
    dummy = DummyRequests()
    monkeypatch.setattr(telegram, 'requests', dummy)
    n = telegram.TelegramNotifier('token', 'chat')
    n.send('hi')
    assert dummy.called
    assert 'token' in dummy.args[0]
