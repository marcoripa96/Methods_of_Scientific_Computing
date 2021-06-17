#bridge.bmp
#filename = #r"C:\Users\ricca\workspace\git\mcs_zanfrani\proj2\python\part2\#images\bridge.bmp"
#imageMatrix = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

import utils
import cv2
import traceback
import numpy as np
import pandas as pd
import sys

filename = r"C:\Users\ricca\workspace\git\mcs_zanfrani\proj2\python\part2\images\bridge.bmp"
imageMatrix = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print(imageMatrix.shape)

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
n3 = int(sys.argv[3])
n4 = int(sys.argv[4])

print(imageMatrix[n1:n2,n3:n4])

newmat = utils.compressImage(imageMatrix, 10, 7)

print(newmat[n1:n2,n3:n4])

print(np.allclose (imageMatrix[n1:n2,n3:n4], newmat[n1:n2,n3:n4]))

print(np.max(imageMatrix[n1:n2,n3:n4] - newmat[n1:n2,n3:n4]))

