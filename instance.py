import numpy as np
import random
import cv2
from time import sleep
import imageUtil
import pygetwindow
import pyautogui

class Instance:
	def __init__(self, win):
		self.win = win
		self.sc = self.screenshot()
	
	def assertSize(self):
		if self.win.size != (1040,600):
			print("Invalid window size, resizing.")
			self.resize()
			return False
		return True

	def compare(self, color, baseline, threshold = 15):
		return sum(abs(color- np.array(baseline)))<threshold

	def showArea(self, x, y, margin = 5):
		self.screenshot()
		cv2.imshow("showArea",self.sc[y-margin:y+margin,x-margin:x+margin,:])
		print(self.sc[(y,x)])
		cv2.waitKey(1)

	def resize(self):
		self.win.resizeTo(1040,600)

	def getTopLeft(self):
		return self.win.topLeft

	def screenshot(self):
		l,t,r,b = (self.win.left, self.win.top, self.win.right, self.win.bottom)
		self.sc = imageUtil.screenshot(l,t,r,b)


	def click(self, x, y, savePos = True):
		start = pyautogui.position()
		pos = (x,y)
		pyautogui.mouseDown(button='left',x=pos[0]+self.win.left,y=pos[1]+self.win.top, duration=.1)
		sleep(.1)
		pyautogui.mouseUp(button='left',x=pos[0]+self.win.left,y=pos[1]+self.win.top, duration=.1)
		if savePos:
			pyautogui.moveTo(*start)

	def getStorePos(self,pos):
		sc = self.sc
		storePos = [
			(131, 48),
			(305, 48),
			(479, 48),
			(653, 48),
			(827, 48),
		]

		cardSize = (298-131, 249-48)
		return imageUtil.grayscale(sc[storePos[pos][1]:storePos[pos][1]+cardSize[1],storePos[pos][0]:storePos[pos][0]+cardSize[0]])

	def buyStorePos(self, pos):
		if self.isStoreOpen():
			self.click(220+160*pos,140)
	
	def isStoreOpen(self):
		self.screenshot()
		sc = self.sc
		tier5shop = (913,280)
		# self.showArea(913,280)
		return self.compare(sc[tier5shop[::-1]],(44, 149, 220, 255))

	def reroll(self):
		pos = (950,400)
		start = pyautogui.position()
		self.click(*pos)		
		pyautogui.moveTo(start)

	def clickShop(self):
		pos = (950,530)
		self.click(*pos)
	
	def openShop(self):
		# cv2.imshow("section",self.sc[530:540,925:935,:])
		# print(self.sc[(920,535)[::-1]])
		self.screenshot()
		if self.isStoreOpen():
			return True
		
		if (all(self.sc[(920,535)[::-1]] == (109, 171, 199, 255)) or \
			all(self.sc[(930,535)[::-1]] == (109, 171, 199, 255))) and \
				self.isStoreOpen() == False:
			while self.isStoreOpen() == False:
				self.clickShop()
				self.screenshot()
			return True
		return False

	def readShop(self, open=False):
		if self.isStoreOpen() == False and open == False:
			return []
		if self.openShop() == False:
			return []
		champions = []
		for i in range(5):
			picture, score, name = imageUtil.search(self.getStorePos(i))
			if score > .7:
				champions.append(name)
			else:
				cv2.imwrite("champions/"+str(random.random())+".png", self.getStorePos(i))
				champions.append("?")
		return (champions)
