Centos 7.3

root password: fac

sudo user: fac
password: fac

sudo yum install redhat-lsb-core kernel-headers kernel-devel python-devel

sudo yum groupinstall “Development Tools”

yum update

sudo reboot

git clone https://github.com/fnevgeny/fac.git

cd fac

./configure

make
sudo make install

make pfac
sudo make install-pfac

shared folder: /media/sf_sharedfolder




mpicc --showme:compile sfac.c
sfac.c -I/usr/local/include -pthread -I/usr/local/include -pthread

mpicc --showme:link sfac.c
-pthread -Wl,-rpath -Wl,/usr/local/lib -Wl,--enable-new-dtags -L/usr/local/lib -lmpi


./configure --with-mpi=mpicc --with-mpicompile="-I/usr/local/include -pthread" --with-mpilink="-pthread -Wl,-rpath -Wl,/usr/local/lib -Wl,--enable-new-dtags -L/usr/local/lib -lmpi"


mpirun -np 2 -hostfile hostfile ./hello-mpi.exe

mpirun -np 2 -hostfile hostfile python bed.py