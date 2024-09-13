import gluonbook as gb
import mxnet as mx
from mxnet import autograd, gluon, image, init, nd
from mxnet.gluon import data as gdata, loss as gloss, utils as gutils
import sys
from time import time

gb.set_figsize()
img = image.imread('../img/lenna.png')
# print(img.shape)
# gb.plt.imshow(img.asnumpy())
# gb.plt.show()

#绘图函数 show_images
def show_images(imgs, num_rows, num_cols, scale=2):
    figsize = (num_cols * scale, num_rows * scale)
    _, axes = gb.plt.subplots(num_rows, num_cols, figsize=figsize)
    for i in range(num_rows):
        for j in range(num_cols):
            axes[i][j].imshow(imgs[i * num_cols + j].asnumpy())
            axes[i][j].axes.get_xaxis().set_visible(False)
            axes[i][j].axes.get_yaxis().set_visible(False)
    return axes

def apply(img, aug, num_rows=2, num_cols=4, scale=1.5):
    # 循环迭代0~num_rows * num_cols-1的每个值，多次调用aug(img)函数
    #语法形式为 [expression for item in iterable]，其中 expression 是对 item 执行的操作，iterable 是一个可迭代的对象。
    #Y是列表
    Y = [aug(img) for _ in range(num_rows * num_cols)]
    show_images(Y, num_rows, num_cols, scale)

#这个就是图片增广方法
#左右翻转
# apply(img, gdata.vision.transforms.RandomFlipLeftRight())

#上下翻转
# apply(img, gdata.vision.transforms.RandomFlipTopBottom())

#随机裁剪
# shape_aug = gdata.vision.transforms.RandomResizedCrop(
# (200, 200), scale=(0.1, 1), ratio=(0.5, 2))
# apply(img, shape_aug)

#颜色变化
# apply(img, gdata.vision.transforms.RandomBrightness(0.5))

#RandomColorJitter 实例并同时设置如何随机变化图像的亮度（brightness）、对⽐度（contrast）、饱和度（saturation）和⾊调（hue）
# color_aug = gdata.vision.transforms.RandomColorJitter(
# brightness=0.5, contrast=0.5, saturation=0.5, hue=0.5)
# apply(img, color_aug)

#多个叠加使用
# augs = gdata.vision.transforms.Compose([
# gdata.vision.transforms.RandomFlipLeftRight(),  gdata.vision.transforms.RandomColorJitter(
# brightness=0.5, contrast=0.5, saturation=0.5, hue=0.5),  gdata.vision.transforms.RandomColorJitter(
# brightness=0.5, contrast=0.5, saturation=0.5, hue=0.5)])
# apply(img, augs)


gb.plt.show()
