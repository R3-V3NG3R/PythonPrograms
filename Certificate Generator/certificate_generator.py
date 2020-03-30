import cv2
import numpy as np
import math
import csv

def generator(text,fi,cID):
    c=cv2.imread('wordpress_new.jpg')
    x=math.floor(500+((22-len(text))*24))
    cv2.putText(c,text,(x,1750),cv2.FONT_HERSHEY_COMPLEX,4,(255,0,0),10)
    cv2.imwrite('wordpress/'+fi+'.jpg',cv2.putText(c,cID,(600,3030),cv2.FONT_HERSHEY_PLAIN,4,(0,0,0),5))


reader=csv.reader(open("wordpress.csv"))

for row in reader:
    generator(row[0],row[1],row[2])
