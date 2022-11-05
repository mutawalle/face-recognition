#MATRIX PASTI PERSEGI 256 kali 256 !1!1!1
MATRIX = [[0 for i in range(256)] for j in range (256)]

def jumlahMatrix(M1, M2):
    M = [[0 for i in range(len(M1))] for j in range (len(M2))]
    for i in range (0,len(M1)):
        for j in range(0,len(M2)):
            M[i][j] = M1[i][j] + M2[i][j]
    return M

def displayMatrix (M):
    for i in range(0, len(M)):
        for j in range (0, len(M)):
            print(M[i][j], end=" ")
        print(" ")

def kaliMatrix (M1, M2):
    M = [[0 for i in range(len(M1))] for j in range (len(M2))]
    for i in range (0,len(M1)):
        for j in range (0, len(M2)):
            M[i][j] = 0
            for k in range (0,len(M1)):
                M[i][j] += M1[i][k] * M2[k][j]
    return M

def kaliMatrixWithConst (const, M):
    hasil = [[0 for i in range(len(M))] for j in range (len(M))]
    for i in range(0, len(M)):
        for j in range (0, len(M)):
            hasil[i][j] *= const
    return hasil

def penguranganMatrix (M1, M2):
    hasil = [[0 for i in range(len(M1))] for j in range (len(M1))]
    for i in range(0, len(M1)):
        for j in range(0,len(M1)):
            hasil[i][j] = M1[i][j] - M2[i][j]
    return hasil


def meanMatrix (Dataset):
    M = [[0 for i in range(256)] for j in range (256)]
    for i in range (0,len(Dataset)):
        M = jumlahMatrix(M,Dataset[i])
    M = kaliMatrixWithConst((1/len(Dataset)), M)
    return M
    
def selisihDenganMean (Dataset):
    # MATRIX = [[0 for i in range(256)] for j in range (256)]
    DataSelisih =  [MATRIX for i in range(len(Dataset))]
    mean = meanMatrix(Dataset)
    for i in range(0, len(DataSelisih)):
        DataSelisih[i] = penguranganMatrix(Dataset[i], mean)
    return DataSelisih

def Tranpose (M):
    hasil = [[0 for i in range(len(M))] for j in range (len(M))]
    for i in range (0, len(M)):
        for j in range (0, len(M)):
            hasil[i][j] = M[j][i]
    return hasil

def Covarian (Dataset):
    # MATRIX = [[0 for i in range(256)] for j in range (256)]
    DataSelisih =  [MATRIX for i in range(len(Dataset))]
    DataSelisih = selisihDenganMean(Dataset)
    DataSelisihTranpose = [MATRIX for i in range(len(Dataset))]
    perkalian = [MATRIX for i in range(len(Dataset))]

    for i in range(0, len(Dataset)):
        DataSelisihTranpose[i] = Tranpose(DataSelisih)

    for i in range(0, len(Dataset)):
        perkalian[i] = kaliMatrix(DataSelisih[i], DataSelisihTranpose[i])

    Cov = meanMatrix(perkalian)

    return Cov
    

M1 = [[2 for i in range(3)] for j in range (3)]
M2 = [[3 for i in range(3)] for j in range (3)]
M = kaliMatrix(M1,M2)
displayMatrix(M)






 