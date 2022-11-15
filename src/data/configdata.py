import os
import cv2 as cv
import glob
import numpy as np
import time
import datetime

# ImagePath= 'D:\\School\\Institut Teknologi Bandung\\Tahun 2\\Semester 1\\Linear Algebra dan Geometri\\Tugas Besar 2\\Algeo02-21054\\test\\pins_Adriana\\*.jpg'
ImagePath= './test/pins_Adriana/*.jpg'

cv_img = []


def Parser(path):
    int_img= []
    DirPath = os.path.abspath(path)
    print(DirPath)
    File= glob.glob(DirPath)
    for file in File:
        img= cv.imread(file)
        img_resize= cv.resize(img,(256,256))
        cv_img.append(img_resize)
        grayscale_img= cv.cvtColor(img_resize, cv.COLOR_BGR2GRAY)
        int_img.append(grayscale_img)
    return int_img

def camera_use():
    cam = cv.VideoCapture(0) #Start Camera
    cv.namedWindow("Camera") #Windows Title
    img_counter= 0
    end= False
    while  not end:
        total_time= 100
        while total_time>=10:
            ret, frame= cam.read() #reading
            if(not ret):
                print("Failed to proccess..")
                break
            cv.imshow("Display", frame) #Showing camera
            total_time-=1
            if(cv.waitKey(125) == ord('q')): #Escape key= q
                end= True
                break
        else:
            ret, frame= cam.read()
            cv.imshow("Display", frame)
            img_name= "{}/cap_cam_{}.jpg".format('./test/get_data', img_counter) #Image Name
            cv.imwrite(img_name, frame)
            print("Data Taken")
            img_counter+=1
            if(cv.waitKey(125) == ord('q')):
                end= True
                break
    cam.release() #Release Camera
    cv.destroyAllWindows() #Close All Opened Windows

# Parser('c:/Users/HP/Documents/Koding/Algeo02-21054/test/*.jpg')

# for image in int_img:
#     # image_int_data= imread(image)
#     cv.imshow('Image', image)
#     cv.waitKey(0)
# cv.destroyAllWindows()

# camera_use()


#Minimum eigen distance
def min_eigen_distance(List_of_vector, input_vector):
    min_distance= 0
    for i in range (len(List_of_vector)):
        min= np.subtract(List_of_vector[i], input_vector)
        min_distance_temp= np.linalg.norm(min)
        if(min_distance > min_distance_temp):
            min_distance= min_distance_temp
            indeks= i 
    return indeks

#Go through image database and return matrix that is pointed by the given indeks
def choose_image(indeks):
    return cv_img[indeks]


