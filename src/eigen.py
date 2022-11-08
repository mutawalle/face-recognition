#MATRIX PASTI PERSEGI 256 kali 256 !1!1!1
import data.configdata as contol
import cv2 as cv
import numpy as np


# def Mat2vec (Matrix):
#     return Matrix.flatten()

# def Vec2Mat (Vector):
#     return Vector.reshape(int(len(Vector)**(1/2)), int(len(Vector)**(1/2)))

# Matrix = [[(i+j) for i in range (10)] for j in range (10)]
# V1 = np.arange(9)
# V2 = np.arange(9)
# # Matrix = np.array(Matrix)
# # print (Matrix)
# # print(Mat2vec(Matrix))


# def jumlahVec(V1, V2):
#     V = [0 for i in range(len(V1))]
#     for i in range(len(V1)):
#         V[i] = V1[i] + V2[i]
#     return V


# def mean(Dataset):
#     # array = [0 for i in range(256**2)]
#     VecData = [array for i in range(len(Dataset))]
#     for i in range(len(Dataset)):
#         VecData[i] = Mat2vec(Dataset[i])
#     Vecjumlah = [0 for i in range(256**2)]
#     for i in range(len(VecData)):
#         Vecjumlah = jumlahVec(Vecjumlah, VecData[i])
#     for i in range(len(Vecjumlah)):
#         Vecjumlah[i] = Vecjumlah[i]/len(Dataset)
#     return Vecjumlah

int_img = []
int_img = contol.Parser('./test/pins_Adriana/*.jpg')


MATRIX = [[0 for i in range(256)] for j in range (256)]

def jumlahMatrix(M1, M2):
    M = [[0 for i in range(len(M1))] for j in range(len(M2))]
    for i in range (len(M1)):
        for j in range(len(M1)):
            M[i][j] = M1[i][j] + M2[i][j]
    return M

def displayMatrix (M):
    for i in range(0, len(M)):
        for j in range (0, len(M)):
            print(M[i][j], end=" ")
        print(" ")

def kaliMatrix (M1, M2):
    M = [[0 for i in range (len(M1))]for j in range(len(M2))]
    for i in range (len(M1)):
        for j in range (len(M1)):
            for k in range (len(M1)):
                M[i][j] += M1[i][k] * M2[k][j]
    return M

def kaliMatrixWithConst (const, M):
    for i in range(0, len(M)):
        for j in range (0, len(M)):
            M[i][j] *= const

def penguranganMatrix (M1, M2):
    hasil = [[0 for i in range(len(M1))] for j in range (len(M2))]
    for i in range(len(M1)):
        for j in range(len(M2)):
            hasil[i][j] = M1[i][j] - M2[i][j]
    return hasil


def meanMatrix (Dataset):
    M = [[0 for i in range(len(Dataset[0]))] for j in range(len(Dataset[0]))]
    for i in range (len(Dataset)):
        M = jumlahMatrix(M,Dataset[i])
    # displayMatrix(M)
    n = (1/len(Dataset))
    kaliMatrixWithConst(n, M)
    return M
    
def selisihDenganMean (Dataset):
    # MATRIX = [[0 for i in range(256)] for j in range (256)]
    DataSelisih =  [MATRIX for i in range(len(Dataset))]
    mean = meanMatrix(Dataset)
    for i in range(len(Dataset)):
        DataSelisih[i] = penguranganMatrix(Dataset[i], mean)
    return DataSelisih

def Tranpose (M):
    hasil = [[0 for i in range(len(M))] for j in range(len(M[0]))]
    for i in range (len(M)):
        for j in range (len(M[0])):
            hasil[i][j] = M[j][i]
    return hasil

def Covarian (Dataset):
    # MATRIX = [[0 for i in range(256)] for j in range (256)]
    AVG = meanMatrix(Dataset)
    Cov = []
    for i in range(len(Dataset)):
        X = penguranganMatrix(Dataset[i], AVG)
        Cov.append(kaliMatrix(X, Tranpose(X)))

    Cov = meanMatrix(Covarian)

    return Cov

# M1 = [[(i+1) for i in range(3)] for j in range(3)]
# M2 = [[(i+j) for i in range(3)] for j in range(3)]
# M3 = [[(i+3*j) for i in range(3)] for j in range(3)]
# displayMatrix(M1)
# displayMatrix(M2)
# print(M2 + M1)
# displayMatrix(M3)
# fak = [M1, M2, M3]
# X = Covarian(int_img)
# displayMatrix(X)
# X = np.array(X, dtype= np.uint8)
# cv.imshow("kontol", X)
# cv.waitKey(0)







 