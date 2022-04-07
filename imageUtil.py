import cv2
import mss
import numpy as np
import os
from skimage.metrics import structural_similarity as ssim

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
		return img#[:,:,:3]

def search(img):
	best = (None, 0, None)
	for filepath in os.listdir("champions"):
		# print(img.shape,end="	")
		im2 = cv2.imread("champions/"+filepath, cv2.IMREAD_GRAYSCALE)
		# print(im2.shape)
		score = ssim(img, im2)#, channel_axis=2)
		if score > best[1]:
			best = (im2, score, filepath[:-4])
		if score > .95:
			return best
	return best

def grayscale(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# look at
# https://www.geeksforgeeks.org/python-image-classification-using-keras/