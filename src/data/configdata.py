import os
import cv2 as cv
import glob
import time

# ImagePath= 'D:\\School\\Institut Teknologi Bandung\\Tahun 2\\Semester 1\\Linear Algebra dan Geometri\\Tugas Besar 2\\Algeo02-21054\\test\\pins_Adriana\\*.jpg'
ImagePath= './test/pins_Adriana/*.jpg'

cv_img = []
int_img= []

def Parser(path):
    DirPath = os.path.abspath(path)
    print(DirPath)
    File= glob.glob(DirPath)
    for file in File:
        img= cv.imread(file)
        img_resize= cv.resize(img,(256,256))
        cv_img.append(img_resize)
        grayscale_img= cv.cvtColor(img_resize, cv.COLOR_BGR2GRAY)
        int_img.append(grayscale_img)

def camera_use():
    cam= cv.VideoCapture(0) #Start Camera
    cv.namedWindow("Camera") #Windows Title
    img_counter= 0
    while True:
        time.sleep(10)# Pausing for 10s
        ret, frame= cam.read()
        if(not ret):
            print("Failed to proccess..")
            break
        cv.imshow("Display", frame) #Showing camera
        k= cv.waitKey(1) #Key
        if k%256 == 27:
            print("Closing camera..") #Key == Esc
            break
        img_name= "{}/cap_cam_{}.jpg".format('./test/get_data', img_counter) #Image Name
        cv.imwrite(img_name, frame)
        print("Data Taken")
        img_counter+=1
    cam.release() #Release Camera
    cam.destroyAllWindows() #Close All Opened Windows

# Parser(ImagePath)

# for image in int_img:
#     # image_int_data= imread(image)
#     cv.imshow('Image', image)
#     cv.waitKey(0)
# cv.destroyAllWindows()