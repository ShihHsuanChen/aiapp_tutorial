from urllib.request import urlopen
from PIL import Image


# TODO handle failure case
def read_image(image_path: str):
    if image_path.startswith('http://') or image_path.startswith('https://'):
        # from url
        image = Image.open(urlopen(image_path))
    else:
        # from local file
        with open(image_path, 'rb') as fp:
            image = Image.open(fp)
    return image
