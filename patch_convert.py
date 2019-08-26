#__*__coding=utf-8__*__
import numpy as np

#图片矩阵转小块,若遇到矩阵和数组的问题，可参考https://www.jb51.net/article/156109.htm
def i2p(im,n1,n2,step1,step2):
    #获取图片矩阵的大小
    #计算每块的坐标，包括x坐标和y坐标

    N1,N2 = im.shape[:]
    # print(N1,N2)
    xstart = [i for i in range(0,N1-n1+1,step1)]
    # print(xstart)
    a = [i for i in range(xstart[len(xstart)-1]+1,N1-n1+1)]
    xstart.extend(a)
    # print(xstart)
    ystart = [i for i in range(0,N2-n2+1,step2)]
    b = [i for i in range(ystart[len(ystart)-1]+1,N2-n2+1)]
    ystart.extend(b)

    l1 = len(xstart)
    l2 = len(ystart)
    xstartI = xstart * l2
    ystartI = list()
    for i in ystart:
        ystartI = ystartI + [i] * l1
    n1_minus1 = n1
    n2_minus2 = n2
    #小块的数量
    patch_num = len(xstartI)
    #提取每一小块
    M_patches = np.zeros((n1,n2,patch_num))
    for i in range(patch_num):
        patch = im[xstartI[i]:xstartI[i]+n1_minus1,ystartI[i]:ystartI[i]+n2_minus2]
        M_patches[:,:,i] = patch
    return M_patches

#块转图片矩阵
def p2i(m_patches,N1,N2,step1,step2):
    #获取块矩阵的大小
    (n1,n2,patch_num) = m_patches.shape
    #计算每块的坐标，包括x坐标和y坐标
    xstart = [i for i in range(0,N1-n1+1,step1)]
    a = [i for i in range(xstart[len(xstart)-1]+1,N1-n1+1)]
    xstart.extend(a)
    ystart = [i for i in range(0,N2-n2+1,step2)]
    b = [i for i in range(ystart[len(ystart)-1]+1,N2-n2+1)]
    ystart.extend(b)
    l1 = len(xstart)
    l2 = len(ystart)
    xstartI = xstart * l2
    ystartI = list()
    for i in ystart:
        ystartI = ystartI + [i] * l1
    n1_minus1 = n1
    n2_minus2 = n2
    #从块恢复图片
    im = np.zeros((N1,N2))
    M_weight = np.zeros((N1,N2))
    for j in range(patch_num):
        im[xstartI[j]:(xstartI[j]+n1_minus1),ystartI[j]:(ystartI[j]+n2_minus2)] = im[xstartI[j]:(xstartI[j]+n1_minus1),ystartI[j]:(ystartI[j]+n2_minus2)] + m_patches[:,:,j]
        M_weight[xstartI[j]:(xstartI[j]+n1_minus1),ystartI[j]:(ystartI[j]+n2_minus2)] = M_weight[xstartI[j]:(xstartI[j]+n1_minus1),ystartI[j]:(ystartI[j]+n2_minus2)] + 1
    return im / M_weight    