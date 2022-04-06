import cv2 as cv
import numpy as np
import pyautogui
import os
import win32gui
import mss

def screenshot(l, t, r, b):
	with mss.mss() as sct:
		# Get information of monitor 2
		monitor_number = 0
		mon = sct.monitors[monitor_number]
		# The screen part to capture
		monitor = {
			"top": t,
			"left": l,
			"width": r-l,
			"height": b-t,
			"mon": 0,
		}
		# Grab the data
		sct_img = sct.grab(monitor)
		img = np.array(sct.grab(monitor)) # BGR Image
		return img

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

while True:
	updateWindows()
	l,t,r,b = map(int,bluestacks[0].split(','))
	sc = screenshot(l, t, r, b)
	cv.imshow('capture', sc)
	sc = screenshot(l+160, t+51, r-44, b-431)
	cv.imshow('store', sc)

	if cv.waitKey(1) == ord('q'):
		cv.destroyAllWindows()
		break
