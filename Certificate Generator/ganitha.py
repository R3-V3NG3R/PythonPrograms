import cv2
import numpy as np
import math
import csv

def generator(text,rank,eve):
    c=cv2.imread('ganitha_new.jpg')
    x=math.floor(1000+((22-len(text))*25))
    c=cv2.putText(c,text,(x,1175),cv2.FONT_HERSHEY_COMPLEX,4,(255,0,0),10)
    c=cv2.putText(c,rank,(630,1380),cv2.FONT_HERSHEY_DUPLEX,3.2,(0,0,0),5)
    c=cv2.putText(c,eve,(1515,1380),cv2.FONT_HERSHEY_DUPLEX,3,(0,0,0),5)

    cv2.imwrite('ganitha/'+text+'.jpg',c)
    

reader=csv.reader(open("wordpress.csv"))

for row in reader:
    generator(row[0],row[1],row[2])


