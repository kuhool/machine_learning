import cv2
import numpy as np

# 读取图像
img = cv2.imread("../img/lenna.png", 1)

# 检查图像是否成功读取
if img is None:
    print("无法读取图像，请检查路径")
else:
    # 分离颜色通道
    (b, g, r) = cv2.split(img)

    # 对每个通道进行直方图均衡化
    bH = cv2.equalizeHist(b)
    gH = cv2.equalizeHist(g)
    rH = cv2.equalizeHist(r)

    # 合并均衡化后的通道
    result = cv2.merge((bH, gH, rH))

    # 显示结果
    cv2.imshow("彩色直方图均衡化", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()