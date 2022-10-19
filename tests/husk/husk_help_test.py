from Husk.husk import Husk_help


def test_husk_help(capsys):
    Husk_help()
    out, err = capsys.readouterr()
    assert out == (
        'Husk: shell written in Python. use the \'-h\' command for help\n'
        'You can use the following commands within Husk:\n'
        '    \n'
        '    -h for help\n'
        '    ls to list files\n'
        '    rm to remove a file/directory\n'
        '    \n'
    )
    assert err == ''
