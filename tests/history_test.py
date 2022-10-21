import os
from unittest import mock

import pytest

from Husk.history import History


def test_history_file_doesnt_exist(tmp_path):
    with mock.patch.dict(os.environ, {'XDG_DATA_HOME': str(tmp_path)}):
        with History('.history') as data:
            ...

        assert data == []


def test_empty_history_file(tmp_path):
    with mock.patch.dict(os.environ, {'XDG_DATA_HOME': str(tmp_path)}):

        with History('.history') as data:
            ...

        assert data == []


def test_history_file(tmp_path, history_file):
    with mock.patch.dict(os.environ, {'XDG_DATA_HOME': str(tmp_path)}):
        with open(str(history_file), 'w') as f:
            f.write('ls\n-h\ncd\n')

        with History('.history') as data:
            ...

        assert data == ['ls', '-h', 'cd']


def test_history_file_with_empty_lines(tmp_path, history_file):
    with mock.patch.dict(os.environ, {'XDG_DATA_HOME': str(tmp_path)}):
        with open(history_file, 'w') as f:
            f.write('ls\n-h\n\n\ncd\n')

        with History('.history') as data:
            ...

        assert data == ['ls', '-h', 'cd']


def test_history_file_correct_write(tmp_path):
    with mock.patch.dict(os.environ, {'XDG_DATA_HOME': str(tmp_path)}):
        with History('.history') as data:
            assert data == []

            data.extend(('ls', '-h', 'cd'))

        with open(tmp_path / 'husk/.history', 'r') as f:
            assert f.read() == 'ls\n-h\ncd\n'


def test_history_path_not_present():
    with pytest.raises(
            ValueError,
            match='length of `history_file_path` can\'t be 0.'
    ):
        with History():
            ...
