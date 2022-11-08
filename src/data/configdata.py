import os
import cv2 as cv
import glob
import time
import datetime

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
    end= False
    while  not end:
        total_time= 100
        while total_time>=10:
            ret, frame= cam.read()
            if(not ret):
                print("Failed to proccess..")
                break
            cv.imshow("Display", frame) #Showing camera
            total_time-=1
            if(cv.waitKey(125) == ord('q')):
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

# Parser(ImagePath)

# for image in int_img:
#     # image_int_data= imread(image)
#     cv.imshow('Image', image)
#     cv.waitKey(0)
# cv.destroyAllWindows()

camera_use()


# SET THE COUNTDOWN TIMER
# for simplicity we set it to 3
# We can also take this as input
# TIMER = int(20)
  
# # Open the camera
# cap = cv.VideoCapture(0)
  
 
# while True:
     
#     # Read and display each frame
#     ret, img = cap.read()
#     cv.imshow('a', img)
 
#     # check for the key pressed
#     k = cv.waitKey(125)
 
#     # set the key for the countdown
#     # to begin. Here we set q
#     # if key pressed is q
#     if k == ord('q'):
#         prev = time.time()
 
#         while TIMER >= 0:
#             ret, img = cap.read()
 
#             # Display countdown on each frame
#             # specify the font and draw the
#             # countdown using puttext
#             font = cv.FONT_HERSHEY_SIMPLEX
#             cv.putText(img, str(TIMER),
#                         (200, 250), font,
#                         7, (0, 255, 255),
#                         4, cv.LINE_AA)
#             cv.imshow('a', img)
#             cv.waitKey(125)
 
#             # current time
#             cur = time.time()
 
#             # Update and keep track of Countdown
#             # if time elapsed is one second
#             # than decrease the counter
#             if cur-prev >= 1:
#                 prev = cur
#                 TIMER = TIMER-1
 
#         else:
#             ret, img = cap.read()
 
#             # Display the clicked frame for 2
#             # sec.You can increase time in
#             # waitKey also
#             cv.imshow('a', img)
 
#             # time for which image displayed
#             cv.waitKey(2000)
 
#             # Save the frame
#             cv.imwrite('camera.jpg', img)
 
#             # HERE we can reset the Countdown timer
#             # if we want more Capture without closing
#             # the camera
 
#     # Press Esc to exit
#     elif k == 27:
#         break
 
# # close the camera
# cap.release()
  
# # close all the opened windows
# cv.destroyAllWindows()

# import datetime
 
# # Create class that acts as a countdown
# def countdown(h, m, s):
 
#     # Calculate the total number of seconds
#     total_seconds = h * 3600 + m * 60 + s
 
#     # While loop that checks if total_seconds reaches zero
#     # If not zero, decrement total time by one second
#     while total_seconds > 0:
 
#         # Timer represents time left on countdown
#         timer = datetime.timedelta(seconds = total_seconds)
        
#         # Prints the time left on the timer
#         print(timer, end="\r")
 
#         # Delays the program one second
#         time.sleep(1)
 
#         # Reduces total time by one second
#         total_seconds -= 1
 
#     print("Bzzzt! The countdown is at zero seconds!")
 
# # Inputs for hours, minutes, seconds on timer
# h = input("Enter the time in hours: ")
# m = input("Enter the time in minutes: ")
# s = input("Enter the time in seconds: ")
# countdown(int(h), int(m), int(s))