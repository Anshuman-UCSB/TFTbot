import cv2 as cv
import pygetwindow
import random
import numpy as np
import pyautogui
import os
import pickle
from imageUtil import *

win = pygetwindow.getWindowsWithTitle("BlueStacks App")[0]

try:
	champValues = pickle.load(open('champValues.pkl','rb'))
except FileNotFoundError:
	champValues = {}


def storePos(sc, pos):
	storePos = [
		(131, 48),
		(305, 48),
		(479, 48),
		(653, 48),
		(827, 48),
	]

	cardSize = (298-131, 249-48)
	return grayscale(sc[storePos[pos][1]:storePos[pos][1]+cardSize[1],storePos[pos][0]:storePos[pos][0]+cardSize[0]])

i = 0
win.moveTo(0,0)
while True:
	l,t,r,b = (win.left, win.top, win.right, win.bottom)
	if(r-l != 1040):
		win.resizeTo(1040,600)
		print("Invalid window size, resizing")
		continue
	sc = screenshot(l, t, r, b)
	cv.imshow('capture', sc)
	i = (i+1)%5
	cv.imshow("store1", storePos(sc, i))
	guess, score = search(storePos(sc,i))
	if guess is not None:
		cv.imshow("Prediction:", guess)
	cv.waitKey(1)
	print("prediction of score:",score)
	if .32<score<.85:
		name = input("What champion is this: ")
	else:
		name = ""
	if name == "quit":
		cv.destroyAllWindows()
		break
	if name:
		cv2.imwrite("champions/"+name+".png", storePos(sc, i))
