import os
import contextlib

from Husk import user_data


@contextlib.contextmanager
def History(*history_file_path):
    if len(history_file_path) == 0:
        raise ValueError('length of `history_file_path` can\'t be 0.')

    os.makedirs(user_data.xdg_data(), exist_ok=True)

    with open(user_data.xdg_data(*history_file_path), 'r') as f:
        data = list(
            hdr.replace('\n', '')
            for hdr in f.readlines()
            if hdr != '\n'
        )

    try:
        yield data
    finally:
        with open(user_data.xdg_data(*history_file_path), 'w') as f:
            f.write('\n'.join(data) + '\n')
