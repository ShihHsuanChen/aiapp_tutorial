from . import __version__


def cli():
    print('hello')
    print('version', __version__)

    # only for test
    from .main import inference
    fname = 'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'
    result = inference(fname, topk=5)
    print(fname)
    for i, (label, prob) in enumerate(result):
        print(f'{i+1}. {label} ({prob})')
