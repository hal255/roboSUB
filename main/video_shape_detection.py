'''
Created on Sep 7, 2016

This example program is used to detect shapes from a video feed

@author: Hong Luu
'''

import numpy as np
import cv2

from matplotlib import pyplot as plt


debug_mode = False  # if debug_mode is on, print debug message
camera_value = 0    # select camera here
contour_index = -1   # -1 to draw all contours
contour_thickness = 1   # -1 to fill in shape, integer values only
camera = cv2.VideoCapture(camera_value)

first_param = 127        # first param for finding optimal thresh 
second_param = 255       # second param for finding optimal thresh 
third_param = cv2.THRESH_BINARY_INV        # third param for finding optimal thresh 

while True:
    if debug_mode:
        print "still going"
    
    # get feed
    frame = camera.read()[1]
    
    # get dimensions of original feed
    img_height, img_width, img_channel = frame.shape
    
    # gray filter for easier rendering
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        
    # create two copies of the original image -- one for
    # the overlay and one for the final underwater_img image
    overlay = frame.copy()

    ret,thresh = cv2.threshold(gray,first_param,second_param,third_param)
    #ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #contours, h = cv2.findContours(thresh,1,2)
    
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        if debug_mode:
            print len(approx)
        if len(approx)==3:
            if debug_mode:
                print "triangle"
            cv2.drawContours(overlay,[cnt],contour_index,(0,0,255),contour_thickness)      # red for triangle
        elif len(approx)==4:
            if debug_mode:
                print "square"
            cv2.drawContours(overlay,[cnt],contour_index,(0,165,255),contour_thickness)    # orange for square
        
        elif len(approx)==5:
            if debug_mode:
                print "pentagon"
            cv2.drawContours(overlay,[cnt],contour_index,(0,255,255),contour_thickness)    # yellow for pentagon
        elif len(approx)==6:
            if debug_mode:
                print "hexagon"
            cv2.drawContours(overlay,[cnt],contour_index,(47,255,173),contour_thickness)   # light green for hexa
        '''    
        elif len(approx)==7:
            if debug_mode:
                print "heptagon"
            cv2.drawContours(overlay,[cnt],contour_index,(0,153,153),contour_thickness)    # dark green for hepta
        elif len(approx)==8:
            if debug_mode:
                print "octagon"
            cv2.drawContours(overlay,[cnt],contour_index,(226,43,138),contour_thickness)      # purple for octogon
        elif len(approx) == 9:
            if debug_mode:
                print "nonagon"
            cv2.drawContours(overlay,[cnt],contour_index,(255,255,0),contour_thickness)    # cyan for 9 sided
        elif len(approx) == 10:
            if debug_mode:
                print "nonagon"
            cv2.drawContours(overlay,[cnt],contour_index,(255,0,0),contour_thickness)    # blue for star
        elif len(approx) > 16:
            if debug_mode:
                print "circle"
            cv2.drawContours(overlay,[cnt],contour_index,(128,128,128),contour_thickness)  # gray for circle
        '''
    
    # display result
    cv2.imshow('original', frame)   # original
    cv2.imshow('gray', gray)
    cv2.imshow('result', overlay)
    
    # needed to run loop, listens for keyboard events
    k = cv2.waitKey(30)
    
    # if ESC or spacebar is pressed, exit
    if k == 27 or k == 32:
        break

    # if button 1 is pressed, first param + 1
    if k == 49:
        first_param += 1
        print "first param=", first_param

    # if button q is pressed, first param - 1
    if k == 113:
        first_param -= 1
        print "first param=", first_param

    # if button 2 is pressed, second param + 1
    if k == 50:
        second_param += 1
        print "second param=", second_param

    # if button w is pressed, second param - 1
    if k == 119:
        second_param -= 1
        print "second param=", second_param

    # if button 3 is pressed, third param + 1
    if k == 51:
        third_param += 1
        if third_param > 4:
            third_param = 4
        print "third param=", third_param

    # if button e is pressed, third param - 1
    if k == 101:
        third_param -= 1
        if third_param < 0:
            third_param = 0
        print "third param=", third_param

    # print parameters
    print first_param, second_param, third_param
    
    
    '''
    ret,th1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY,11,2)
    
    titles = ['Original Image', 'Global Thresholding (v = 127)',
                'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [gray, th1, th2, th3]
    
    for i in xrange(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()
    '''

############# END of While:True loop ######################    



cv2.destroyAllWindows()
camera.release()
print "done"
