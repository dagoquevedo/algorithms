import random
import time

def inv_count_naive(A):
    n = len(A)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (A[i] > A[j]):
                count += 1

    return count

def inv_count_sortm(A):
    if len(A) == 1:
        return A, 0
        
    C = []
    M = int(len(A)/2)
    L, nL = inv_count_sortm(A[:M])
    R, nR = inv_count_sortm(A[M:])
    N = nL + nR

    while (len(L) > 0) or (len(R) > 0):
        if (len(L) > 0) and (len(R) > 0):
            if L[0] > R[0]:
                C.append(R[0])
                N+=len(L)
                R.pop(0)
            else:
                C.append(L[0])
                L.pop(0)
        elif len(R) > 0:
            C.extend(R)
            R = []
        else:
            C.extend(L)
            L = []
            
    return C, N


if __name__== '__main__':
    L = list(range(1,int(1E+8)))
    N = list(range(1,16))
    K = list(range(1,11))
    
    for k in K:
        for n in N:
            b = 2**n
            
            A = random.sample(L,b)
            
            start_time = time.process_time()
            inv_count_naive(A)
            
            print('%d, %s, %d, %d, %2.8f' % (k,'naive',b,n,time.process_time() - start_time))
            
            start_time = time.process_time()
            inv_count_sortm(A)
            
            print('%d, %s, %d, %d, %2.8f' % (k,'merge',b,n,time.process_time() - start_time))

