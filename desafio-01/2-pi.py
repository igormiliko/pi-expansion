from mpmath import mp
# mp.dps=100000
mp.dps=100

PI = str(mp.pi)
slicer = 0

print(len(PI))

PI = PI.replace('.', '')

for ix, c in enumerate(PI):
    str_to_compare = ''
    
    if(ix == len(PI) - 9):
        print('break')
        break
    for i in range(9):
        str_to_compare += PI[slicer]
        slicer += 1
    print(str_to_compare)
    slicer = ix
