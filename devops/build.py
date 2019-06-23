import contextlib
import hashlib
import os

from shutil import copy, copytree, rmtree, make_archive


def clean_build_dir():
    print('Cleaning up old build files...')
    with contextlib.suppress(FileNotFoundError):
        os.remove('.venv/Lib/site-packages/siren_call.py')


def copy_app_to_build_dir():
    print('Copying app to build dir...')
    copy('siren_call.py', '.venv/Lib/site-packages')


def build_app():
    print('Building app...')
    make_archive('dist/siren_call', 'zip', '.venv/Lib/site-packages')

    BUF_SIZE = 32768  # Read file in 32kb chunks
    md5 = hashlib.md5()

    with open('dist/siren_call.zip', "rb") as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)

    os.rename('dist/siren_call.zip', f'dist/siren_call_{md5.hexdigest()}.zip')

    print(f'Filename is : siren_call_{md5.hexdigest()}.zip')


if __name__ == '__main__':
    """ Little helper util to make process of creating a deployable faster.  .zip is created in local dist folder"""
    clean_build_dir()
    copy_app_to_build_dir()
    build_app()
