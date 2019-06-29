import contextlib
import os
import subprocess

from datetime import datetime
from shutil import copy, make_archive


def clean_build_dir():
    """ Clean previous build """
    print('Cleaning up old build files...')
    with contextlib.suppress(FileNotFoundError):
        os.remove('.venv/lib/python3.7/site-packages/siren_call.py')


def copy_app_to_build_dir():
    """ Copy new app file"""
    print('Copying app to build dir...')
    copy('./app/siren_call.py', '.venv/lib/python3.7/site-packages/')


def build_app() -> str:
    """ Create deployable zip archive """
    print('Building app...')
    make_archive('dist/siren_call', 'zip', '.venv/lib/python3.7/site-packages/')
    timestamp = datetime.now().strftime('%Y_%m_%d_%H%M%S')
    dist_file = f'siren_call_{timestamp}.zip'
    
    os.rename('dist/siren_call.zip', f'dist/{dist_file}')
    print(f'Filename is : dist/{dist_file}')
    return dist_file


def upload_to_s3(dist_file: str):
    """ Upload to deployable to s3 """
    s3_dest = f"s3://code-commit-build-artifacts/siren-call/{dist_file}"
    print(f"Uploading {dist_file} to {s3_dest}")
    subprocess.run(["aws", "s3", "mv", f"dist/{dist_file}", s3_dest])


if __name__ == '__main__':
    """ Little helper util to make process of creating a deployable faster. """
    clean_build_dir()
    copy_app_to_build_dir()
    dist_file = build_app()
    upload_to_s3(dist_file)
    print("To deploy...")
    print(f"python ./devops/deploy.py {dist_file}")
