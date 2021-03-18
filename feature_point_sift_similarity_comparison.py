"""
Created on Thu Mar 18 18:12:05 2021
@author: Mohammad Jobayer Hossain
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_left = cv2.imread("park1.jpg", cv2.IMREAD_GRAYSCALE)
img_right = cv2.imread("park2.jpg", cv2.IMREAD_GRAYSCALE)

sift = cv2.xfeatures2d.SIFT_create()

kp_left, desc_left = sift.detectAndCompute(img_left, None)
kp_right, desc_right = sift.detectAndCompute(img_right, None)

sift_points_left = cv2.drawKeypoints(img_left, kp_left, None)
sift_points_right = cv2.drawKeypoints(img_right, kp_right, None)

plt.figure(1)
plt.imshow(sift_points_left)
plt.axis('off')
plt.title('left')

plt.figure(2)
plt.imshow(sift_points_right)
plt.axis('off')
plt.title('right')


index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(desc_left, desc_right, k=2)
result=cv2.drawMatchesKnn(img_left, kp_left, img_right, kp_right, matches, None)

plt.figure(3)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()