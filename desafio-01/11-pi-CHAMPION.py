import sys
from datetime import datetime
from mpmath import mp
from numba import cuda, njit, vectorize, int32, prange
mp.dps = 200000


PI = str(mp.pi)
pi_iteration_init = 0
PI_SLICER = 0
# PI_STOP = 0
PI = PI.replace('.', '')

if(len(sys.argv) > 1):
    pi_iteration_init = float(sys.argv[1])
    PI_SLICER = int(int(len(PI) * float(pi_iteration_init)))
    PI = PI[PI_SLICER:]

# PI_STOP = int(int(len(PI) * (float(pi_iteration_init + 0.1))))

print(f'Initializing the finder prime palindrome in PI |=>| {pi_iteration_init * 100}%')
# print(PI_STOP)
def main():
    palin_prime = ''
    for ix, c in enumerate(PI):
        # if(ix == PI_STOP):
            # break
        prime_checker = 0
        number_to_check = 0

        if (ix == len(PI) - 9):
            print('break')
            break

        number_to_check = int(PI[ix:ix + 9])
        
        if(len(str(number_to_check)) == 9):
            if(str(number_to_check) == str(number_to_check)[::-1]):
                buff = prime_verify(number_to_check, prime_checker, ix, PI_SLICER)
                if(buff):
                    if(str(buff) == str(buff)[::-1]):
                        print('PRIME and PALINDROME => ', ix + PI_SLICER, ' - ', number_to_check)
                        with open('palin_prime.txt', 'a') as FILE:
                            FILE.write(f'{datetime.now()} # {ix + PI_SLICER} => {number_to_check}\n')


    print('end')

@njit
def prime_verify(number_to_check, prime_checker, ix, PI_SLICER):
    for i in prange(2,number_to_check):        
        if (number_to_check % i == 0):
            prime_checker += 1

        if(number_to_check % i + int(number_to_check * 0.1) == 0):
            prime_checker += 1

        if(number_to_check % i + int(number_to_check * 0.2) == 0):
            prime_checker += 1

        if(number_to_check % i + int(number_to_check * 0.3) == 0):
            prime_checker += 1

        if(number_to_check % i + int(number_to_check * 0.4) == 0):
            prime_checker += 1

        if(number_to_check % i + int(number_to_check * 0.5) == 0):
            prime_checker += 1

        if(number_to_check % i + int(number_to_check * 0.6) == 0):
            prime_checker += 1

        if(number_to_check % i + int(number_to_check * 0.7) == 0):
            prime_checker += 1

        if(number_to_check % i + int(number_to_check * 0.8) == 0):
            prime_checker += 1

        if(number_to_check % i + int(number_to_check * 0.9) == 0):
            prime_checker += 1

        if(prime_checker > 0):
            # print('BREAK IN => ', ix ,' |' ,PI_SLICER + ix, '| ', number_to_check)
            break

    if(prime_checker==0):
        print('PRIME -> ', ix ,' |' ,PI_SLICER + ix, '| ', number_to_check)
        return number_to_check
    return

if __name__ == '__main__':
    main()
