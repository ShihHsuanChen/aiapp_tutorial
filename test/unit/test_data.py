"""
This file do the unit test for aiapp_tutorial.data functions:
- read_image(image_path: str) -> PIL.Image.Image
"""

import pytest
from PIL import Image
from helpers import get_data_path, does_not_raise

import aiapp_tutorial.data


@pytest.mark.parametrize(
    'fname, islocal, expect_success',
    [
        ('beignets-task-guide.png', True, True),
        ('cloth.jpg', True, True),
        ('https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png', False, True),
        ('notanimage.csv', True, False),
    ],
    ids=[
        'local_png',
        'local_jpg',
        'url_png',
        'csv', # expect fail
    ],
)
def test_read_image(fname, islocal, expect_success):
    # prepare
    if islocal:
        path = get_data_path(fname)
    else:
        path = fname

    # test for raising error by given condition "expect_success"
    if expect_success:
        check_raises = does_not_raise()
    else:
        check_raises = pytest.raises(Exception)

    # execute and test
    with check_raises:
        res = aiapp_tutorial.data.read_image(path)

    # test return type if expect_success
    if expect_success:
        assert isinstance(res, Image.Image)
