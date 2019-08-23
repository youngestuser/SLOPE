#__*__coding=utf-8__*__
import cv2
import numpy as np

def p_dct(m_patches):
    l,w,h = np.shape(m_patches)
    for i in range(h):
        temp = np.reshape(m_patches[:,:,i],(l,w))
        m_patches[:,:,i]  = cv2.dct(temp)
       
    return m_patches

def p_idct(patches):
    a,b,c = np.shape(patches)
    for j in range(c):
        temp = np.reshape(patches[:, :, j], (a, b))
        patches[:,:,j] = cv2.idct(temp)
    return patches