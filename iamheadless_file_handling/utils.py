import uuid

from .conf import settings
from .loader import load


def get_file_handling_backend():
    return load(settings.FILE_HANDLING_BACKEND_CLASS)


def get_file_name(prefix, file_name):
    if prefix.startswith('/') is False:
        prefix = '/' + prefix
    if prefix.endswith('/') is False:
        prefix = prefix + '/'
    id = str(uuid.uuid4()).split('-')[-1]
    file_name = f'{id}-{file_name}'
    return f'{prefix}{file_name}'
