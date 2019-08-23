# __*___ coding=utf-8 __*__
import matplotlib.pyplot as plt
import numpy as np
import random
import hadmardgenerate as hd

i = random.sample(range(4),4)
A = hd.generate(4)
print(A)
A = A[i,:]
print(A)