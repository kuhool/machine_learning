import  numpy as np
import cv2

"""
双线性插值法
"""

def bilinear_interpolation(img,out_dim):
    src_h,src_w,channels = img.shape
    dst_h,dst_w = out_dim[0],out_dim[1]
    print(src_h,src_w,dst_h,dst_w,channels)
    if src_h == dst_h and src_w == dst_h:
        return img.copy()

    dst_img = np.zeros((dst_h,dst_w,3),dtype=np.uint8)
    scale_x,scale_y=float(src_w/dst_w) ,float(src_h/dst_h)

    for i in range(channels):
        for dst_y in range(dst_h):
            for dst_x in range(dst_w):

                #加0.5就是中心点对称,
                #src_x=dst_x*scale_x 给原图和目标图x轴各加0.5
                src_x = (dst_x + 0.5) * scale_x-0.5
                src_y = (dst_y + 0.5) * scale_y-0.5

                src_x0 = int(np.floor(src_x))
                src_x1 = min(src_x0 +1,src_w-1)
                src_y0 = int(np.floor(src_y))
                src_y1 = min(src_y0 +1,src_h-1)

                #计算差值
                temp0 =(src_x1 - src_x) * img[src_y0,src_x0,i] + (src_x -src_x0) * img[src_y0,src_x1,i]
                temp1 =(src_x1 - src_x) * img[src_y1, src_x0, i] + (src_x - src_x0) * img[src_y1, src_x1, i]
                dst_img[dst_y,dst_x,i] = int((src_y1-src_y) *temp0 + (src_y-src_y0)*temp1)

    return dst_img

if __name__ == "__main__":
    img = cv2.imread("../img/lenna.png")
    dst = bilinear_interpolation(img,(700,700))
    cv2.imshow("old", img)
    cv2.imshow("bilinear_interpolation",dst)
    dst2 = cv2.resize(img,(800,800),cv2.INTER_LINEAR)
    cv2.imshow("bilinear_interpolation2", dst2)
    cv2.waitKey()
