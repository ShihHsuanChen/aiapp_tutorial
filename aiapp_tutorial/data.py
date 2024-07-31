from urllib.request import urlopen
from PIL import Image


# TODO handle failure case
def read_image(image_path: str):
    if image_path.startswith('http://') or image_path.startswith('https://'):
        # from url
        image = Image.open(urlopen(image_path))
    else:
        image = Image.open(image_path)
    return image
