# Given a sequence of n values x1, x2, ..., xn and a window size k>0, the k-th moving
# average of the given sequence is defined as follows:
# The moving average sequence has n-k+1 elements as shown below.
# The moving averages with k=4 of a ten-value sequence (n=10) is shown below
# i 1 2 3 4 5 6 7 8 9 10
# ===== == == == == == == == == == ==
# Input 10 20 30 40 50 60 70 80 90 100
# y1 25 = (10+20+30+40)/4
# y2 35 = (20+30+40+50)/4
# y3 45 = (30+40+50+60)/4
# y4 55 = (40+50+60+70)/4
# y5 65 = (50+60+70+80)/4
# y6 75 = (60+70+80+90)/4
# y7 85 = (70+80+90+100)/4

# Thus, the moving average sequence has n-k+1=10-4+1=7 values.

# Problem Statement
# Write a function to find moving average in an array over a window:
# Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3.

import numpy as np


def FindMovingAverage(numberSeq, window):
    # create a sequence of 1/window of window size: say weights
    weights = np.repeat(1.0, window)/window
    # use convolution of two sequences(weights and numberSeq)
    # use mode as valid to specify the overlap is always complete
    # addition of second array(weights) reversed convoluted onto first array(numberSeq)
    # and multiplied at each position of overlapping sequence of arrays

    # first element
    # [0.33,0.33,0.33]
    # [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
    # (3*0.33 + 5*0.33 +7*0.33)

    # second element
    #    [0.33,0.33,0.33]
    # [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
    # (5*0.33 + 7*0.33 + 2*0.33)

    # and so on so forth
    movingAvg = np.convolve(numberSeq, weights, 'valid')
    return movingAvg


sequence = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
window = 3
calcMovingAvg = FindMovingAverage(sequence, window)
print(calcMovingAvg)
