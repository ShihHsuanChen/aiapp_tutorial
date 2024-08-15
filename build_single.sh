#!/bin/bash
pyinstaller \
    -n Myaiapp \
    --onefile \
    --additional-hooks-dir=hook_files \
    --add-data=./models/mobilenetv4_conv_small.e2400_r224_in1k/:models/mobilenetv4_conv_small.e2400_r224_in1k \
    main.py
