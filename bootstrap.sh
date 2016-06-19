#!/usr/bin/env bash

# Add an apt-get repository that hosts python3.5
sudo add-apt-repository ppa:fkrull/deadsnakes

# Install desired system libraries
apt-get update
apt-get install -y build-essentials
apt-get install -y emacs24
apt-get install -y git
apt-get install -y python3.5
apt-get install -y python3-pip
apt-get install -y ruby1.9.1-dev

# Install virtualenv for python3
pip3 install virtualenv

# Install the travis command line tool
gem install travis -v 1.8.2 --no-rdoc --no-ri
