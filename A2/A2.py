#Project    : Algorithms - Activity 2
#Developer: : Dago Quevedo
#Date       : Feb 20

import time
import random

#Iterative binary search
def it_binary_search(vector,s):
    left  = 0
    right = len(vector)-1

    while left <= right:
        half = (left + right)//2

        if vector[half] == s:
            return half

        elif vector[half] > s:
            right = half - 1
        else:
            left = half + 1

    return -1

#Recursive binary search
def re_binary_search(vector, s, left, right):
    if left > right:
        return -1
    half = (left + right)//2
    if vector[half] == s:
        return half
    elif vector[half] > s:
        return re_binary_search(vector, s, left, half-1)
    else:
        return re_binary_search(vector, s, half+1,right)

#Iterative integer exponentiation
def it_int_exp(a,b):
    r = 1
    while 1:
        if b % 2 == 1:
            r *= a
        b //= 2
        if b == 0:
            break
        a *= a

    return r

#Recursive integer exponentiation
def re_int_exp(a,b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        r = re_int_exp(a, b / 2)
        return r * r
    else:
        return a * re_int_exp(a, b - 1)
        
        
#Recursive tower of Hanoi
log_re_hanoi = []
def re_hanoi(n, A, B, C):
    if n == 1:
        log_re_hanoi.append('Move %d from %s to %s' % (1,A,C))
        return
    re_hanoi(n-1, A, B, C)
    log_re_hanoi.append('Move %d from %s to %s' % (n,A,C))
    re_hanoi(n-1, B, C, A)

#Iterative tower of Hanoi
def it_hanoi(n):
    log_it_hanoi = []
    
    def move(X,Y,label_X,label_Y):
        if len(X) > 0:
            Y.append(X.pop())
            
            if len(Y) > 0:
                log_it_hanoi.append('Move %d from %s to %s' % (Y[-1],label_X,label_Y))
            
    A = list(range(1, n + 1))
    B = []
    C = []

    for i in range(1,2**n):
        if i % 3 == 1:
            move(A,C,'A','C')
        if i % 3 == 2:
            move(A,B,'A','B')
        if i % 3 == 0:
            move(B,C,'B','C')
            
    return log_it_hanoi


if __name__== '__main__':
    N_IE = list(range(1,25))
    N_BS = list(range(1,25))
    N_TH = list(range(1,25))
    K = list(range(1,5))
    a = 1000
    
    for k in K:
        for n in N_IE:
            b = 2**n

            start_time = time.process_time()
            it_int_exp(a,b)
            print('%d, %s, %s, %d, %d, %d, %2.8f' % (k,'ie','it',a,b,n,time.process_time() - start_time))

            start_time = time.process_time()
            re_int_exp(a,b)
            print('%d, %s, %s, %d, %d, %d, %2.8f' % (k,'ie','re',a,b,n,time.process_time() - start_time))

        for n in N_BS:
            vector = list(range(1,2**n));
            element = random.sample(vector,1)[0]
            
            start_time = time.process_time()
            it_binary_search(vector,element)
            print('%d, %s, %s, %d, %2.8f' % (k,'bs','it',len(vector),time.process_time() - start_time))
            
            start_time = time.process_time()
            re_binary_search(vector,element,0,len(vector)-1)
            print('%d, %s, %s, %d, %2.8f' % (k,'bs','re',len(vector),time.process_time() - start_time))
            
        for n in N_TH:
            start_time = time.process_time()
            it_hanoi(n)
            print('%d, %s, %s, %d, %2.8f' % (k,'th','it',n,time.process_time() - start_time))
            
            start_time = time.process_time()
            re_hanoi(n,'A','B','C')
            print('%d, %s, %s, %d, %2.8f' % (k,'th','re',n,time.process_time() - start_time))
