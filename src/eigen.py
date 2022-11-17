#MATRIX PASTI PERSEGI 256 kali 256 !1!1!1
import data.configdata as contol
import cv2 as cv
import numpy as np
from scipy.linalg import hessenberg

int_img = []
int_img = contol.Parser('./test/pins_Adriana/*.jpg')

def Mat2vec (Matrix):
    return Matrix.flatten()

def Vec2Mat (Vector):
    return Vector.reshape(int(len(Vector)**(1/2)), int(len(Vector)**(1/2)))

def convertGambar (Dataset):
    vec = []
    for i in range(len(Dataset)):
        vec.append(Dataset[i].flatten())
    return vec

def Average (Dataset):
    n = len(Dataset)
    Vec = convertGambar(Dataset)
    mean = [0.0 for i in range(65536)]
    for i in range(0,len(Vec)):
        mean = mean + Vec[i]
    return (mean/n)

def selisihdenganAVG (Dataset):
    Vec = convertGambar(Dataset)
    avg = Average(Dataset)
    DataSelisih = []
    for i in range(len(Vec)):
        DataSelisih.append(Vec[i] - avg)
    return DataSelisih

def covarian (Dataset):
    DataSelisih = selisihdenganAVG(Dataset)
    DataSelisihTranspose = np.transpose(DataSelisih)
    return DataSelisih @ DataSelisihTranspose 

def eigen_qr(A):
    Ai, Q = hessenberg(A, calc_q=True)
    QQ = np.eye(len(A))
    for i in range(5000):
        Q, R = np.linalg.qr(Ai)
        Ai = R @ Q
        QQ = QQ @ Q
    eigenVals = np.diag(Ai)
    return eigenVals, QQ



def eigenface (Dataset):
    DataSelisih = selisihdenganAVG(Dataset)
    eigenval, eigenvec = eigen_qr(covarian(Dataset))
    # eigenvec = np.transpose(eigenvec)
    eigenFace = []
    for i in range(len(Dataset)):
        X = [0.0 for i in range(65536)]
        for k in range(len(Dataset)):
            X = X + (eigenvec[i][k] * DataSelisih[k])
        X = Vec2Mat(X)
        eigenFace.append(X)
    return eigenFace


# DataSelisih = selisihdenganAVG(int_img)
# X = eigenface(int_img)
# for image in X:
#     image = np.array(image, dtype= np.uint8)
#     # image_int_data= imread(image)
#     cv.imshow('Image', image)
#     cv.waitKey(0)
# cv.destroyAllWindows()
# print(X[0])
# cv.imshow("kontol", X[0])
# cv.waitKey(0)

















 