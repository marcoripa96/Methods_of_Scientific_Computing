import sys
import os
import humanize
import numpy as np
import random
import matplotlib.pylab as plt
import cv2
from PySide2 import QtCore, QtWidgets, QtGui

# define a Content component which displays the original and processed images
class Content(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # create all widgets components inside the current component
        self.createWidgets()
        # set layout where all widgets are positioned 
        self.setMainLayout()
        
    
    def createWidgets(self):
        self.img1 = QtWidgets.QLabel()
        self.img2 = QtWidgets.QLabel()
        self.lblTitle1 = QtWidgets.QLabel()
        self.lblTitle2 = QtWidgets.QLabel()
        self.w = self.img1.width()
        self.h = self.img1.height()
    
    def setMainLayout(self):
        self.layout = QtWidgets.QHBoxLayout()
        self.vtLayout1 = QtWidgets.QVBoxLayout()
        self.vtLayout2 = QtWidgets.QVBoxLayout()
        self.vtLayout1.addWidget(self.lblTitle1)
        self.vtLayout1.addWidget(self.img1)
        self.vtLayout2.addWidget(self.lblTitle2)
        self.vtLayout2.addWidget(self.img2)
        self.layout.addLayout(self.vtLayout1)
        self.layout.addLayout(self.vtLayout2)
        self.lblTitle1.setAlignment(QtCore.Qt.AlignTop)
        self.lblTitle2.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.layout)

    # set matrix corresponding to the image selected
    def setImg1(self, mat):
        self.mat1 = mat
        self.lblTitle2.setText("")
        self.img2.setPixmap(None)
        self.lblTitle1.setText("<b>Original</b> | <small>{}x{} | {}</small>".format(mat.shape[1], mat.shape[0], \
            humanize.naturalsize(os.path.getsize(self.path1), binary=True)))
    
    # get matrix corresponding to the original image
    def getImg1(self):
        return self.mat1

    # set matrix corresponding to the processed image
    def setImg2(self, mat):
        self.mat2 = mat

    # get matrix corresponding to the processed image
    def getImg2(self):
        return self.mat2
    
    # set path of original image
    def setImgPath1(self, path1):
        self.path1 = path1

    # get path of original image
    def getImgPath1(self):
        return self.path1
    
    # set path of processed image
    def setImgPath2(self, F, d):
        filename, file_extension = os.path.splitext(self.path1)
        folder2 = os.path.join(os.path.dirname(self.path1), "processed")
        # create processed foled if does not exist
        if not os.path.isdir(folder2):
            os.mkdir(folder2)
        filename2 = os.path.basename(filename) + "_F{}_d{}".format(F, d) + file_extension
        path2 = os.path.join(folder2, filename2)
        self.path2 = path2

    # get path of processed image
    def getImgPath2(self):
        return self.path2        

    # show original image
    def showImg1(self):
        self.pixmap = QtGui.QPixmap(self.path1)
        self.pixmap = self.pixmap.scaled(self.w, self.h, QtCore.Qt.KeepAspectRatio) 
        self.img1.setPixmap(self.pixmap)

    # show processed image
    def showImg2(self):
        self.pixmap2 = QtGui.QPixmap(self.path2)
        self.pixmap2 = self.pixmap2.scaled(self.w, self.h, QtCore.Qt.KeepAspectRatio)
        self.img2.setPixmap(self.pixmap2)
        self.lblTitle2.setText("<b>Processed</b> | <small>{}x{} | {}</small>".format(self.mat2.shape[1], self.mat2.shape[0], \
            humanize.naturalsize(os.path.getsize(self.path2), binary=True)))

    # functions to get the execution time of the compression
    def setStartTime(self, startTime):
        self.startTime = startTime

    def getStartTime(self):
        return self.startTime

    def setElapsedTime(self, startTime):
        self.elapsedTime = startTime

    def getElapsedTime(self):
        return self.elapsedTime
    