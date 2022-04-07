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

i = 0
while True:
	# win.moveTo(0,0)
	if inst.assertSize() == False:
		continue
	sc = inst.screenshot()
	cv.imshow('capture', inst.sc)
	i = (i+1)%5
	# if i == 0:
	# 	if inst.isStoreOpen():
	# 		print("rolling")
	# 		inst.reroll()
	# guess, score,_ = search(inst.getStorePos(i))
	# cv.imshow("store/prediction", np.vstack((inst.getStorePos(i), guess)))
	cv.waitKey(1)
	# inst.openShop()
	print(inst.readShop(open = False))
	# print("prediction of score:",score)
	# if inst.isStoreOpen() and score<.80:
	# 	name = input("What champion is this: ")
	# else:
	# 	name = ""
	# if name == "quit":
	# 	cv.destroyAllWindows()
	# 	break
	# if name:
	# 	cv2.imwrite("champions/"+name+".png", storePos(sc, i))
