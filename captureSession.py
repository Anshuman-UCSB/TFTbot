import pygetwindow
import cv2
import mss
import numpy as np
import time
import os

session = time.time()
os.mkdir(f"session{session}")
while True:
	with mss.mss() as sct:
		img = np.array(sct.grab(sct.monitors[2]))
		cv2.imshow("capture",img)
		k = cv2.waitKey(1000)
		cv2.imwrite(f"session{session}/{time.time()}.jpg", img)
		
		if k == 27:         # wait for ESC key to exit
			cv2.destroyAllWindows()
			break