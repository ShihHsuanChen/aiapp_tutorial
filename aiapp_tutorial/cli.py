from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def cli():
    # define command line interface
    parser = ArgumentParser(
        prog='myaiapp',
        description='Doing image classification using MobileNet',
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        '-v', '--version',
        action='store_true',
        help='show version',
    )
    parser.add_argument(
        '-k', '--topk',
        default=5,
        type=int,
        help='list predict classes of top-k highest probabilities',
    )
    parser.add_argument(
        'image_path',
        nargs='?',
        help='image path or url',
    )

    args = parser.parse_args()

    if args.version:
        _show_version()
        return

    if args.image_path:
        _inference(args.image_path, topk=args.topk)
    else:
        print('Require image path or url')


def _show_version():
    from . import __version__
    print(__version__)


def _inference(image_path, topk: int = 5):
    # cli-level code: pass parameters from command line to app-level function
    # import here can make other subcommand or options execute faster since
    # there is `import torch` when import inference from main.py
    from .main import inference
    result = inference(image_path, topk=topk)
    print(image_path)
    for i, (label, prob) in enumerate(result):
        print(f'{i+1}. {label} ({prob})')
