"""
This file do the unit test for aiapp_tutorial.model functions:
- load_model
"""
import pytest
from PIL import Image
from helpers import get_data_path

import aiapp_tutorial.model


@pytest.fixture()
def image_obj():
    return Image.open(get_data_path('cloth.jpg'))


@pytest.mark.parametrize(
    'model_name_or_path, islocal',
    [
        ('mobilenetv4_conv_small.e2400_r224_in1k', False),
        ('mobilenetv4_conv_small.e2400_r224_in1k', True),
    ],
)
def test_load_model(model_name_or_path, islocal, image_obj):
    # prepare
    from aiapp_tutorial.model import InferModel
    if islocal:
        model_name_or_path = get_data_path(model_name_or_path)
    topk = 6

    # execute 1
    model = aiapp_tutorial.model.load_model(model_name_or_path)

    # test 1: return type
    assert isinstance(model, InferModel)

    # execute 2: inference
    res = model.inference(image_obj, topk=topk)
    # test 2: inference results
    assert isinstance(res, list)
    assert len(res) == topk
    for label, prob in res:
        assert isinstance(label, str)
        assert isinstance(prob, float)
