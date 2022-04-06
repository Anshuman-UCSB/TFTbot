import cv2 as cv
import random
import numpy as np
import pyautogui
import os
import win32gui
import pickle
from imageUtil import *

def callback(hwnd, strings):
	if win32gui.IsWindowVisible(hwnd):
		window_title = win32gui.GetWindowText(hwnd)
		left, top, right, bottom = win32gui.GetWindowRect(hwnd)
		if window_title and right-left and bottom-top and "BlueStacks" in window_title and "Manager" not in window_title:
			strings.append(','.join(map(str,[left, top, right, bottom])))
	return True
bluestacks = []
def updateWindows():
	global bluestacks
	bluestacks = []
	win32gui.EnumWindows(callback, bluestacks)

def OCR(champValues, img, threshold):
	value = sumImage(img)
	for k,v in champValues.items():
		if abs(k-value) < threshold:
			return v
	return None

i = 0
try:
	champValues = pickle.load(open('champValues.pkl','rb'))
except FileNotFoundError:
	champValues = {}
tolerance = 100
firstRun = True
seen = []
while True:
	updateWindows()
	l,t,r,b = map(int,bluestacks[0].split(','))
	assert(r-l == 1246)
	sc = screenshot(l, t, r, b)
	cv.imshow('capture', sc)
	store = sc[51:-431,160:-15]
	cv.imshow('store', store)
	img = cv.cvtColor(store, cv.COLOR_BGR2GRAY)
	img = thresholding(img)
	
	cv.imshow('mask', img)
	titles = np.array_split(img[180:-9],5,axis = 1)
	name1 = titles[i%5][0:28,5:150]
	i+=1
	cv.imshow('titles', name1)
	print(champValues.keys())
	# if input("Save? ")!="":
	# 	cv.imwrite(str(random.random())+".jpg", name1)
	if cv.waitKey(1) == ord('q'):
		cv.destroyAllWindows()
		pickle.dump(champValues,open('champValues.pkl','wb'))
		break
	if not firstRun and search(champValues, name1) == None:
		name = input("What champion is this?")
		if name != "":
			if name not in champValues:
				champValues[name] = name1
			else:
				print(ssim(champValues[name], name1))
	firstRun = False
