import  cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("../img/lenna.png",1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("img_",img)
# cv2.imshow("img_gray",gray)


# 灰度图像直方图均衡化
dst = cv2.equalizeHist(gray)

# 直方图
hist =cv2.calcHist([dst],[0],None,[265],[0,256])


# 创建一个新的图形窗口
plt.figure()
# 绘制直方图的函数 1.灰度图像 gray 转换为一维数组 2.指定直方图的“桶”数量
plt.hist(gray.ravel(),256)
plt.show()

cv2.imshow("直方图均衡化",np.hstack([gray,dst]))
cv2.waitKey(0)

