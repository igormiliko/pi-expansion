import sys
from datetime import datetime
from mpmath import mp
from numba import njit, vectorize, int32, prange, cuda
import numpy as np
mp.dps = 100000


PI = str(mp.pi)
pi_iteration_init = 0
PI_SLICER = 0
PI_STOP = 0
PI = PI.replace('.', '')


threadsperblock = 32


if(len(sys.argv) > 1):
    pi_iteration_init = float(sys.argv[1])
    PI_SLICER = int(int(len(PI) * float(pi_iteration_init)))
    PI = PI[PI_SLICER:]

PI_STOP = int(int(len(PI) * (float(pi_iteration_init + 0.1))))

print(f'Initializing the finder prime palindrome in PI |=>| {pi_iteration_init * 100}%')

def main():
    palin_prime = ''
    for ix, c in enumerate(PI):
        if(ix == PI_STOP + 1):
            break
        prime_checker = 0
        number_to_check = 0

        if (ix == len(PI) - 9):
            print('break')
            break

        number_to_check = int(PI[ix:ix + 9])
        blockspergrid = ((64 * 4) + (threadsperblock - 1)) // threadsperblock
        
        if(len(str(number_to_check)) == 9):
            arr = np.array([number_to_check])
            # buff = prime_verify[blockspergrid, threadsperblock](number_to_check, prime_checker, ix, PI_SLICER)
            d_arr = cuda.to_device(arr)
            
            prime_verify.forall(len(d_arr))(d_arr, prime_checker, ix, PI_SLICER)

            result_array = d_arr.copy_to_host()

            print(result_array)
            if(buff):
                if(str(buff) == str(buff)[::-1]):
                    print('PRIME and PALINDROME => ', ix + PI_SLICER, ' - ', number_to_check)
                    with open('palin_prime.txt', 'a') as FILE:
                        FILE.write(f'{datetime.now()} # {ix + PI_SLICER} => {number_to_check}')


    print('end')

@cuda.jit
def prime_verify(number_to_check, prime_checker, ix, PI_SLICER):
    tx = cuda.threadIdx.x
    # Block id in a 1D grid
    ty = cuda.blockIdx.x
    # Block width, i.e. number of threads per block
    bw = cuda.blockDim.x
    # Compute flattened index inside the array
    pos = tx + ty * bw
    for i in prange(2,number_to_check[pos]):        
        if (number_to_check[pos] % i == 0):
            prime_checker += 1

        if(number_to_check[pos] % i + int(number_to_check[pos] * 0.1) == 0):
            prime_checker += 1

        if(number_to_check[pos] % i + int(number_to_check[pos] * 0.2) == 0):
            prime_checker += 1

        if(number_to_check[pos] % i + int(number_to_check[pos] * 0.3) == 0):
            prime_checker += 1

        if(number_to_check[pos] % i + int(number_to_check[pos] * 0.4) == 0):
            prime_checker += 1

        if(number_to_check[pos] % i + int(number_to_check[pos] * 0.5) == 0):
            prime_checker += 1

        if(number_to_check[pos] % i + int(number_to_check[pos] * 0.6) == 0):
            prime_checker += 1

        if(number_to_check[pos] % i + int(number_to_check[pos] * 0.7) == 0):
            prime_checker += 1

        if(number_to_check[pos] % i + int(number_to_check[pos] * 0.8) == 0):
            prime_checker += 1

        if(number_to_check[pos] % i + int(number_to_check[pos] * 0.9) == 0):
            prime_checker += 1

        if(prime_checker > 0):
            number_to_check[pos] = 0
            # return

    if(prime_checker==0):
        number_to_check[pos] = number_to_check[pos]
        # return

    number_to_check[pos] = 0
    # return

if __name__ == '__main__':
    main()
