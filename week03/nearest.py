import  cv2
import  numpy as np
import math
def Nearest(img):
    #读取图片的长，宽，通道
    height,width,channels = img.shape
    #获取图片的数据类型，img.dtype
    #创建一个800*800的图片值为0的图片，也就是黑色图片
    emptyImage=np.zeros((800,800,channels),np.uint8)

    # print(height,width,channels,img.dtype)

    sh = 800/height #新图和老图片长度的缩放比值
    sw = 800/width  #新图和老图片宽度的缩放比值

    for i in range(800):
        for j in range(800):
            # x= int(math.floor(i/sh))
            # y= int(math.floor(i/sw))
            x= int(i/sh+0.5)
            y= int(j/sw+0.5)
            emptyImage[i,j] =img[x,y]
    print(emptyImage)
    return emptyImage


img = cv2.imread("../img/lenna.png")
NearestImg=Nearest(img)
cv2.imshow("原图",img)
cv2.imshow("图片使用最近邻插值法",NearestImg)
#直接调用函数获取最邻居插值法扩大的图
NearestImg2=cv2.resize(img,(800,800))
cv2.imshow("图片使用最近邻插值法2",NearestImg2)
cv2.waitKey(0)
