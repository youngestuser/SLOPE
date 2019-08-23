#__*__coding=utf-8__*__
import numpy as np

H = np.array([[1,1],[1,-1]])
def generate(m):
    if m==0:
        raise ValueError
    if m==2:
        return H
    else:
        return np.append(np.append(generate(m//2),generate(m//2),axis=1),np.append(generate(m//2),-1*generate(m//2),axis=1),axis=0)
           
if __name__ == "__main__":
    a = generate(64)
    #a.reshape((8,8))
    print(a)
