sudo yum update -y
sudo yum install redhat-lsb-core kernel-headers kernel-devel python-devel -y
sudo yum groupinstall "Development Tools" -y
sudo yum update -y

cd /vagrant/fac
./configure
make
sudo make install
make pfac
sudo make install-pfac