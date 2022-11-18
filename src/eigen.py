#MATRIX PASTI PERSEGI 256 kali 256 !1!1!1
import data.configdata as contol
import cv2 as cv
import numpy as np
from scipy.linalg import hessenberg

int_img = []
int_img = contol.Parser('./test/database_classmate/*.jpg')

height= 256
width= 256

def Mat2vec (Matrix): # Change
    matrix= np.array(Matrix, dtype='float64').flatten()
    return matrix

def Vec2Mat (Vector):
    return Vector.reshape(int(len(Vector)**(1/2)), int(len(Vector)**(1/2)))

def convertGambar (Dataset): # Change
    #mengubah sekumpulan dataset gambar menjadi list of vector
    vec = []
    for i in range(len(Dataset)):
        vec.append(Mat2vec(Dataset[i]))
    return vec

def Average (List_of_Vec): #Change
    # input : Matrix hasil convert gambar dari data set
    n = len(List_of_Vec)
    division= 1/n
    mean = [0.0 for i in range(65536)]
    for i in range (n):
        mean = np.add(mean, List_of_Vec[i])
    print(mean)
    print(n)
    return np.multiply(mean, division)
    # mean_face= np.zeros((1, height*width))
    # for i in List_of_Vec:
    #     mean_face= np.add(mean_face, i)
    # mean_face= np.divide(mean_face, float(len(List_of_Vec))).flatten()
    # return mean_face

def selisihdenganAVG (Vec, avg): # Change
    #input Vec adalah list of vector hasil dari convert gambar (Vec = convertGambar(Dataset)), dan avg adalah rata2 dari dataset
    DataSelisih = []
    for i in range(len(Vec)):
        dif= np.subtract(Vec[i], avg)
        DataSelisih.append(dif)
    return DataSelisih

def covarian (DataSelisih): # Change
    #DataSelisih adalah list of vector yang merupakan kumpulan vector yang sudah dikurangkan dengan rata2 dataset (DataSelisih = selisihdenganAVG)
    DataSelisihTranspose = np.transpose(DataSelisih)
    multiple= DataSelisih @ DataSelisihTranspose 
    return multiple / len(DataSelisih)

def eigen_qr(A): # A is the result of eigenspace_data * transpose(eigenspace_data)
    #A adalah matrix sembarang, digunakan untuk menghitung eigen val dan eigen vec dari matrix covarian
    Ai, Q = hessenberg(A, calc_q=True)
    QQ = np.eye(len(A))
    for i in range(5000):
        Q, R = np.linalg.qr(Ai)
        Ai = R @ Q
        QQ = QQ @ Q
    eigenVals = np.diag(Ai)
    return eigenVals, np.transpose(QQ)

def magnitude(vector):
    return np.linalg.norm(vector)

def eigenface (Covarian): # Dataselisih is eigenspace after being substract with average of n vectors
    #DataSelisih adalah list of vector yang merupakan kumpulan vector yang sudah dikurangkan dengan rata2 dataset (DataSelisih = selisihdenganAVG)
    #Covarian adalah matrix covarian dari dataset
    eigenval, eigenvec = eigen_qr(Covarian)
    # eigenvec = np.transpose(eigenvec)
    # print(eigenvec)
    eigenFace = []
    for i in range(len(eigenvec)):
        divider= 1/magnitude(eigenvec[i])
        eigenFace.append(np.multiply(eigenvec[i], divider))
    return eigenFace

def get_weight(eigenface, dif_with_avg_vector):
    weight_of_image= []
    for i in range (len(eigenface)):
        print(np.shape(dif_with_avg_vector))
        print(np.shape(np.transpose(eigenface[i])))
        weight_component = np.transpose(eigenface[i]) @ dif_with_avg_vector
        weight_of_image.append(weight_component)
    return weight_of_image

def get_eigen_distance(weight_input, weight_data):
    dif= np.subtract(weight_input, weight_data)
    return np.linalg.norm(dif)

def compare_distance(control_variable, free_variable): # free variable is a eigenspace
    min= get_eigen_distance(control_variable, free_variable[0])
    indeks= 0
    for i in range (len(free_variable)):
        min_temp= get_eigen_distance(control_variable, free_variable[i])
        if(min > min_temp):
            min= min_temp
            indeks= i
    return indeks

def run_func (input_img_path, dataset_img_path):
    input_mat= contol.parser_one_file(input_img_path)
    # cv.imshow("Image", input_mat)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    dataset_mat= contol.Parser(dataset_img_path)
    # # for i in range (len(dataset_mat)):
    # #     cv.imshow("Image", dataset_mat[i])
    # #     cv.waitKey(0)
    # # cv.destroyAllWindows()
    vector_dataset= convertGambar(dataset_mat)
    vector_input= Mat2vec(input_mat)
    avg_dataset= Average(vector_dataset)
    cv.imshow("Image", avg_dataset.reshape(256,256))
    cv.waitKey(0)
    cv.destroyAllWindows()
    # # avg_dataset= np.array(avg_dataset)
    # # avg_dataset= Vec2Mat(avg_dataset)
    # # cv.imshow("Image", avg_dataset)
    # # cv.waitKey(0)
    # # cv.destroyAllWindows()
    # dif_with_avg= selisihdenganAVG(vector_dataset, avg_dataset)
    # covarian_dataset= covarian(dif_with_avg)
    # # print(np.shape(covarian_dataset))
    # eigen_face= eigenface(covarian_dataset)
    # print(np.shape(eigen_face))
    # weight_of_data= []
    # for i in range (len(dif_with_avg)):
    #     weight_of_data.append(get_weight(eigen_face, dif_with_avg[i]))
    # weight_of_input= get_weight(eigen_face, vector_input)
    # indeks= compare_distance(weight_of_input, weight_of_data)
    # cv.imshow("Image", contol.choose_image(indeks))
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    
run_func('./test/get_data/IMG_5758.jpg', './test/database_classmate/*.jpg')
    
# Example Using
# input
# input_img= '.test/get_data/cap_cam_0.jpg'

# cv.imshow("Image", input_img)
# cv.waitKey(0)
# cv.destroyAllWindows()
# Selis


# # Get eigen distance from one image
# def get_eigen_distance(eigen_face, vector, average):
#     dif_with_avg= np.subtract(vector, average)
#     distance= dif_with_avg @ eigen_face
#     distance= np.linalg.norm(distance)
#     return distance

# def get_input_eigen_face (eigen_vec, dif_with_avg):
#     X = [0.0 for i in range(65536)]
#     for i in range (len(dif_with_avg)):
#         X = X + (eigen_vec[i] * dif_with_avg)
#     return X
    
# def get_eigen_distance(vector):
#     return np.linalg.norm(vector)

# # Get minimal eigen distance from difference between input image and dataset
# def min_eigen_distance(eigen_face_input, eigen_face_data):
#     dist_input= get_eigen_distance(eigen_face_input)
#     dist_data= get_eigen_distance(eigen_face_data[0])
#     data= dist_input- dist_data
#     min= abs(data)
#     indeks= 0
#     for i in range(len(eigen_face_data)):
#         dist_input= get_eigen_distance(eigen_face_input)
#         dist_data= get_eigen_distance(eigen_face_data[i])
#         data= dist_input- dist_data
#         min_temp= abs(data)
#         if(min > min_temp):
#             min= min_temp
#             indeks= i
#     return indeks

# ###### COntoh jika mau menacari eigen face ############
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
# # input_img= './test/pins_Adriana/Adriana Lima10_2.jpg' 
# input_img= './test/get_data/adrianna_lima.jpg'
# # Average
# avg = Average(convertGambar(int_img))
# # Difference with average
# dif_with_avg= selisihdenganAVG(convertGambar(int_img), avg)
# # Covarian
# covarian_result= covarian(dif_with_avg)
# # eigenface
# face= eigenface(dif_with_avg, covarian_result) 
# # parser input photo
# gray_img= contol.parser_one_file(input_img) 
# # Input photo vector eigen
# eigen_face_input= get_input_eigen_face(Mat2vec(gray_img), dif_with_avg)
# # minimal eigen distance
# indeks= min_eigen_distance(eigen_face_input, face)
# # output
# cv.imshow("gambar", contol.choose_image(indeks))
# cv.waitKey(0)
# cv.destroyAllWindows()














 