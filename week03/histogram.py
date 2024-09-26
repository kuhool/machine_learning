import  cv2
import numpy as np
from matplotlib import pyplot as plt

'''
calcHist 计算直方图

函数原型：calcHist(img,channels,mask,histSize,ranges,hist=None,accumulate=None)
img :图像矩阵
channels :通道数
mask:掩膜 
histSize:直方图大小
ranges:横轴范围
'''


#灰度直方图
#获取灰度图像
#
img=cv2.imread("../img/lenna.png",1)
gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# # 创建一个新的图形窗口
# plt.figure()
# # 绘制直方图的函数 1.灰度图像 gray 转换为一维数组 2.指定直方图的“桶”数量
# plt.hist(gray.ravel(),256)
# plt.show()

#方法2
#
# hist = cv2.calcHist([gray],[0],None,[256],[0,256])
# plt.figure()
# plt.title("histogram")
# plt.xlabel("bins")
# plt.ylabel("of pixes")
# plt.plot(hist)
# plt.xlim([0,256])
# plt.show()

# 彩色直方图

chans =cv2.split(img)
colors = ("b","g","r")
plt.figure()
plt.title("histogram color")
plt.xlabel("bins")
plt.ylabel("of pixes")
for (chan,color) in zip(chans,colors):
    hist = cv2.calcHist([chan],[0],None,[256],[0,256])
    plt.plot(hist,color = color )
    plt.xlim([0,256])

plt.show()