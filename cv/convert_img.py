import numpy as np
import cv2
import imageio
import matplotlib.pyplot as plt
from PIL import Image
my=Image.open(r'out_video_vc0_01.raw')
#print(my)
#my_raw=cv2.imread('out_video_vc0_130.raw')
#type=my_raw.dtype
#print(type)
#cv2.imshow('raw',my_raw)
#cv2.waitKey()
#cv2.destroyAllWindows()
rawfile=np.fromfile('out_video_vc0_130.raw',dtype='uint8')
print(rawfile.shape)
rawfile=rawfile.reshape(640,618,3)
rawfile.shape=(3,640,618)
print(rawfile)


'''
b=rawfile.astype(np.uint8)
print(b)
#imageio.imwrite("1.jpg",b)
#img=plt.imread('1.jpg')
#print(img.shape)
#plt.imshow(b)
plt.imshow(b)
plt.show()
'''