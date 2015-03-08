#!/usr/bin/env python
import numpy as np
import cv2
from scipy.misc import imread,imsave
from numpy import zeros
from PIL import Image

img1 = cv2.imread('001.tif',0) #imports the image in true cv grey 
print img1                          #checks for image if 'None' then path is incorect
print img1.shape                    #prints the dimensions of the image 
for i in range(3196):              #iterates through the image 
    if img1[i,15] < 35 and img1[i,15] > 10:#filters out the squigle
	print "Found the something at y=" #filters out the squigle and any fragments
	print i
	if img1[i,25] < 35 and img1[i,25] > 10:
		print "Found the something at y=" 
		print i
		if img1[i,35] < 35 and img1[i,35] > 10:
			print "Found the something at y=" 
			print i
	   		if img1[i,45] < 35 and img1[i,45] > 10:
				print "Found the img1 line at y=" 
				print i
				n1=i
				break

img2 = cv2.imread('002.tif',0) #imports the image in true cv grey 
print img2                          #checks for image if 'None' then path is incorect
print img2.shape                    #prints the dimensions of the image 
for i in range(3196):              #iterates through the image 
    if img2[i,15] < 35 and img2[i,15] > 10:#filters out the squigle
	print "Found the something at y=" #filters out the squigle and any fragments
	print i
	if img2[i,25] < 35 and img2[i,25] > 10:
		print "Found the something at y=" 
		print i
		if img2[i,35] < 35 and img2[i,35] > 10:
			print "Found the something at y=" 
			print i
	   		if img2[i,45] < 35 and img2[i,45] > 10:
				print "Found the img2 line at y=" 
				print i
				n2=i
				break
img3 = cv2.imread('003.tif',0) #imports the image in true cv grey 
print img3                          #checks for image if 'None' then path is incorect
print img3.shape                    #prints the dimensions of the image 
for i in range(3196):              #iterates through the image 
    if img3[i,15] < 35 and img3[i,15] > 10:#filters out the squigle
	print "Found the something at y=" #filters out the squigle and any fragments
	print i
	if img3[i,25] < 35 and img3[i,25] > 10:
		print "Found the something at y=" 
		print i
		if img3[i,35] < 35 and img3[i,35] > 10:
			print "Found the something at y=" 
			print i
	   		if img3[i,45] < 35 and img3[i,45] > 10:
				print "Found the img3 line at y=" 
				print i
				n3=i
				break
    else:
	n3=n2
for i in range(2338):              #iterates through the image 
    if img1[15,i] < 28 and img1[15,i] > 10:#filters out the squigle
	print "Found the something at x=" #filters out the squigle and any fragments
	print i
	if img1[25,i] < 35 and img1[25,i] > 10:
		print "Found the something at x=" 
		print i
		if img1[35,i] < 35 and img1[35,i] > 10:
			print "Found the something at x=" 
			print i
	   		if img1[45,i] < 35 and img1[45,i] > 10:
				print "Found the img1 line at x=" 
				print i
				m1=i
				break	
for i in range(2338):              #iterates through the image 
    if img2[15,i] < 28 and img2[15,i] > 10:#filters out the squigle
	print "Found the something at x=" #filters out the squigle and any fragments
	print i
	if img2[25,i] < 35 and img2[25,i] > 10:
		print "Found the something at x=" 
		print i
		if img2[35,i] < 35 and img2[35,i] > 10:
			print "Found the something at x=" 
			print i
	   		if img2[45,i] < 35 and img2[45,i] > 10:
				print "Found the img2 line at x=" 
				print i
				m2=i
				break
for i in range(2338):              #iterates through the image 
    if img3[15,i] < 28 and img3[15,i] > 10:#filters out the squigle
	print "Found the something at x=" #filters out the squigle and any fragments
	print i
	if img3[25,i] < 35 and img3[25,i] > 10:
		print "Found the something at y=" 
		print i
		if img3[35,i] < 35 and img3[35,i] > 10:
			print "Found the something at x=" 
			print i
	   		if img3[45,i] < 35 and img3[45,i] > 10:
				print "Found the img3 line at x=" 
				print i
				m3=i
				break
    else:
        m3=m2	
background = zeros([15985,6994], dtype=np.uint8)
#background = zeros([6994,6717], dtype=np.uint8)
print 'ABCNBCBAC', background.shape
yb=(n1-n2)
yyb=3197-yb
yc=yb+n3-n2
yyc=yyb-(n3-n2)
xb=(m1-m2)
xxb=xb-m1
xc=xb+m3-m2
xxc=2239-(m3-m2)
print "m1 ", m1
print yb
print yc
print 'Image 1 shape', img1.shape
background[3197*3:3197*4, 2239*2:2239*3]=img1[:3197, :2239]

background[3197*3-yb:3197*3+yyb, 2239-m1+xxb:2239*2+xxb]=img2[:3197, :2239]

background[3197*3-yc:3197*3+yyc, 0+(m3-m2):xxc+42]=img3[:3197, :2239]

cv2.imwrite("outt.jpg",background) 
cv2.waitKey(0)
cv2.destroyAllWindows()


