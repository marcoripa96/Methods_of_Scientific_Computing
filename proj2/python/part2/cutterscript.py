#bridge.bmp
#filename = #r"C:\Users\ricca\workspace\git\mcs_zanfrani\proj2\python\part2\#images\bridge.bmp"
#imageMatrix = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

import utils
import cv2
import traceback
import numpy as np
import pandas as pd
import sys


K =  np.round(np.random.uniform(0, 255, size=(10, 10)))
print(K)
print("\n"*5)

G = utils.matrixCutter(K, 7)
print(K)