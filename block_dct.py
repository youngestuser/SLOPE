#__*__coding=utf-8__*__
import cv2
import numpy as np

def p_dct(m_patches):
    l,w,h = np.shape(m_patches)
    for i in range(h):
        temp = m_patches[:,:,i]
        temp = np.float32(temp)
        m_patches[:,:,i]  = cv2.dct(temp)
       
    return m_patches

def p_idct(patches):
    a,b,c = np.shape(patches)
    for j in range(c):
        temp = patches[:, :, j]
        temp = np.float32(temp)
        patches[:,:,j] = cv2.idct(temp)
    return patches