import cv2
import os.path
import glob
import numpy as np
from PIL import Image
alpha=0
j=0
beta=0
def convertPNG(pngfile,outdir):
    # READ THE DEPTH
    im_depth = cv2.imread(pngfile)
    #apply colormap on deoth image(image must be converted to 8-bit per pixel first)
    im_color=cv2.applyColorMap(cv2.convertScaleAbs(im_depth,alpha=alpha,beta=beta),cv2.COLORMAP_JET)
    #convert to mat png
    im=Image.fromarray(im_color)
    #save image
    im.save(os.path.join(outdir,os.path.basename("RGBShendutu"+"_"+str(i)+"_"+".png")))
for i in range(800):
    alpha=255.000/(255-0)
    beta=beta+0.2
    convertPNG("L:/DepthMap/shendutu02.png","L:/DepthMap/RAINBOW/")
    print("正在生成第"+str(i)+"张"+",还剩"+str(500-i)+"张"+"当前alpha值为"+str(alpha)+"，当前beta值为"+str(beta))
        
# for i in range(500):
#     alpha=alpha+0.001
#     for j in range(500):
#         beta=beta+1
#         convertPNG("L:/DepthMap/shilishendutu.png","L:/DepthMap/shilishendutu/")
#         print("正在生成第"+str(i)+"张"+",还剩"+str(500-i)+"张"+",当前alpha="+str(alpha))
#批量化方法
# for pngfile in glob.glob("PNG FILE"):#C:/Users/BAMBOO/Desktop/source pics/rgbd_6/depth/*.png
    # convertPNG(pngfile,"TARGET FILE")#C:/Users/BAMBOO/Desktop/source pics/rgbd_6/color