import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#--------------------Setting-----------------------------------------------------------------

N=40                                         #Number of feature points to select 

#----------------------Functions-------------------------------------------------------------
def resize_image(src, scale_percent):
    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)
    # dsize
    dsize = (width, height)
    # resize image
    output = cv2.resize(src, dsize)
    return output

def mousePoints(event,x,y,flags,params):
    global counter
    global Im_name
    if Im_name==str('Image1'):
        img=img1
    elif Im_name==str('Image2'):
        img=img2
    Points_Image=np.zeros((N,2),np.int)
    if (event == cv2.EVENT_LBUTTONDOWN and counter<=N):
        counter = counter + 1
        print(x,y,135,5)
        #print(Im_name+'_Point', counter, ': (', x, ',' ,y, ')' )
        Points_Image[counter-1]=x,y
        #strxy='*'
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(counter), (x,y), font, 0.25 , (255,0,0), 1)  #BGR=(255,255,0)
        x_vals.append(x)
        y_vals.append(y)
        #cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
        caption=str(Im_name+'_points')
        cv2.imshow(caption, img)
    return 0

def display_click_select_destroy(img, Im_name):
    cv2.imshow(Im_name, img)
    cv2.setMouseCallback(Im_name, mousePoints)
    cv2.waitKey(0)
    cv2.destroyWindow(Im_name)
    return 0
    
#----------------------------------------main-----------------------------------------    

img1 = cv2.imread('Image1.jpg')#, cv2.IMREAD_GRAYSCALE)
#img1=resize_image(img1, 10)
#plt.imsave('Image1.jpg', img1, cmap = 'gray')

img2 = cv2.imread('Image2.jpg')#, cv2.IMREAD_GRAYSCALE)
#img2=resize_image(img2, 10)
#plt.imsave('Image2.jpg', img2, cmap = 'gray') 

x_vals = []
y_vals = []
counter = 0
Im_name=str('Image1')
display_click_select_destroy(img1, Im_name)
data1 = {'X':x_vals,'Y':y_vals, 'R':135, 'A':5}
df_img1 = pd.DataFrame(data1)
print('First Image Done!')

x_vals = []
y_vals = []
counter = 0
Im_name=str('Image2')
display_click_select_destroy(img2, Im_name)
data2 = {'X':x_vals,'Y':y_vals, 'R':135, 'A':5}
df_img2 = pd.DataFrame(data2)
print('Second Image Done!')

cv2.waitKey(1000)      #time in ms
cv2.destroyAllWindows()