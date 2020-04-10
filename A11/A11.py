#Project    : Algorithms - Activity 11 - Hash fuction & colission
#Developer: : Dago Quevedo
#Date       : Apr 20

import math
import random 

def hash_func(key,hash_table,type):
    #mod method
    if type == 1:
        return key % len(hash_table)
    #product method
    if type == 2:
        return math.floor(len(hash_table) * (key * 0.86 % 1))

def insert(hash_table, key, value, type):
    hash_key = hash_func(key,hash_table,type)
    key_exists = False
    position = hash_table[hash_key]
    colission = len(position) > 0
        
    for i, kv in enumerate(position):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        position[i] = ((key, value))
    else:
        position.append((key, value))
        
    return colission, hash_key
        

M = 10000
L = list(range(1,int(1E+6)))

for k in range(5):
    for type in range(1,3):
        hash_table = [[] for _ in range(M)]
        for i in random.sample(L,M):
            colission, key = insert(hash_table, i, 's',type)
            print('%d;%d;%d;%d' % (k,type,int(colission), key))

