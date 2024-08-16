# AI APP Tutorial

This is a tutorial for building a simple AI inference application.

## Contents

1. Write an inference code of **MobileNet** from `timm`
    - `timm/mobilenetv4_conv_small.e2400_r224_in1k`
    - Example from [HuggingFace](https://huggingface.co/timm/mobilenetv4_conv_small.e2400_r224_in1k)
    - Write down the critical dependencies in `requirements.txt`

2. Initialize as a new git repository
    - `git init`
    - Add `.gitignore` file
    - `git add` and `git commit`
    - (Optional) Create a new repository on your git service (i.e. [GitHub](https://github.com)) and set the remote url
    - (Optional) `git push`

3. Basic layout to make this repository a python package
4. Re-write the inference code as a command line interface (CLI) application
    - User interface: CLI layer
    - Business logics: application layer
    - Technical logics: core

5. Write some testing for this application
    - Unit test
    - End-to-end test

6. Setup pyinstaller build files
    - Handle hidden imports
    - Handle data files
    - (optional) using `cmd_config` as the configuration tool for build

7. (Optional) Pack build files using `Inno Setup Compiler` (Windows) or `deb` (Linux/debian, ubuntu)

8. (Optional) Write a simple FastAPI project for this inference application

9. (Optional) Build docker image and setup docker-compose of this FastAPI project.
