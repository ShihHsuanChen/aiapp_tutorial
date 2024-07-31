# pip install torch==2.2.1 torchvision==0.17.1 --index-url https://download.pytorch.org/whl/cu121
from .model import load_model
from .data import read_image

# TODO from config
infer_model = load_model('mobilenetv4_conv_small.e2400_r224_in1k')


def inference(image_path: str, topk: int = 5):
    """
    Arguments:
        - image_path: (str) path or url of an image file
    Returns:
        Returns: (list) List of (class_name, probability) tuple
    """
    image = read_image(image_path)
    print('start inference')
    result = infer_model.inference(image)
    return result
