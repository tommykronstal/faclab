
""" calculation of the energy levels. and radiative transition rates
"""

from pfac import fac

fac.SetAtom('Fe')
# 1s shell is closed
fac.Closed('1s')
fac.Config('2*8', group = 'n2')
# instead of a keyword, the group name can also
# be given as the first argument.
fac.Config('n3', '2*7 3*1')
# Self-consistent iteration for optimized central potential
fac.ConfigEnergy(0)
# the configurations passed to OptimizeRadial should always
# be one or two of the lowest lying ones. and it is often best to
# just use the ground configurations. If you need more highly
# excited levels, such as n=4, 5, 6, ..., do not put them
# in the OptimizeRadial. 
fac.OptimizeRadial(['n2'])
fac.ConfigEnergy(1)
fac.GetPotential('ne.pot')
fac.Structure('ne.lev.b', ['n2', 'n3'])
fac.MemENTable('ne.lev.b')
fac.PrintTable('ne.lev.b', 'ne.lev', 1)

fac.TransitionTable('ne.tr.b', ['n2'], ['n3'])
fac.PrintTable('ne.tr.b', 'ne.tr', 1)

