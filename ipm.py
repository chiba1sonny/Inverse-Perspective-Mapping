import cv2
import matplotlib.pyplot as plt
import numpy as np
from get_coordinates import img
from get_H_W import p1,p2,p3,p4
from get_H_W import max_w,max_h

src = np.float32([p1,p2,p3,p4])
des = np.float32([[0,0],[0,max_h],[max_w,max_h],[max_w,0]])

M = cv2.getPerspectiveTransform(src,des)

output = cv2.warpPerspective(img,M,(max_w,max_h))

plt.imshow(output)
plt.show()
