import cv2 as cv
import pygetwindow
import random
import numpy as np
import pyautogui
import os
import pickle
from instance import *
from imageUtil import *

win = pygetwindow.getWindowsWithTitle("BlueStacks App")[0]

inst = Instance(win)

while True:
	# win.moveTo(0,0)
	if inst.assertSize() == False:
		continue
	sc = inst.screenshot()
	cv.imshow('capture', inst.sc)
	if inst.isShopOpen():
		for i in range(5):
			card = inst.getShopPos(i)
			_, score, name = imageUtil.search(card)
			if score > .7:
				os.mkdir(f"captures/{name}",)
				cv.imwrite("captures/name/"+str(random.random())+".jpg", card)
			else:
				cv.imwrite("captures/unlabeled/"+str(random.random())+".jpg", card)

	cv.waitKey(1)
