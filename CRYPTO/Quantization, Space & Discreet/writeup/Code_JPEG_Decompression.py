import numpy as np
from matplotlib import pyplot as plt
from os import system
system("cd /home/chelinka/Pictures/MakingACTF/step4")

def colorSpaceTFI(triplet):
    matriceCSTFI = np.array([[1., 0, 1.402], [1., -0.34414, -0.71414], [1., 1.772, 0]])
    return matriceCSTFI @ (triplet-np.array([[0, 128, 128]])).reshape(3)

def reformation(Y, Cb, Cr):
    Cb, Cr = Cb[:Y.shape[0], :Y.shape[1]], Cr[:Y.shape[0], :Y.shape[1]]
    matrix_refox = np.zeros((Y.shape[0], Y.shape[1], 3))
    matrix_refox[:,:,0], matrix_refox[:,:,1], matrix_refox[:,:,2] = Y, Cb, Cr
    calcul = np.apply_along_axis(colorSpaceTFI, 2, matrix_refox)
    return calcul.astype(int)

def upsampling(matrix_d):
    matrix_u = np.ones((matrix_d.shape[0]*2, matrix_d.shape[1]*2))
    for i in range(matrix_d.shape[0]):
        for j in range(matrix_d.shape[1]):
            matrix_u[2*i:2*(i+1), 2*j:2*(j+1)] *= matrix_d[i, j]
    return matrix_u

def chall1easy(Y):#chall 1 easy :
    plt.imshow(Y, cmap="gray")
    plt.show()

def chall1complete(Y, Cb, Cr):# chall 1 clean :
    Cb, Cr = upsampling(Cb), upsampling(Cr)
    image = reformation(Y, Cb, Cr)
    plt.imshow(image)
    plt.show()

def merging(matrix_c):
    matrix = np.zeros((matrix_c.shape[0]*8, matrix_c.shape[1]*8))
    for i in range(matrix_c.shape[0]):
        for j in range(matrix_c.shape[1]):
            matrix[8*i:8*(i+1), 8*j:8*(j+1)] = matrix_c[i,j]
    return matrix

def DCTI(matrix):
    F = np.zeros((8, 8))
    for u in range(8):
        for v in range(8):
            F += matrix[u, v]*coslist[u, v]
    return(F/4+128)

def mass_DCTI(matrix):
    g = np.zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            g[i, j] = DCTI(matrix[i, j])
    return np.clip(g, 0, 255)

def create_matrix_discreet():
    wow_matrix = np.ones((8, 8, 8, 8))
    for u in range(8):
        for v in range(8):
            for x in range(8):
                for y in range(8):
                    wow_matrix[u, v, x, y] = alpha(u)*alpha(v)*np.cos(u*np.pi*(2*x+1)/16)*np.cos(v*np.pi*(2*y+1)/16)
    return(wow_matrix)

def chall2easy(Y): #chall 2 easy :
    Y = mass_DCTI(Y)
    Y = merging(Y)
    plt.imshow(Y, cmap="gray")
    plt.show()

def chall2complete(Y, Cb, Cr): #chall 2 clean :
    Y, Cb, Cr = mass_DCTI(Y), mass_DCTI(Cb), mass_DCTI(Cr)
    Y, Cb, Cr = merging(Y), merging(Cb), merging(Cr)
    Cb, Cr = upsampling(Cb), upsampling(Cr)
    image = reformation(Y, Cb, Cr)
    plt.imshow(image)
    plt.show()

def Inversequantization(matrix, matrix_Q):
    return matrix * matrix_Q

def mass_QuantizationI(matrix, matrix_Q):
    g = np.zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            g[i, j] = Inversequantization(matrix[i, j], matrix_Q)
    return g

def chall3easy(Y): #chall 3 easy :
    Y = mass_QuantizationI(Y, Quantization_Matrix)
    Y = mass_DCTI(Y)
    Y = merging(Y)
    plt.imshow(Y, cmap="gray")
    plt.show()

def chall3complete(Y, Cb, Cr): #chall 3 clean :
    Y, Cb, Cr = mass_QuantizationI(Y, Quantization_Matrix),mass_QuantizationI(Cb, Quantization_Matrix),mass_QuantizationI(Cr, Quantization_Matrix)
    Y, Cb, Cr = mass_DCTI(Y), mass_DCTI(Cb), mass_DCTI(Cr)
    Y, Cb, Cr = merging(Y), merging(Cb), merging(Cr)
    Cb, Cr = upsampling(Cb), upsampling(Cr)
    image = reformation(Y, Cb, Cr)
    plt.imshow(image)
    plt.show()

do = 0 # 1 2 3

Y, Cb, Cr = np.load("chall{}_Y.npy".format(do)), np.load("chall{}_Cb.npy".format(do)), np.load("chall{}_Cr.npy".format(do))

alpha = lambda x : 1/np.sqrt(2) if (x==0) else 1
coslist = create_matrix_discreet()
    
Quantization_Matrix = np.array([16, 11, 10, 16, 24, 40, 51, 61, 12, 12, 14, 19, 26, 58, 60, 55, 14, 13, 16, 24, 40, 57, 69, 56, 14, 17, 22, 29, 51, 87, 80, 62, 18, 22, 37, 56, 68, 109, 103, 77, 24, 35, 55, 64, 81, 104, 113, 92, 49, 64, 78, 87, 103, 121, 120, 101, 72, 92, 95, 98, 112, 100, 103, 99]).reshape(8,8)

#chall1easy(Y)
#chall1complete(Y, Cb, Cr)
#chall2easy(Y)
#chall2complete(Y, Cb, Cr)
#chall3easy(Y)
#chall3complete(Y, Cb, Cr)