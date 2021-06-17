import numpy as np
from scipy.fft import dct, idct

# helper function which cuts the frquencies
def cutFrequencies(mat, d):
    nrow,_ = mat.shape
    for i in range(0,nrow):
        mat[i, d:] = 0
        d = d - 1 if d > 1 else 0

# function to compress an image
def compressImage(mat, F, d, progress_callback = None):

    if d < 0 or d > 2*F - 2:
        raise ValueError("d has to be in [0:2*F-2] = [0:{}]".format(2*F - 2))
    if F < 1 or F > min(mat.shape) :
        raise ValueError("F has to be in [1:{}]".format(min(mat.shape)))

    progress = 0
    blockinitY = 0
    blockendY = F

    # max row and column size of the new matrix
    maxX = mat.shape[1] - mat.shape[1] % F
    maxY = mat.shape[0] - mat.shape[0] % F

    newMatrix = np.empty((maxY, maxX))

    # iterate over matrix rows
    while blockendY <= mat.shape[0]:
        # update progress
        if progress_callback is not None:
            progress += 1
            progress_callback.emit(progress)
        
        blockinitX = 0
        blockendX = F

        # iterate over matrix columns
        while blockendX <= mat.shape[1]:

            # select block
            currentBlock = mat[blockinitY:blockendY, blockinitX:blockendX]

            # compute dct2 on selected block
            newBlock = dct( dct( currentBlock, axis=1, norm='ortho' ), axis=0, norm='ortho' )
            # cut frquencies
            cutFrequencies(newBlock, d)
            # compute idct2
            newBlock = idct( idct( newBlock, axis=1, norm='ortho' ), axis=0, norm='ortho' )
            
            # check if each coefficient is included between 0 and 255
            newBlock[newBlock < 0] = 0
            newBlock[newBlock > 255] = 255

            # set block in new matrix
            newMatrix[blockinitY:blockendY, blockinitX:blockendX] = newBlock.round()

            # go to next block on the row
            blockinitX += F
            blockendX += F
        
        # go to next row matrix 
        blockinitY += F
        blockendY += F
    return newMatrix