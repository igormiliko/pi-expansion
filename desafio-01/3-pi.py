from mpmath import mp
# mp.dps=100000
mp.dps = 100

PI = str(mp.pi)
slicer = 0
prime_checker = 0

print(len(PI))

PI = PI.replace('.', '')

for ix, c in enumerate(PI):
    number_to_check = 0

    if (ix == len(PI) - 9):
        print('break')
        break
    number_to_check = int(PI[ix:ix + 9])

    # Prime verify
    for i in range(2,number_to_check):
        if (number_to_check % i == 0):
            prime_checker += 1
    if(prime_checker==0):
        print("PRIME => ", number_to_check)
    else:
        print("Have",prime_checker," multiples big than 2 and less than ",number_to_check)
