import numpy as np
import math  as m

def getAlpha(k, N):
    if k == 0:
        a = N
    else:
        a = N/2
    return a

# dct1D
def dct1(v):
    N = len(v)
    c = np.zeros(N)
    for k in range(0, N):
        ck = 0
        for i in range(0, N):
            ck = ck + m.cos(m.pi * k * (2*(i+1) - 1) / (2*N)) * v[i]
        ck = ck / m.sqrt(getAlpha(k, N))
        c[k] = ck
    return c


# dct2D with 2 x dct1D
def dct2V1(Mat):
    N,M = np.shape(Mat)
    
    C = np.zeros((N, M))

    for h in range(0, N):
        v = Mat[h,:]
        C[h] = dct1(v)
    
    Mat = np.copy(C)
    
    for h in range(0, M):
        v = Mat[:, h]
        C[:,h] = dct1(v)
    return C

# dct2D
def dct2V2(Mat):
    N,M = np.shape(Mat)

    C = np.zeros((N, M))

    for k in range(0, N):
        for l in range(0, M):
            ckl = 0
            for i in range(0, N):
                for j in range(0, M):
                    ckl = ckl + m.cos(m.pi * k * (2*(i+1) - 1) / (2 * N)) * m.cos(m.pi * l * (2*(j+1) - 1) / (2 * M)) * Mat[i, j]
            C[k, l] = ckl / m.sqrt(getAlpha(k,N) * getAlpha(l,M));                    
    return C