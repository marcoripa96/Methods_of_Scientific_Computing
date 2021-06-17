#!/usr/bin/env python
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from libraryMCS import dct2V1, dct2V2, dct1
from scipy.fft import dct
from verifyDCT import verifyBlockDCT2, verifyRowDCT1
from utils import generateRandomMatrix, printSignature


if __name__ == '__main__':
    printSignature()
    while True:
        flag = input("Select a function to run by typing the corresponding number: \n 1- verifyBlockDCT2 \
            \n 2- verifyRowDCT1 \n 3- check dct2 implementation \n 4- compare dcts \n 0- EXIT \n")
        try:
            flag = int(flag)
        except:
            print("Invalid input")
            sys.exit()
        if flag < 0 or flag > 4:
            print("Invalid input")
            sys.exit()

        # if EXIT is selected
        if flag == 0:
            break
        # if verifyBlockDCT2 is selected
        elif flag == 1:
            option = input("Choose which library to use to verify: \n 0- SciPy \
            \n 1- libraryMCS \n")
            try:
                option = int(option)
            except:
                print("Invalid input")
                sys.exit()
            if option == 0:
                print("VERIFY BLOCK DCT2 SciPy \n")
            elif option == 1:
                print("VERIFY BLOCK DCT2 libraryMCS \n")
            else:
                print("Invalid input")
                sys.exit()
            verifyBlockDCT2(option)
        
        # if verifyRowDCT1 is selected
        elif flag == 2:
            option = input("Choose which library to use to verify: \n 0- SciPy \
            \n 1- libraryMCS \n")
            try:
                option = int(option)
            except:
                print("Invalid input")
                sys.exit()
            if option == 0:
                print("VERIFY ROW DCT1 SciPy \n")
            elif option == 1:
                print("VERIFY ROW DCT1 libraryMCS \n")
            else:
                print("Invalid input")
                sys.exit()
            verifyRowDCT1(option)
        
        # if check dct2 implementation is selected
        elif flag == 3:
            print("CHECK DCT2 IMPLEMENTATION")
            M = np.int_(np.random.rand(5, 5) * 100)
            A = dct(dct(M, axis=1, norm='ortho'),
                    axis=0, norm='ortho')
            D = dct2V1(M)
            E = dct2V2(M)
            print('DCT2 SciPy \n')
            print(A)
            print('\n DCT2V1 libraryMCS \n')
            print(D)
            print('\n DCT2V2 libraryMCS \n')
            print(E)
        
        # if compare dcts is selected
        else:
            print('COMPARE DCTs \n')

            df = pd.DataFrame(columns=['DCT2_SCIPY', 'DCT2V1', 'DCT2V2', 'DIM'])

            for n in range(10, 210, 10):
                K = generateRandomMatrix(n, n)
                print('DIMENSION: {} x {}'.format(n, n))
                start = timer()
                A = dct(dct(K, axis=1, norm='ortho'),
                        axis=0, norm='ortho')
                end = timer()
                A_time = end - start
                print('DCT2 SCIPY: ', end - start)
                start = timer()
                A = dct2V1(K)
                end = timer()
                B_time = end - start
                print('DCT2V1: ', end - start)

                if (n > 100):
                    print('DCT2V2: NaN')
                    C_time = float('NaN')
                else:
                    start = timer()
                    A = dct2V2(K)
                    end = timer()
                    C_time = end - start
                    print('DCT2V2: ', end - start)
                df = df.append({'DCT2_SCIPY': A_time, 'DCT2V1': B_time,
                                'DCT2V2': C_time, 'DIM': n}, ignore_index=True)
            df.to_csv("report.csv", index=False)

            ax = plt.gca()
            df.plot(logy=True, x='DIM', y='DCT2_SCIPY', ax=ax)
            df.plot(logy=True, x='DIM', y='DCT2V1', ax=ax)
            df.plot(logy=True, x='DIM', y='DCT2V2', ax=ax)
            plt.show()
        
        while True:
            flag = input("Continue?: yes[y] or no[n] \n")
            if flag == "n":
                sys.exit()
            elif flag == "y":
                break
            else:
                print("Invalid input")