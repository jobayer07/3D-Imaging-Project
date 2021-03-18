"""
Created on Thu Mar 18 18:12:05 2021
@author: Mohammad Jobayer Hossain
"""

import numpy as np
import cv2
from pypylon import pylon
import matplotlib.pyplot as plt


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
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        # Image grabbed successfully?
        if grabResult.GrabSucceeded():
            # Access the image data.
            print("SizeX: ", grabResult.Width)
            print("SizeY: ", grabResult.Height)
            #img = grabResult.Array
            image=converter.Convert(grabResult)
            img=image.GetArray()
            plt.imshow(img)
            plt.axis('off')
            
            cv2.imwrite('opencv'+str(1)+'.bmp', img)  #save image
            plt.imshow(img)
            plt.axis('off')
            
        else:
            print("Error: ", grabResult.ErrorCode, grabResult.ErrorDescription)
        grabResult.Release()
    camera.Close()
    print('Job Done!')

except:
    camera.Close()
    print("An exception occurred.") # Error handling.
