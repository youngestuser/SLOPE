# __*__ coding=utf-8 __*__
import numpy as np
# from scipy.io import loadmat
import patch_convert as pc
import hadmardgenerate as hc
import matplotlib.pyplot as plt
import block_dct as bd
from PIL import Image

r = 256
N = 65536
patch = 6
step = 2
sig = 2
iter_mum = 100
CSR = 0.4
mea_num = np.ceil(CSR*N)



im = Image.open("./Barbara.png")
im =np.array(im.resize((r,r)))
im = im[:]
M = hc.generate(2**16)
A = M[0:mea_num,:]
PA = A.T@(np.linalg.inv(A@A.T))
y = A@im
ima = A.T@(np.linalg.inv(A@A.T))@y
ima.resize((r,r))
for i in range(iter_mum):
    ima = ima + sig@PA@(y-A@ima)
    extract_p = pc.i2p(ima,patch,patch,step,step)
    p_dct = bd.p_dct(extract_p)
    pix = list(p_dct[:])
    pix.sort(reverse=True)
    thero = pix[mea_num+1]
    bater = p_dct*max(abs(pix)-thero,0)
    p_idct = bd.p_idct(bater)
    ima = pc.p2i(p_dct,r,r,step,step)

ima = ima.resize((r,r))
plt.imshow(ima)
plt.show()





# m = loadmat("./perm64k.mat")
# m = dict(m)
# m1 = m['P64k'][0]
# m3 = sorted(m1)
# print(m3[2517],m3[65535])
# print(len(m1))
# m2 = set(m1)
# print(m2)