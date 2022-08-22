from mpmath import mp
# import numba
from numba import jit

mp.dps = 100500

PI = str(mp.pi)
slicer = 0

PI = PI.replace('.', '')

def main():
    for ix, c in enumerate(PI):
        prime_checker = 0
        number_to_check = 0

        if (ix == len(PI) - 9):
            print('break')
            break
        number_to_check = int(PI[ix:ix + 9])

        # Prime verify
        prime_verify(number_to_check, prime_checker, ix)

    print('end')

@jit
def prime_verify(number_to_check, prime_checker, ix):
    for i in range(2,number_to_check):
        if(len(str(number_to_check)) < 9):
            break
        if (number_to_check % i == 0):
            prime_checker += 1
        if(prime_checker > 0):
            break  

    if(prime_checker==0):
        print('Is PRIME => ', number_to_check)
        if(str(prime_checker) == str(prime_checker)[::-1]):
            print('PRIME and PALINDROME => ', ix, ' - ', number_to_check)
    return 0

if __name__ == '__main__':
    main()
