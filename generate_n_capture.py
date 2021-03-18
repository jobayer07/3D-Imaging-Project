"""
Created on Thu Mar 18 18:12:05 2021
@author: Mohammad Jobayer Hossain
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import time
from threading import Event
import cv2
from pypylon import pylon

#--------Settings------------------------------------
F=5                         #Number of spatial frequencies  
patternAxis = 'vertical' #v=vertical, h=horizontal
exposure_time=250000       #exposure time in us

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

def projector (d, high_level):
    Nx=1366#int(668)
    Ny=int(1366)
    im=np.zeros([Nx,Ny])
    #d=Number of pixels together
    # low_level: violet:10, blue:15, green:55, yellow: 75, Red: 85
    a=0
    b=high_level
    for i in range(0, Ny):
        im[:, 2*d*i : 2*d*i+d]=a
        im[:, 2*d*i+d : 2*d*i+d+d]=b
    if (patternAxis == 'vertical'):
        im_out=im
    elif (patternAxis == 'horizontal'):
        im_out=matrix_rotation(im, 1)
    else:
        print('Input the pattern axis')
    return im_out

def capture_image():
    try:
        camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice()) # Create an instant camera object with the camera device found first.
        camera.Open()
        print("Using device ", camera.GetDeviceInfo().GetModelName())  # Print the model name of the camera.
    
        camera.MaxNumBuffer = 20 # The parameter MaxNumBuffer can be used to control the count of buffers. allocated for grabbing. The default value of this parameter is 10.
        countOfImagesToGrab = 1  # Number of images to be grabbed.
        camera.StartGrabbingMax(countOfImagesToGrab)
        
        converter=pylon.ImageFormatConverter()
    
        #converting to opencv bgr format
        converter.OutputPixelFormat=pylon.PixelType_BGR8packed#pylon.PixelType_BGR8packed
        converter.OutputBitAlignment=pylon.OutputBitAlignment_MsbAligned 
    
        # Camera.StopGrabbing() is called automatically by the RetrieveResult() method
        # when c_countOfImagesToGrab images have been retrieved.
        while camera.IsGrabbing():
            # Wait for an image and then retrieve it. A timeout of 5000 ms is used.
            grabResult = camera.RetrieveResult(exposure_time, pylon.TimeoutHandling_ThrowException)
    
            # Image grabbed successfully?
            if grabResult.GrabSucceeded():
                # Access the image data.
                print("SizeX: ", grabResult.Width)
                print("SizeY: ", grabResult.Height)
                #img = grabResult.Array
                image=converter.Convert(grabResult)
                img=image.GetArray()
                #plt.imshow(img)
                #plt.axis('off')
            else:
                print("Error: ", grabResult.ErrorCode, grabResult.ErrorDescription)
            grabResult.Release()
        camera.Close()
    except:
        camera.Close()
        print("An exception occurred.") # Error handling.
    return img


def project_n_capture(color, high_level):
    # violet:10, blue:15, green:55, yellow: 75, Red: 85       
    for i in range (1, F+1):
        d=i*5
        im=projector(d, high_level)
        plt.imshow(im, cmap = 'nipy_spectral', vmin=0, vmax=100) #Greys, Greens, Blues, Oranges, Reds, binary
        plt.axis('off')
        plt.title('Period: '+str(2*d)+'pixels')
        plt.imsave('projector_image.jpg', im, cmap = 'nipy_spectral', vmin=0, vmax=100)
        plt.pause(1)    #pause for 2 seconds
        #capture & save
        image=capture_image()
        cv2.imwrite('camera_'+ str(color) +'_' +str(2*d)+'pixel_' + str(patternAxis) + '.bmp', image)  #bmp=bit map image
        print('Image Capture Done!   Color:'+str(color)+'   Period: '+str(2*d)+'pixel')

#---------------------------------Main Code---------
# violet:10, blue:15, green:55, yellow: 75, Red: 85 
color='Red'
project_n_capture(color, 85)
color='Green'
'''
project_n_capture(color, 55)
color='Blue'
project_n_capture(color, 15)
color='Yellow'
project_n_capture(color, 75)
color='Violet'
project_n_capture(color, 10)
'''