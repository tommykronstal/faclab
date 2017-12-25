#!/bin/bash

cleanSpace() {
    rm -rf /vagrant/fac* /vagrant/*.zip*
}

cleanSpace

sudo yum update -y
sudo yum install redhat-lsb-core kernel-headers wget kernel-devel python-devel -y
sudo yum groupinstall "Development Tools" -y

cd /vagrant
wget https://github.com/fnevgeny/fac/archive/v1.1.4.zip
unzip v1.1.4.zip && cd /vagrant/fac-1.1.4

./configure
make
sudo make install
make pfac
sudo make install-pfac

cleanSpace