import cv2 as cv
import pygetwindow
import random
import numpy as np
import pyautogui
import os
import pickle
from imageUtil import *

win = pygetwindow.getWindowsWithTitle("BlueStacks App")[0]
win.moveTo(0,0)

try:
	champValues = pickle.load(open('champValues.pkl','rb'))
except FileNotFoundError:
	champValues = {}

while True:
	l,t,r,b = (win.left, win.top, win.right, win.bottom)
	win.resizeTo(1040,600)
	# win.height = 600
	if(r-l != 1040):
		print(win)
		print("Invalid window size, skipping")
		continue
	sc = screenshot(l, t, r, b)
	cv.imshow('capture', sc)
	if cv.waitKey(1) == ord('q'):
		cv.destroyAllWindows()
		break
