
from pfac import fac
import time

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print "hello world from process ", rank

print 'Be-like C III'

t = str(time.localtime())
print 'Script started at', t

# Atomic Structure

print 'calculating atomic structure'

fac.SetAtom('C')

fac.Config('1s2 2s', group = 'lithium')
fac.Config('1s2 2*2', group = 'ground')

fac.Config('1s2 2*1 3*1', group = '2exc3')
fac.Config('1s2 2*1 4*1', group = '2exc4')
fac.Config('1s2 2*1 5*1', group = '2exc5')

fac.Config('1s 2*3', group = '1exc2')
fac.Config('1s 2*2 3*1', group = '1exc3')
fac.Config('1s 2*2 4*1', group = '1exc4')
fac.Config('1s 2*2 5*1', group = '1exc5')

fac.ConfigEnergy(0)
fac.OptimizeRadial(['ground'])
fac.ConfigEnergy(1)

fac.Structure('beb.en', ['ground'])
fac.Structure('beb.en', ['2exc3'])
fac.Structure('beb.en', ['2exc4'])
fac.Structure('beb.en', ['2exc5'])
fac.Structure('beb.en', ['1exc2'])
fac.Structure('beb.en', ['1exc3'])
fac.Structure('beb.en', ['1exc4'])
fac.Structure('beb.en', ['1exc5'])
fac.Structure('beb.en', ['lithium'])

g = ['ground', '2exc3', '2exc4', '2exc5', '1exc2', '1exc3', '1exc4', '1exc5']

fac.MemENTable('beb.en')
fac.PrintTable('beb.en', 'bea.en', 1)

# Radiative Transitions

for i in range(len(g)):
    for j in range(i,len(g)):
    	print 'calculating radiative transitions between', g[i], 'and', g[j]
        fac.TransitionTable('beb.tr', [g[i]], [g[j]])

fac.PrintTable('beb.tr', 'bea.tr', 1)

# Collisional Transitions

print 'calculating collisional transitions'

for i in range(len(g)):
    fac.CETable('beb.ce', ['ground'], [g[i]])

fac.PrintTable('beb.ce', 'bea.ce', 1)

# Autoionization Rates

print 'calculating AI rates'

for i in range(len(g)):
    fac.AITable('beb.ai', [g[i]], ['lithium'])

fac.PrintTable('beb.ai', 'bea.ai', 1)

t = str(time.localtime())
print 'Script finished at', t