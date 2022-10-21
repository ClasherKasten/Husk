from Husk.errorcodes import Syntax_Error
from Husk.errorcodes import User_Auth_Error1


def test_user_auth_error1(capsys):
    User_Auth_Error1()
    out, err = capsys.readouterr()
    assert out == 'Husk Error 01: The entered passwords do not match please try again\n'
    assert err == ''


def test_syntax_error(capsys):
    Syntax_Error()
    out, err = capsys.readouterr()
    assert out == 'Husk Error 02: SYNTAX ERROR\n'
    assert err == ''
