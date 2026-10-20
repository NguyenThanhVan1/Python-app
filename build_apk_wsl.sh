#!/bin/bash
set -e
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev cmake libffi-dev libssl-dev
python3 -m pip install --user --upgrade buildozer cython==0.29.34
buildozer -v android debug
echo "APK created in: bin/"
