import sys
import os
import numpy as np
import random
import matplotlib.pylab as plt
import cv2
from PySide2 import QtCore, QtWidgets, QtGui
from components.toolbar import Toolbar
from components.content import Content

# MainWindow is the main component which includes all the sub components
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # create all widgets components inside the current component
        self.createWidgets()    

        # set layout where all widgets are positioned  
        self.setMainLayout()    
        self.layout.setContentsMargins(0,0,0,0)
    def createWidgets(self):
        # create loading animation
        self.status_txt = QtWidgets.QLabel()
        self.status_txt.setAlignment(QtCore.Qt.AlignCenter)
        movie = QtGui.QMovie(os.path.join(os.path.dirname(__file__), "../assets/loading.gif"))
        self.status_txt.setMovie(movie)
        movie.start()

        self.loadingLabel = QtWidgets.QLabel("Loading...")
        self.loadingLabel.setAlignment(QtCore.Qt.AlignHCenter)
        self.loadingLabel.setStyleSheet("color: #E6E6E6; background-color: #2A2826; font-size: 24px")
        self.loadingLabel.setContentsMargins(10,10,10,10)
        
        # set animation duration
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.setComponents)
        self.timer.start(2000)

        # instantiate sub components
        self.content = Content()
        self.toolbar = Toolbar(self.content)
        self.toolbar.setMaximumWidth(600)
    
    def setMainLayout(self):
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.addWidget(self.status_txt)
        self.layout.addWidget(self.loadingLabel)
        self.setLayout(self.layout)

    # remove loading animation and add main widgets
    def setComponents(self):
        self.layout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.content)
        self.status_txt.setMovie(None)
        self.status_txt.setVisible(False)
        self.loadingLabel.setVisible(False)
        self.timer.stop()
        self.layout.setContentsMargins(10,10,10,10)