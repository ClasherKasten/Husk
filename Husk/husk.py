import os, subprocess, readchar
from Husk import history


def execute_command(command):
    """execute commands and handle piping"""
    try:
        if "|" in command:
            # save for restoring later on
            s_in, s_out = (0, 0)
            s_in = os.dup(0)
            s_out = os.dup(1)

            # first command takes commandut from stdin
            fdin = os.dup(s_in)

            # iterate over all the commands that are piped
            for cmd in command.split("|"):
                # fdin will be stdin if it's the first iteration
                # and the readable end of the pipe if not.
                os.dup2(fdin, 0)
                os.close(fdin)

                # restore stdout if this is the last command
                if cmd == command.split("|")[-1]:
                    fdout = os.dup(s_out)
                else:
                    fdin, fdout = os.pipe()

                # redirect stdout to pipe
                os.dup2(fdout, 1)
                os.close(fdout)

                try:
                    subprocess.run(cmd.strip().split())
                except Exception:
                    print("Husk: command not found: {}".format(cmd.strip()))

            # restore stdout and stdin
            os.dup2(s_in, 0)
            os.dup2(s_out, 1)
            os.close(s_in)
            os.close(s_out)
        else:
            subprocess.run(command.split(" "))
    except Exception:
        print("Husk: command not found: {}".format(command))


def husk_input(history_data):
    print(f'{os.getcwd()} $Husk>', end=' ', flush=True)
    command = ''
    cursor_pos = 0
    history_pos = len(history_data)
    while (key := readchar.readkey()) != readchar.key.ENTER:
        if key == readchar.key.LEFT:
            if cursor_pos == 0:
                continue
            cursor_pos -= 1
        elif key == readchar.key.RIGHT:
            if cursor_pos == len(command):
                continue
            cursor_pos += 1
        elif key == readchar.key.BACKSPACE:
            if cursor_pos == 0:
                continue

            if cursor_pos < len(command):
                command = command[:cursor_pos-1] + command[cursor_pos:]
                print(
                    f'\b{command[cursor_pos-1:]} ' \
                        + ('\b' * (len(command) - cursor_pos + 2)),
                    end='',
                    flush=True
                )
            elif cursor_pos == len(command):
                command = command[:-1]
                print('\b \b', end='', flush=True)
            cursor_pos -= 1
        elif key == readchar.key.UP:
            if history_pos == 0:
                continue
            history_pos -= 1
            print(
                ('\b' * cursor_pos) + (' ' * len(command)) \
                    + ('\b' * len(command)),
                end='', flush=False
            )
            command = history_data[history_pos]
            cursor_pos = len(command)
            print(command, end='', flush=True)
            continue
        elif key == readchar.key.DOWN:
            if (history_pos + 1) == len(history_data):
                print(
                    ('\b' * cursor_pos) + (' ' * len(command)) \
                        + ('\b' * len(command)),
                    end='', flush=True
                )
                command = ''
                cursor_pos = 0
                history_pos = len(history_data)
                continue
            elif history_pos == len(history_data):
                continue
            history_pos += 1
            print(
                '\b' * cursor_pos + ' ' * len(command) + '\b' * len(command),
                end='', flush=False
            )
            command = history_data[history_pos]
            cursor_pos = len(command)
            print(command, end='', flush=True)
            continue
        elif key == '\t':
            cursor_pos += 4
            key = key.expandtabs(4)
            command += '    '
        else:
            cursor_pos += 1
            command += key
        print(key, end='', flush=True)
    print()
    return command

def Husk_cd(path):
    """convert to absolute path and change directory"""
    try:
        os.chdir(os.path.abspath(path))
    except Exception:
        print("cd: no such file or directory: {}".format(path))


def Husk_help():
    print("Husk: A shell written entirely in Python. use the '-h' command to open the help menu")
    print("""Please note that traditional Shell commands apply within Husk. Try to git add, git commit, git push :)
    
    version: 1.0.0
    
    Author: 
    SchoolyB on GitHub
    
    Contributors:
    ClasherKasten on GitHub
    
    Standard Husk Commands:
    Enter '-h' to enter the help menu
    Enter 'clear' to clean up a cluttered terminal 
    Enter 'exit' to exit Husk
    Enter 'husk' to launch an instance of Husk
    Enter 'pwd' to print your working directory to the CLI   
    Enter 'ls' to list files in you current working directory
    Enter 'rm' followed by the name of a file in the current working directory to delete it
    Enter 'mv' followed by the name of file(s) or directory(s) you would like to move. Then add the name of the directory you would like to move the specified items into
    Enter 'mkdir' followed by a name to create a directory with that name  
    Enter 'cd ..' to go one directory higher 
    Enter 'cd' followed by the name of a directory to enter that directory as your new working directory """)


###main function##
def main():
    with history.History('.husk-history') as history_data:
        while True:
            inp = husk_input(history_data)
            history_data.append(inp)
            if inp == "exit":
                break
            elif inp[:3] == "cd ":
                Husk_cd(inp[3:])
            elif inp == "-h":
                Husk_help()
            else:
                execute_command(inp)


if '__main__' == __name__:
    main()
