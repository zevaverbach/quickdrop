import os
from pathlib import Path
import sys

import click
import dropbox
import pyperclip


DROPBOX_ACCESS_TOKEN = os.getenv('DROPBOX_ACCESS_TOKEN')
DROPBOX_ROOT_PATH = os.getenv('DROPBOX_ROOT_PATH')
LB = '\n'


@click.command()
@click.argument('filepath', type=click.Path(exists=True))
def cli(filepath):
    check_for_env_vars()
    dropbox_relative_path = get_relative_path(filepath)
    url = share_file(dropbox_relative_path)
    copy_to_clipboard(url)
    print(f'Okay, {filepath} is now shared, accessible via {LB}{url}.')
    print('This url was also copied to your clipboard for your convenience.')


def share_file(filepath):
    try:
        shared_link = get_client().sharing_create_shared_link(filepath)
    except dropbox.exceptions.ApiError as e:
        raise click.ClickException('There was a problem with the path.')
    else:
        return shared_link.url


def get_relative_path(filepath):
    DROPBOX_ROOT = Path(DROPBOX_ROOT_PATH).expanduser()

    if '/' not in filepath:
        filepath = f'/{filepath}'

    elif not filepath.startswith('/') and not filepath.startswith('~'):
        *path_parts, filename = filepath.split('/')
        relevant_path_parts = []
        for path_part in path_parts:
            if path_part not in DROPBOX_ROOT_PATH:
                relevant_path_parts.append(path_part)
        filepath = os.path.join(*relevant_path_parts, f'/{filename}')

    filepath_expanded_user = Path(filepath).expanduser()

    path = Path(str(filepath_expanded_user).replace(str(DROPBOX_ROOT), ''))

    return str(path)


def check_for_valid_access_token():
    if not DROPBOX_ACCESS_TOKEN:
        raise click.ClickException(
            'Please get an access token here and store it in an environment '
            'variable called "DROPBOX_ACCESS_TOKEN": '
            ' https://www.dropbox.com/developers/apps')
    try:
        dbx = get_client()
        dbx.users_get_current_account()
    except dropbox.exceptions.AuthError as e:
        raise click.ClickException(str(e))


def check_for_env_vars():
    check_for_valid_access_token()
    check_for_dropbox_root_path()


def check_for_dropbox_root_path():
    if not DROPBOX_ROOT_PATH:
        raise click.ClickException(
            'Please create an environment variable called "DROPBOX_ROOT_PATH" '
            'with the path to your computer\'s root Dropbox folder.')
    if not Path(DROPBOX_ROOT_PATH).exists:
        raise click.ClickException(f'{DROPBOX_ROOT_PATH} doesn\'t exist!')


def get_client():
    return dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)


def copy_to_clipboard(url):
    pyperclip.copy(url)
