import data.configdata as contol
import cv2 as cv
import numpy as np
from scipy.linalg import hessenberg
import glob


def Average(List_of_Vec):  #Change
    # input : Matrix hasil convert gambar dari data set
    n = len(List_of_Vec)
    division = 1 / n
    mean = [0.0 for i in range(65536)]
    for i in range(n):
        mean = np.add(mean, List_of_Vec[i])
    return np.multiply(mean, division)
    # mean_face= np.zeros((1, height*width))
    # for i in List_of_Vec:
    #     mean_face= np.add(mean_face, i)
    # mean_face= np.divide(mean_face, float(len(List_of_Vec))).flatten()
    # return mean_face


def selisihdenganAVG(Vec, avg):  # Change
    #input Vec adalah list of vector hasil dari convert gambar (Vec = convertGambar(Dataset)), dan avg adalah rata2 dari dataset
    DataSelisih = []
    for i in range(len(Vec)):
        dif = np.subtract(Vec[i], avg)
        DataSelisih.append(dif)
    return DataSelisih


def covarian(DataSelisih):  # Change
    #DataSelisih adalah list of vector yang merupakan kumpulan vector yang sudah dikurangkan dengan rata2 dataset (DataSelisih = selisihdenganAVG)
    DataSelisih = np.array(DataSelisih)
    return np.divide(np.matmul(DataSelisih, DataSelisih.T), len(DataSelisih))


def eigen_qr(
        A):  # A is the result of eigenspace_data * transpose(eigenspace_data)
    #A adalah matrix sembarang, digunakan untuk menghitung eigen val dan eigen vec dari matrix covarian
    Ai, Q = hessenberg(A, calc_q=True)
    QQ = np.eye(len(A))
    for i in range(5000):
        Q, R = np.linalg.qr(Ai)
        Ai = R @ Q
        QQ = QQ @ Q
    eigenVals = np.diag(Ai)
    return eigenVals, np.transpose(QQ)


def face_reg_func(path_dataset, path_input):
    vector_dataset = contol.Parser(path_dataset)
    vector_input_img = contol.parser_one_file(path_input)
    mean = Average(vector_dataset)
    centered_data = selisihdenganAVG(vector_dataset, mean)
    centered_data = np.array(centered_data)
    centered_data_input = np.subtract(vector_input_img, mean)
    correlation = covarian(centered_data)
    eigval, eigvec = eigen_qr(correlation)
    eigval = np.array(eigval)
    eigenface = np.transpose(np.dot(centered_data.transpose(), eigvec))
    weight_dataset = []
    for i in range(len(centered_data)):
        weight_dataset.append(np.dot(eigenface, centered_data[i]))
    weight_input = np.dot(eigenface, centered_data_input)
    min = np.linalg.norm(weight_input - weight_dataset[0])
    indeks = 0
    for i in range(len(centered_data)):
        min_temp = np.linalg.norm(weight_input - weight_dataset[i])
        if (min > min_temp):
            min = min_temp
            indeks = i
    return indeks


face_reg_func('./test/database_classmate/*.jpg', 'test\get_data\cap_cam_0.jpg')