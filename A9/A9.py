import binomialheap
import binary_heap
import random
import time

if __name__== '__main__':
    L = list(range(1,int(1E+8)))
    N = list(range(1,20))
    K = list(range(1,11))

    bryheap = binary_heap.MinHeap()
    binheap = binomialheap.BinomialHeap()
    

    for k in K:
        for n in N:
            b = 2**n
            
            A = random.sample(L,b)
            
            start_time = time.process_time()
            
            bryheap.add_element(A)
            
            print('%d, %s, %d, %d, %2.8f' % (k,'binary',b,n,time.process_time() - start_time))
            
            start_time = time.process_time()
            
            for q in A:
                binheap.insert(q)

            print('%d, %s, %d, %d, %2.8f' % (k,'binomial',b,n,time.process_time() - start_time))
            
