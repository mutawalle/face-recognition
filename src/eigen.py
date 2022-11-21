import configdata as cd
import numpy as np
from scipy.linalg import hessenberg


def Average(List_of_Vec):  #Change
    # input : Matrix hasil convert gambar dari data set
    n = len(List_of_Vec)
    division = 1 / n
    mean = [0.0 for i in range(65536)]
    for i in range(n):
        mean = np.add(mean, List_of_Vec[i])
    return np.multiply(mean, division)


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

def householder(a):
    v = a/(a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    H = np.eye(a.shape[0])
    H -= (2/np.dot(v,v)) * np.dot(v[:, None], v[None, :])
    return H

def qr_decomposition (A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(m - (m == n)):
        H = np.eye(m)
        H[i:, i:] = householder(A[i:,i])
        Q = np.dot(Q,H)
        A = np.dot(H,A)
    return Q, A


def face_reg_func(path_dataset, path_input):
    vector_dataset = cd.Parser(path_dataset)
    vector_input_img = cd.parser_one_file(path_input)
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
        min_temp= np.linalg.norm(weight_input-weight_dataset[i])
        if(min > min_temp):
            min= min_temp
            indeks= i
    return indeks