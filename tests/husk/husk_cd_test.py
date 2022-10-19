import os

from Husk.husk import Husk_cd


def test_husk_cd_existing_directory(chdir_safe_path):
    Husk_cd(chdir_safe_path)
    assert os.getcwd() == str(chdir_safe_path)


def test_husk_cd_non_existing_directory(capsys):
    Husk_cd('/definitely/not/existing/path')
    out, err = capsys.readouterr()
    assert out == 'cd: no such file or directory: /definitely/not/existing/path\n'
    assert err == ''
