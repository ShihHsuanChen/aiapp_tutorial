# Image classification Inference Application

Doing image classification using `timm/mobilenetv4_conv_small.e2400_r224_in1k`

## Dependencies
- `python==3.8`
- `torch==2.2.1(+cu121)`
- `torchvision==0.17.1(+cu121)`
- `Pillow==10.2.0`
- `timm==1.0.7`
- `imagenet-stubs` (imagenet labelmap)
- `six` (required by `imagenet-stubs`)

## Setup environment

1. Create a new environment (conda)

```
$ conda create -n aiapp_tutorial python=3.8
```

2. Install dependencies

- By `requirements.txt`

    ```
    $ pip install -e requirements/basic.txt
    ```

- By this package

    ```
    $ pip install -e .
    ```

## Run

## Build
