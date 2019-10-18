
# coding: utf-8

# In[2]:


# import the necessary packages
import numpy as np
import argparse
import cv2
from imutils.object_detection import non_max_suppression
import numpy as np
import pytesseract
import argparse
import cv2
# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image file")
# args = vars(ap.parse_args())
 
# load the image from disk
def kmeans(input_img, k, i_val):
    hist = cv2.calcHist([input_img],[0],None,[256],[0,256])
    img = input_img.ravel()
    img = np.reshape(img, (-1, 1))
    img = img.astype(np.float32)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness,labels,centers = cv2.kmeans(img,k,None,criteria,10,flags)
    centers = np.sort(centers, axis=0)

    return centers[i_val].astype(int), centers, hist

img = cv2.imread('/home/nextjob/Create_Online.jpg')
_, thresh = cv2.threshold(img, kmeans(input_img=img, k=8, i_val=6)[0], 255, cv2.THRESH_BINARY)
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 3)
cv2.imwrite('text.png',thresh)
# cv2.imshow('threshold',thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
image = cv2.imread("/home/nextjob/text.png")


# In[3]:


# convert the image to grayscale and flip the foreground
# and background to ensure foreground is now "white" and
# the background is "black"
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)
 
# threshold the image, setting all foreground pixels to
# 255 and all background pixels to 0
thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


# In[4]:



# grab the (x, y) coordinates of all pixel values that
# are greater than zero, then use these coordinates to
# compute a rotated bounding box that contains all
# coordinates
coords = np.column_stack(np.where(thresh > 0))
angle = cv2.minAreaRect(coords)[-1]
 
# the `cv2.minAreaRect` function returns values in the
# range [-90, 0); as the rectangle rotates clockwise the
# returned angle trends to 0 -- in this special case we
# need to add 90 degrees to the angle
if angle < -50:
	angle = -(90 + angle)
 
# otherwise, just take the inverse of the angle to make
# it positive
else:
	angle = -angle


# In[5]:


# rotate the image to deskew it
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h),
	flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)


# In[6]:


# draw the correction angle on the image so we can validate it
cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle),
	(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
cv2.imwrite('text2.png',rotated) 
# show the output image
print("[INFO] angle: {:.3f}".format(angle))
cv2.imshow("Input", image)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[4]:


import numpy as np
import cv2
import math
from scipy import ndimage

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)

angles = []

for x1, y1, x2, y2 in lines[0]:
    cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    angles.append(angle)

median_angle = np.median(angles)
img_rotated = ndimage.rotate(image, median_angle)

print("Angle is {}".format(median_angle))
cv2.imwrite('rotated.jpg', img_rotated)
cv2.imshow("Rotated", img_rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


image = cv2.imread("2.jpg")


# In[7]:


text=pytesseract.image_to_string("rotated.jpg",lang='eng')
text


# In[1]:


'Brand Name Inc.\n\nA Message From Your Company\n\nFull Name\nMain Title\n\n122 Main Street
\nCity, STATE, a013\n\n \n\ntel. (206) 555
.\nyou@emaiy\n\n1689\nladdress.com'


# In[ ]:



###image resize
from PIL import Image
im = Image.open("rotated.jpg")
nx, ny = im.size
im2 = im.resize((int(nx*1.5), int(ny*1.5)), Image.BICUBIC)
im2.save("2.jpg")

