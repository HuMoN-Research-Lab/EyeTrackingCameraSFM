import os
import numpy as np

image_dir = '/Users/luyifan/Desktop/motionCap/SFM/images/'
MRT = 0.7

#camera calibration matrix K
K = np.array([[1.06334775e+03,0.00000000e+00,4.83541243e+02],
 [0.00000000e+00,1.06334775e+03,1.06554082e+03],
 [0.00000000e+00,0.00000000e+00,1.00000000e+00]])


#chose range of points that will be deleted
x = 0.5
y = 1