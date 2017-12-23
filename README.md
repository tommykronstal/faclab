### fac repository
git clone https://github.com/fnevgeny/fac.git

### mpi configure makefile

```mpicc --showme:compile sfac.c```
-> sfac.c -I/usr/local/include -pthread -I/usr/local/include -pthread

```mpicc --showme:link sfac.c```
-> -pthread -Wl,-rpath -Wl,/usr/local/lib -Wl,--enable-new-dtags -L/usr/local/lib -lmpi

./configure --with-mpi=mpicc --with-mpicompile="-I/usr/local/include -pthread" --with-mpilink="-pthread -Wl,-rpath -Wl,/usr/local/lib -Wl,--enable-new-dtags -L/usr/local/lib -lmpi"

### mpi run
mpirun -np 2 -hostfile hostfile ./hello-mpi.exe

mpirun -np 2 -hostfile hostfile python bed.py