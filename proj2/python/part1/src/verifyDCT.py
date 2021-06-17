import numpy as np
from scipy.fft import dct
from libraryMCS import dct2V1, dct1

test = np.array([[231, 32, 233, 161, 24, 71, 140, 245],
                [247, 40, 248, 245, 124, 204, 36, 107],
                [234, 202, 245, 167, 9, 217, 239, 173],
                [193, 190, 100, 167, 43, 180, 8, 70],
                [11, 24, 210, 177, 81, 243, 8, 112],
                [97, 195, 203, 47, 125, 114, 165, 181],
                [193, 70, 174, 167, 41, 30, 127, 245],
                [87, 149, 57, 192, 65, 129, 178, 228]])

def verifyBlockDCT2(flag = 0, norm = 'ortho'):
    if flag == 0: # scipy dct2 
        D = dct( dct( test, axis=1, norm=norm ), axis=0, norm=norm )
    else: # dct2 ours dct
        D = dct2V1(test)
    print(D)

def verifyRowDCT1(flag = 0, norm = 'ortho'):
    firstRow = test[0]
    print(firstRow)
    if flag == 0: # scipy 
        D = dct(firstRow, axis=0, norm=norm )
    else:
        D = dct1(firstRow)
    print(D)
    

