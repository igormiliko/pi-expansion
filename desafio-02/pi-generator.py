from numba import cuda

def main():
    print(pi_gen.forall(100000)(100000))
    
@cuda.jit
def pi_gen(iterations):
    k = 1
    pi = 0
    for i in range(iterations):
        if(i % 2 == 0):
            pi += 4/k
        else:
            pi -= 4/k
if __name__ == '__main__':
    main()