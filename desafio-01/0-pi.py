from mpmath import mp
# mp.dps=100000
mp.dps=1000

PI = str(mp.pi)
slicer = 0

for ix, c in enumerate(PI):
    if(ix % 9 == 0):
        print(PI[slicer:ix + 9])
        slicer += 9