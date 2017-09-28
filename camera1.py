from time import time
from flask import Flask
import cv2

class Camera(object):
 #   """An emulated camera implementation that streams a repeated sequence of
#    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

	def __init__(self):
        # self.video = cv2.VideoCapture('video.mp4')   for streaming any video file over the webpage
		self.camera = cv2.VideoCapture(0)
	def get_frame(self):
		
		# self.frames = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]
		
		while True:
		# grab the current frame
			(grabbed, frame) = self.camera.read()
			#key = cv2.waitKey(1) & 0xFF
			
			
			#if key==ord("q"):
			#	break
			#else:
			return cv2.imencode('.jpg',frame)[1].tobytes()
			

		#camera.release()
		
		
		
	
		#return self.frames[int(time()) % 3]





