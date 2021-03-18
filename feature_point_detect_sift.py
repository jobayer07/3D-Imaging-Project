"""
Created on Thu Mar 18 18:12:05 2021
@author: Mohammad Jobayer Hossain
"""

import cv2
#import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("fr_467.jpg", cv2.IMREAD_GRAYSCALE)

#sift = cv2.xfeatures2d.SIFT_create()
#surf = cv2.xfeatures2d.SURF_create()
orb = cv2.ORB_create(nfeatures=15000)

#keypoints_sift, descriptors_sift = sift.detectAndCompute(img, None)
#keypoints_surf, descriptors_surf = surf.detectAndCompute(img, None)
keypoints_orb, descriptors_orb = orb.detectAndCompute(img, None)


#img_sift_points = cv2.drawKeypoints(img, keypoints_sift, None)
#img_surf_points = cv2.drawKeypoints(img, keypoints_surf, None)
img_orb_points = cv2.drawKeypoints(img, keypoints_orb, 100)

plt.figure(1)
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.title('original image')

plt.figure(2)
plt.imshow(img_orb_points)
plt.axis('off')
plt.title('sift')
'''
plt.figure(3)
plt.imshow(img_surf_points)
plt.axis('off')
plt.title('surf')

plt.figure(4)
plt.imshow(img_orb_points)
plt.axis('off')
plt.title('orb')
'''
'''
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''