#MATRIX PASTI PERSEGI 256 kali 256 !1!1!1
import data.configdata as contol
import cv2 as cv
import numpy as np
from scipy.linalg import hessenberg


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


MATRIX = np.zeros((256,256))

def displayMatrix (M):
    for i in range(0, len(M)):
        for j in range (0, len(M)):
            print(M[i][j], end=" ")
        print(" ")


def meanMatrix (Dataset):
    M = np.zeros((256,256))
    for i in range (len(Dataset)):
        M = M + Dataset[i]
    n = len(Dataset)
    return M/n
    
# def selisihDenganMean (Dataset):
#     DataSelisih =  []
#     mean = meanMatrix(Dataset)
#     for i in range(len(Dataset)):
#         DataSelisih.append((Dataset[i] - mean))
#     return DataSelisih


def Covarian (Dataset):
    # MATRIX = [[0 for i in range(256)] for j in range (256)]
    AVG = meanMatrix(Dataset)
    Cov = []
    n = len(Dataset)
    for i in range(n):
        X = Dataset[i] - AVG
        Cov.append((X @ np.transpose(X)))
        # X = penguranganMatrix(Dataset[i], AVG)
        # Cov.append(kaliMatrix(X, np.transpose(X)))

    Cov = meanMatrix(Cov)

    return Cov


def eigen_qr(A):
    Ai, Q = hessenberg(A, calc_q=True)
    for i in range(5000):
        Q, R = np.linalg.qr(Ai)
        Ai = R @ Q
    eigenVals = []
    for j in range (len(A)):
        eigenVals.append(Ai[j][j])
    return eigenVals



X = Covarian(int_img)
# displayMatrix(X)
print(eigen_qr(X))
# print(np.linalg.eigvals(X))
# X = np.array(X, dtype= np.uint8)
# cv.imshow("kontol", X)
# cv.waitKey(0)







 