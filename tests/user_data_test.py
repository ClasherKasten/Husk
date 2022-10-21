import os
from unittest import mock

from Husk.user_data import xdg_data


def test_xdg_data_home_set():
    with mock.patch.dict(os.environ, {'XDG_DATA_HOME': '/some/path/to/data'}):
        ret = xdg_data('history', 'today')
    assert ret == '/some/path/to/data/husk/history/today'


def test_xdg_data_home_not_set():
    def mock_expanduser(s):
        return s.replace('~', '/home/username')

    with mock.patch.object(os.path, 'expanduser', mock_expanduser):
        with mock.patch.dict(os.environ, clear=True):
            ret = xdg_data('history', 'today')
        assert ret == '/home/username/.local/share/husk/history/today'
