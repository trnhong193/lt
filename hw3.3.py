import numpy as np
import cv2 as cv
im = cv.imread('TUM_old.jpg')
cv.imshow('Anh goc', im)
print(im.shape)

#anh_resize
im2 = cv.resize(im, dsize = None, fx = 0.5, fy = 0.5)
cv.imshow('Anh thu nho', im2)
cv.imwrite("TUM_small.png",im2)

#anh_blue
im3 = np.array(im)  #chuyen_anh_ve_arr
im3 = cv.resize(im, (1000,1000))
im3[0:100,:] = [179,112,48]
im3[:,0:150] = [179,112,48]
im3[:,750:1000] = [179,112,48]
im3[900:1000,:] = [179,112,48]
cv.imshow("Anh Blue", im3)
cv.imwrite("TUM_blue.png",im3)
cv.waitKey()