#!/bin/bash

# Setup venv
python3 -m venv ./venv
source ./venv/bin/activate

# Setup environment and download packages
pip3 install --upgrade pip
pip3 install numpy pyyaml tensorflow==2.12.0 rospkg pyqt5 opencv-python Pillow pandas matplotlib pyserial
