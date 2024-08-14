""" Write helper functions in this file """
import os
from contextlib import contextmanager


DATADIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def get_data_path(relpath: str):
    return os.path.join(DATADIR, relpath)


@contextmanager
def does_not_raise():
    try:
        yield
    except Exception as e:
        AssertionError(f'Expect no raise from statements, got {e}')
