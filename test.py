# __*__ coding=utf-8 __*__

from PIL import Image
import numpy as np
import patch_convert as pc
import hadmardgenerate as hc
import block_dct as bd
import matplotlib.pyplot as plt

r =256
N = 1024
patch = 6
step = 1
sig = 2
iter_mum = 100
CSR = 0.5
mea_num = np.ceil(CSR*N)


im = Image.open("./Barbara.png")
im.show()
im =np.array(im.resize((r,r)))
print(im)
# M = hc.generate(2**16)
# A = M[0:mea_num,:]
# PA = A.T@(np.linalg.inv(A@A.T))
# y = A@im
# ima = A.T@(np.linalg.inv(A@A.T))@y
# for i in range(iter_mum):
#     ima = ima + sig@PA@(y-A@ima)
#     extract_p = pc.i2p(ima,patch,patch,step,step)
#     p_dct = bd.p_dct(extract_p)
#     pix = list(p_dct[:])
#     pix.sort(reverse=True)
#     thero = pix[mea_num+1]
#     bater = p_dct*max(abs(pix)-thero,0)
#     p_idct = bd.p_idct(bater)
#     ima = pc.p2i(p_dct,r,r,step,step)
#
# ima = ima.resize((r,r))
# plt.imshow(ima)
# plt.show()