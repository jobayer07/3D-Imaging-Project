"""
Created on Thu Mar 18 18:12:05 2021
@author: Mohammad Jobayer Hossain
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#--------Settings-------------------
f=10
patternAxis = 'h' #v=vertical, h=horizontal
signalType = 2  # square wave illumination pattern

#------------------------------------Functions----------
def matrix_rotation(image_in, theta):
    #clockwise rotation: theta=-1,  anti-clockwise rotation: theta=+1
    n,m=image_in.shape
    for i in range(m):
        b=image_in[:,i]
        b = b[::theta]
        image_in[:,i]=b
    image_out=image_in.transpose()
    return image_out

#-------------------------------------

Nx=100
Ny=100
im=np.zeros([Nx,Ny])

im[:, :]=np.linspace(0, 1, Ny, endpoint=False)

if (patternAxis == 'h'):
    d=matrix_rotation(im, 1)
    
x=im[:, :]
im=signal.square(2 * np.pi* f * x, duty=0.5)
'''
sos = signal.butter(1,f, 'lp', fs=200, output='sos')
y = signal.sosfilt(sos, im)
'''
plt.imshow(im, cmap = 'Greens') #Greys, Greens, Blues, Oranges, Reds
plt.axis('off')
plt.title('a')
plt.title('Spatial frequency= '+str(f))

#plt.ylim(-2, 2)
#plt.figure()
#plt.plot(x,y)