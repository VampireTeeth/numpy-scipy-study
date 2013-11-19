'''
Created on Nov 19, 2013

@author: steven
'''


import numpy as np


def list_times(l, v):
    for i, val in enumerate(l):
        l[i] = val*v
    return l


arr = np.arange(1e7)
larr = arr.tolist()

if __name__ == '__main__':
    
    list_times(larr, 1.1)
    
    arr * 1.1