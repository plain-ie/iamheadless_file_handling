from .conf import settings
from .loader import load


def get_file_handling_backend():
    return load(settings.FILE_HANDLING_BACKEND_CLASS)
