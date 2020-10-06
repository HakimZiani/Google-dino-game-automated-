import pyautogui
import numpy as np
import pyscreenshot as ImageGrab
from PIL import Image
import cv2
import time
#490,212,913,617
def screenshot():
	img = ImageGrab.grab(bbox=(650,212,850,315)).convert('L')
	#img.show()
	return img

def detect(data):
	for i in range(0,69):
		for j in range(0,40):
			#print(data[i,j])
			if data[i,j] < 100:
				pyautogui.press('up')
				return
''''
while (True):
	img = screenshot()
	detect(img.load())
	print(img.load())'''
def screen_record():
	last_time = time.time()
	while(True):
		# 800x600 windowed mode 650,212,850,315
		image = ImageGrab.grab(bbox=(680,270,750,315)).convert('L')

		#prints2 = np.array(ImageGrab.grab(bbox=()))

		#cv2.imshow('window',cv2.cvtColor(, cv2.COLOR_BGR2RGB))
		datae = image.load()
		detect(datae)
		printscreen =  np.array(image)
		print('loop took {} seconds'.format(time.time()-last_time))
		last_time = time.time()
		cv2.imshow('window23',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break

screen_record()
