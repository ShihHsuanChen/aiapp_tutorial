import os
import logging

from aiapp_tutorial.cli import cli


if __name__ == '__main__':
    # path setting
    os.environ['INFER_MODEL_NAME_OR_PATH'] = os.path.join('models', 'mobilenetv4_conv_small.e2400_r224_in1k')
    # run cli
    cli()
