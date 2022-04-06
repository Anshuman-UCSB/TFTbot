import cv2
import mss
import numpy as np
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
		return img

def search(champValues, title, threshold = .8):
	for k, v in champValues.items():
		if ssim(title, v)>threshold:
			return k
	return None

# look at
# https://www.geeksforgeeks.org/python-image-classification-using-keras/

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,1)

def thresholding(image):
    return cv2.threshold(image, 0, 200, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def sumImage(image):
	return int(sum(sum(image)))