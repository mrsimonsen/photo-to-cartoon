import cv2
import numpy as np

def read_file(filename):
	img = cv2.imgread(filename)
	return img


