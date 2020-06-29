from pycubescrambler import nxn,side,bld,non

#gets 1x1 scramble and prints it out

scramble=nxn.get1()

print(scramble)

#gets 2x2 scramble and prints it out

scramble=nxn.get2()

print(scramble)

#gets 3x3 scramble and prints it out

scramble=nxn.get3()

print(scramble)

#gets 4x4 scramble and prints it out

scramble=nxn.get4()

print(scramble)

#gets 5x5 scramble and prints it out

scramble=nxn.get5()

print(scramble)

#gets 6x6 scramble and prints it out

scramble=nxn.get6()

print(scramble)


#gets 7x7 scramble and prints it out

scramble=nxn.get7()

print(scramble)

#gets a big cube of size 100 (100x100)

scramble=nxn.get_big_cube(100)

print(scramble)

#gets fmc scramble and prints it out

scramble=nxn.get_fmc()

print(scramble)

#gets skewb scramble and prints it out

scramble=side.get_skewb()

print(scramble)

#gets pyraminx scramble and prints it out

scramble=side.get_pyra()

print(scramble)

#gets clock scramble and prints it out

scramble=side.get_clock()

print(scramble)

#gets megaminx scramble and prints it out

scramble=side.get_mega()

print(scramble)

#gets 3bld scramble and prints it out

scramble=bld.get3()

print(scramble)

#gets 4bld scramble and prints it out

scramble=bld.get4()

print(scramble)

#gets 5bld scramble and prints it out

scramble=bld.get5()

print(scramble)

#gets ivy cubescramble

scramble=non.get_ivy()

print(scramble)
