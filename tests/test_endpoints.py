import os
from webtest import TestApp
from chimera_app.server import server
from chimera_app.config import PLATFORMS, AUTHENTICATOR_PATH


# Prevent pytest from trying to collect webtest's TestApp as tests:
TestApp.__test__ = False


def test_runs(monkeypatch):
    def mock_launch(self):
        if not os.path.isfile(AUTHENTICATOR_PATH):
            raise FileNotFoundError("Authenticator not found at path {}".format(AUTHENTICATOR_PATH))

    from chimera_app.authenticator import Authenticator
    monkeypatch.setattr(Authenticator, 'launch', mock_launch)

    app = TestApp(server)
    assert app.get('/login').status == '200 OK'


def test_platform_images():
    app = TestApp(server)
    for platform, name in PLATFORMS.items():
        assert app.get('/images/{}.png'.format(platform)).status == '200 OK'
