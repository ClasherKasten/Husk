import pytest

from Husk.husk import execute_command


def test_unknown_command(capsys):
    execute_command('some-non-existing-commmand')
    out, err = capsys.readouterr()
    assert out == 'Husk: command not found: some-non-existing-commmand\n'
    assert err == ''


@pytest.mark.parametrize(
    ('command',),
    (('cd',), ('ls',), ('sh',), ('cd -',), ('echo 1',))
)
def test_known_command(command, capsys):
    execute_command(command)
    out, err = capsys.readouterr()
    assert out != f'Husk: command not found: {command}'
    assert err == ''


@pytest.mark.parametrize(
    ('command',),
    (('ls | echo',), ('ls | ls | echo',))
)
def test_command_with_pipes(command):
    execute_command(command)


@pytest.mark.parametrize(
    ('command', 'output'),
    (
        (
            'ls | some-non-existing-command',
            'psh: command not found: some-non-existing-command\n'
        ),
        (
            'non-existing-command | other-non-existing-command',
            'psh: command not found: non-existing-command\npsh: '
                'command not found: other-non-existing-command\n'
        )
    )
)
def test_unknown_commands_with_pipes(command, output, capsys):
    execute_command(command)
    out, err = capsys.readouterr()
    assert out == output
    assert err == ''
