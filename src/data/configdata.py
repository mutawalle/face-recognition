import cv2 as cv
import glob

# ImagePath= 'D:\\School\\Institut Teknologi Bandung\\Tahun 2\\Semester 1\\Linear Algebra dan Geometri\\Tugas Besar 2\\Algeo02-21054\\test\\pins_Adriana\\*jpg'

cv_img = []
int_img= []

def Parser(path):
    DirPath = path
    File= glob.glob(DirPath)
    for file in File:
        img= cv.imread(file)
        img_resize= cv.resize(img,(256,256))
        cv_img.append(img_resize)
        grayscale_img= cv.cvtColor(img_resize, cv.COLOR_BGR2GRAY)
        int_img.append(grayscale_img)


# Parser(ImagePath)
# print(int_img[1])