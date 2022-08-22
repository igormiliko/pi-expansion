from mpmath import mp
# mp.dps=100000
mp.dps=100

PI = str(mp.pi)
slicer = 0

print(len(PI))

for ix, c in enumerate(PI):
    if(ix == len(PI) - 9):
        print('break')
        break
    for i in range(9):
        PI[slicer]
        slicer += 1
    slicer = ix