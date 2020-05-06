# pycubescrambler
A scrambling module that generates scrambles for most wca events
example:

from pycubescrambler import nxn,side,bld

scramble=nxn.get3()

print(scramble)

#will display 3x3 scramble; 2-7 are supported and all work get2() get4() etc

scramble=bld.get3()

print(scramble)

#prints a 3bld scramble 4 and 5bld are get4() and get5()

scramble=side.get_skewb()

print(scramble)

#prints a skewb scramble, all of the side events are get_event name for example get_pyra() get_clock() get_mega()

fmc is nxn.get_fmc()
