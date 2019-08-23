# __*__ coding __*__
import numpy as np
from PIL import Image
import patch_convert as pc
import hadmardgenerate as hc
import block_dct as bd
import random

r =64
N = 4096
patch = 6
step = 2
sig = 2
iter_mum = 100
CSR = 0.5
mea_num = int(np.ceil(CSR*N))

IM = Image.open("./Barbara.png")
IM = IM.resize((r,r))
IM.show()
IM = np.array(IM)
IM = IM.flatten()
M = hc.generate(2**12)
i = random.sample(range(mea_num),mea_num)
A = M[i,:]
c = random.sample(range(N),N)
A = A[:,c]
PA = A.T@(np.linalg.inv(A@A.T))
y = A@IM
ima = A.T@(np.linalg.inv(A@A.T))@y

for i in range(iter_mum):
    ima = ima + sig*PA@(y-A@ima)
    ima.resize((r, r))
    extract_p = pc.i2p(ima,patch,patch,step,step)
    p_dct = bd.p_dct(extract_p)
    pix = p_dct.flatten()
    pix = sorted(pix,reverse=True)
    thero = pix[mea_num+1]
    a = np.maximum(np.abs(p_dct) - thero, 0)
    bater = p_dct*a
    p_idct = bd.p_idct(bater)
    ima = pc.p2i(p_dct,r,r,step,step)
    ima = ima.flatten()

ima.resize((r,r))
pic = Image.fromarray(ima)
pic = pic.convert("L")
pic.save("./result.png")
