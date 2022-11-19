import os
import cv2 as cv
import glob
import numpy as np
import time
import datetime

# ImagePath= 'D:\\School\\Institut Teknologi Bandung\\Tahun 2\\Semester 1\\Linear Algebra dan Geometri\\Tugas Besar 2\\Algeo02-21054\\test\\pins_Adriana\\*.jpg'
ImagePath= './test/pins_Adriana/*.jpg'

cv_img = [] # Dataset for image

# Parser file for folder
def Parser(path):
    int_img= []
    DirPath = path
    File = glob.glob(DirPath)
    for file in File:
        int_img.append(parser_one_file(file))
    return int_img

# Camera
# Will automatically capture data every 10 second
def camera_use():
    cam = cv.VideoCapture(0) #Start Camera
    cam.set(3, 1920) # Resolution 1080p
    cam.set(4, 1080)
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
            frame= cv.resize(frame, (256, 256))
            cv.imshow("Display", frame) #Showing camera
            total_time-=1
            if(cv.waitKey(125) == ord('q')): #Escape key= q
                end= True
                break
            elif(cv.waitKey(125) == ord('s')):
                img_name= "{}/cap_cam_{}.jpg".format('./test/get_data', img_counter) #Image Name
                cv.imwrite(img_name, frame)
                print("Data Taken")
                img_counter+=1
        else:
            ret, frame= cam.read()
            frame= cv.resize(frame, (256, 256))
            cv.imshow("Display", frame)
            img_name= "{}/cap_cam_{}.jpg".format('./test/get_data', img_counter) #Image Name
            cv.imwrite(img_name, frame)
            print("Data Taken")
            img_counter+=1
            if(cv.waitKey(125) == ord('q')):
                end= True
                break
    print("Closing Cam")
    cam.release() #Release Camera
    cv.destroyAllWindows() #Close All Opened Windows

# Parser('c:/Users/HP/Documents/Koding/Algeo02-21054/test/*.jpg')


# for image in int_img:
#     # image_int_data= imread(image)
#     cv.imshow('Image', image)
#     cv.waitKey(0)
# cv.destroyAllWindows()

camera_use()

# Go through image database and return matrix that is pointed by the given indeks
def choose_image(indeks):
    return cv_img[indeks] # get image from data set

# Parser only for one photo 
def parser_one_file(path):
    img= cv.imread(path)
    img_resize= cv.resize(img,(256,256))
    cv_img.append(img_resize)
    grayscale_img= cv.cvtColor(img_resize, cv.COLOR_BGR2GRAY)
    return grayscale_img.flatten()

# img = parser_one_file('./test/pins_Adriana/Adriana Lima0_0.jpg')
# cv.imshow("Image", img)
# cv.waitKey(0)
# cv.destroyAllWindows()