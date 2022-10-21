import os

import pytest


@pytest.fixture
def history_file(tmp_path):
    history_file = tmp_path / 'husk'
    history_file.mkdir(parents=True, exist_ok=True)
    history_file /= '.history'
    history_file.touch()
    return history_file


@pytest.fixture
def chdir_safe_path(tmp_path):
    current_path = os.getcwd()
    yield tmp_path
    os.chdir(current_path)
