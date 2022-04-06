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

storePos = [
	(131, 48),
	(305, 48),
	(479, 48),
	(653, 48),
	(828, 48),
]

cardSize = (298-131, 249-48)

i = 0
while True:
	l,t,r,b = (win.left, win.top, win.right, win.bottom)
	win.resizeTo(1040,600)
	# win.moveTo(0,0)
	# win.height = 600
	if(r-l != 1040):
		print(win)
		print("Invalid window size, skipping")
		continue
	sc = screenshot(l, t, r, b)
	cv.imshow('capture', sc)
	i = (i+1)%5
	cv.imshow("store1", sc[storePos[i][1]:storePos[i][1]+cardSize[1],storePos[i][0]:storePos[i][0]+cardSize[0]])
	if cv.waitKey(1) == ord('q'):
		cv.destroyAllWindows()
		break
