import os.path


# This file is part of `babi` which is released under MIT.
# Go to https://github.com/asottile/babi/blob/main/LICENSE for full license details.


def _xdg(*path, env, default):
    return os.path.join(
        os.environ.get(env) or os.path.expanduser(default),
        'husk', *path
    )


def xdg_data(*path):
    return _xdg(*path, env='XDG_DATA_HOME', default='~/.local/share')
