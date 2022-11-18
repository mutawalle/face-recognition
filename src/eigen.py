#MATRIX PASTI PERSEGI 256 kali 256 !1!1!1
import data.configdata as contol
import cv2 as cv
import numpy as np
from scipy.linalg import hessenberg

int_img = []
int_img = contol.Parser('./test/pins_Adriana/*.jpg')

def Mat2vec (Matrix):
    matrix= np.transpose(Matrix)
    return matrix.flatten()

def Vec2Mat (Vector):
    return Vector.reshape(int(len(Vector)**(1/2)), int(len(Vector)**(1/2)))

def convertGambar (Dataset):
    #mengubah sekumpulan dataset gambar menjadi list of vector
    vec = []
    for i in range(len(Dataset)):
        vec.append(Mat2vec(Dataset[i]))
    return vec

def Average (List_of_Vec):
    #input : Matrix hasil convert gambar dari data set
    n = len(List_of_Vec)
    mean = [0.0 for i in range(65536)]
    for i in range(0,n):
        mean = mean + List_of_Vec[i]
    return (mean/n)

def selisihdenganAVG (Vec, avg):
    #input Vec adalah list of vector hasil dari convert gambar (Vec = convertGambar(Dataset)), dan avg adalah rata2 dari dataset
    DataSelisih = []
    for i in range(len(Vec)):
        DataSelisih.append(Vec[i] - avg)
    return DataSelisih

def covarian (DataSelisih):
    #DataSelisih adalah list of vector yang merupakan kumpulan vector yang sudah dikurangkan dengan rata2 dataset (DataSelisih = selisihdenganAVG)
    DataSelisihTranspose = np.transpose(DataSelisih)
    return DataSelisih @ DataSelisihTranspose 

def eigen_qr(A):
    #A adalah matrix sembarang, digunakan untuk menghitung eigen val dan eigen vec dari matrix covarian
    Ai, Q = hessenberg(A, calc_q=True)
    QQ = np.eye(len(A))
    for i in range(5000):
        Q, R = np.linalg.qr(Ai)
        Ai = R @ Q
        QQ = QQ @ Q
    eigenVals = np.diag(Ai)
    return eigenVals, QQ

# Check eigen vector
# eigenval, eigenvec= eigen_qr(covarian(selisihdenganAVG(convertGambar(int_img), Average(convertGambar(int_img)))))
# print(np.shape(eigenvec))

def eigenface (DataSelisih, Covarian):
    #DataSelisih adalah list of vector yang merupakan kumpulan vector yang sudah dikurangkan dengan rata2 dataset (DataSelisih = selisihdenganAVG)
    #Covarian adalah matrix covarian dari dataset
    eigenval, eigenvec = eigen_qr(Covarian)
    # eigenvec = np.transpose(eigenvec)
    # print(eigenvec)
    eigenFace = []
    for i in range(len(DataSelisih)):
        X = [0.0 for i in range(65536)]
        for k in range(len(DataSelisih)):
            X = X + (eigenvec[i][k] * DataSelisih[k])
        # X = Vec2Mat(X)
        eigenFace.append(X)
    return eigenFace
    return np.transpose(eigenFace)

# # Get eigen distance from one image
# def get_eigen_distance(eigen_face, vector, average):
#     dif_with_avg= np.subtract(vector, average)
#     distance= dif_with_avg @ eigen_face
#     distance= np.linalg.norm(distance)
#     return distance

def get_input_eigen_face (eigen_vec, dif_with_avg):
    X = [0.0 for i in range(65536)]
    for i in range (len(dif_with_avg)):
        X = X + (eigen_vec[i] * dif_with_avg)
    return X
    


# Get minimal eigen distance from difference between input image and dataset
def min_eigen_distance(eigen_face_input, eigen_face_data):
    data= np.subtract(eigen_face_input, eigen_face_data)
    min= abs(data)
    indeks= 0
    for i in range(len(eigen_face_data)):
        data= np.subtract(eigen_face_input, eigen_face_data)
        min_temp= abs(data)
        if(min > min_temp):
            min= min_temp
            indeks= i
    return indeks

####### COntoh jika mau menacari eigen face ############
# Vec = convertGambar(int_img)
# avg = Average(convertGambar(int_img))
# DataSelisih = selisihdenganAVG(Vec, avg)
# Covarian = covarian(DataSelisih)
# Face = eigenface(DataSelisih, Covarian)
# for image in Face:
#     image = np.array(image, dtype= np.uint8)
#     image = Vec2Mat(image)
#     cv.imshow('Image', image)
#     cv.waitKey(0)

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

# def input_eigen_face(vector_input, Dataset):
#     eigenval, eigenvector= eigen_qr(Dataset)
#     average= Average(Dataset)
#     new_eigen = eigenvector @ vector_input - average
#     return new_eigen

# # Example Using
# # test case 
# input_img= './test/pins_Adriana/Adriana Lima10_2.jpg' 
# # input_img= './test/get_data/adrianna_lima.jpg'
# # eigenface
# face= eigenface(int_img) 
# # average
# average= Average(int_img) 
# # parser input photo
# gray_img= contol.parser_one_file(input_img) 
# # input eigen distance
# input_eigen_distance= get_eigen_distance(face, Mat2vec(gray_img), average)
# # data set after convert to vector
# data_set_eigen_distance= convertGambar(int_img)
# # minimal eigen distance
# indeks= min_eigen_distance(data_set_eigen_distance, input_eigen_distance, face, average)
# # output
# cv.imshow("gambar", contol.choose_image(indeks))
# cv.waitKey(0)
# cv.destroyAllWindows()














 