import sys
import os
import numpy as np
import random
import matplotlib.pylab as plt
import cv2
from PySide2 import QtCore, QtWidgets, QtGui
from shared.imageCompressor import compressImage
import shared.worker as worker
from timeit import default_timer as timer

class Toolbar(QtWidgets.QWidget):

    def __init__(self, content):
        super().__init__()
        # get reference to content component
        self.content = content
        # instantiate a thread pool to use workers
        self.threadpool = QtCore.QThreadPool()

        # create all widgets components inside the current component
        self.createWidgets()
        # set layout where all widgets are positioned        
        self.setMainLayout()
        
        # connect buttons to their function
        self.btnImage.clicked.connect(self.openFileExplorer)
        self.btnConfirm.clicked.connect(self.startWorker)

    
    def createWidgets(self):
        self.btnImage = QtWidgets.QPushButton("Select image")
        self.btnConfirm = QtWidgets.QPushButton("Confirm")
        self.filenameLbl = QtWidgets.QLabel("filename")
        self.errorBox = QtWidgets.QMessageBox()
        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setVisible(False)
        self.elapsedTimeLbl = QtWidgets.QLabel("")
        self.elapsedTimeLbl.setVisible(False)
        self.blockSizeEdit = QtWidgets.QLineEdit()
        self.blockSizeEdit.setValidator(QtGui.QIntValidator())
        self.freqTreshold = QtWidgets.QLineEdit()
        self.freqTreshold.setValidator(QtGui.QIntValidator())
    
    def setMainLayout(self):
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.formLayout.addRow("Block size (F):", self.blockSizeEdit)
        self.formLayout.addRow("Frequency threshold (d):", self.freqTreshold)
        self.formLayout.addRow(self.filenameLbl, self.btnImage)
        self.formLayout.addRow(self.btnConfirm)
        self.formLayout.addRow(self.progressBar)
        self.formLayout.addRow(self.elapsedTimeLbl)
        self.mainLayout.addLayout(self.formLayout)
        self.setLayout(self.mainLayout)
    
    # function called when worker emits a done signal
    def onDone(self, blockSize, freqTreshold):
        self.content.setElapsedTime(timer() - self.content.getStartTime())
        self.progressBar.setVisible(False)
        if self.success:
            self.elapsedTimeLbl.setText("Processed in {:.3f}s" \
                .format(self.content.getElapsedTime()))
            self.elapsedTimeLbl.setVisible(True)
        else:
            self.elapsedTimeLbl.setVisible(False)
        
        # set path of processed image in content
        self.content.setImgPath2(blockSize, freqTreshold)
        # save image on disk
        if not cv2.imwrite(self.content.getImgPath2(), self.content.getImg2()):
            raise Exception("Could not write image")
        # if image has been saved show it
        self.content.showImg2()
        
        self.btnImage.setEnabled(True)
        self.btnConfirm.setEnabled(True)
        return

    # function called when worker emits a progress signal
    def onProgress(self, progress):
        # update progress bar value
        self.progressBar.setValue(progress)
        return

    # function called when worker emits a error signal
    def onError(self, msg):
        self.success = False
        # show message box with error
        self.errorBox.setText("<h2>" + msg + "</h2>")
        self.errorBox.exec()
        return

    # function called inside a worker which execute the compression algorithm
    def computeImage(self, blockSize, freqTreshold, mat, progress_callback):
        self.content.setImg2(compressImage(mat, blockSize, freqTreshold, progress_callback))
    
    # function called when the user clicks on the Confirm button
    def startWorker(self):
        self.success = True
        # check if all form fields and an image are set and valid
        try:
            blockSize = int(self.blockSizeEdit.text())
            freqTreshold = int(self.freqTreshold.text())
        except Exception as err:
            self.success = False
            self.errorBox.setText("Invalid input: {}".format(err))
            self.errorBox.exec()
            return
        try:
            mat = self.content.getImg1()
        except Exception as err:
            self.success = False
            self.errorBox.setText("Please select an image")
            self.errorBox.exec()
            return

        if freqTreshold < 0 or freqTreshold > 2*blockSize - 2:
            self.success = False
            self.errorBox.setText("d has to be in [0:2*F-2] = [0:{}]".format(2*blockSize - 2))
            self.errorBox.exec()
            return

        if blockSize < 1 or blockSize > min(mat.shape) : 
            self.success = False
            self.errorBox.setText("F has to be in [1:{}]".format(min(self.content.mat1.shape)))
            self.errorBox.exec()
            return

        # disabled buttons to prevent user from messing with the UI
        self.btnImage.setEnabled(False)
        self.btnConfirm.setEnabled(False)
        
        self.elapsedTimeLbl.setVisible(False)
        self.elapsedTimeLbl.setText("")
        # show progress bar and set its maximum progress size
        self.progressBar.setVisible(True)
        self.progressBar.setMaximum((mat.shape[0] - mat.shape[0] % blockSize) / blockSize)

        # instantiate a worker which executes the compression
        work = worker.Worker(self.computeImage, blockSize, freqTreshold, mat)

        # connect worker signals to their corrisponding function
        work.signals.progress.connect(self.onProgress)
        work.signals.finished.connect(self.onDone)
        work.signals.error.connect(self.onError)

        self.content.setStartTime(timer())
        # execute run function of worker
        self.threadpool.start(work)

    # function called when user clicks the Select Image button
    def openFileExplorer(self):
        # open file explorer to select and image from the file system. Filter only bmp images. Default location is "part2/images"
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open Image", "part2/images", "Image Files (*.bmp)")

        # if a file is selected
        if fileName[0] != '':
            self.content.setImgPath1(fileName[0])
            self.filenameLbl.setText(os.path.basename(os.path.normpath(fileName[0])))
            
            # read image in grayscale as matrix
            imageMatrix = cv2.imread(fileName[0], cv2.IMREAD_GRAYSCALE)
            # set and show image in Content component
            self.content.setImg1(imageMatrix)
            self.content.showImg1()