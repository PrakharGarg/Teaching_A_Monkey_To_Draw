# USAGE
# python compare.py

# import the necessary packages
from skimage.measure import compare_ssim as ssim
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np
import cv2
import os

def compare_images(imageA, imageB, t):
	# compute the mean squared error and structural similarity
	# index for the images
	s = ssim(imageA, imageB)
	if s < .85 :
		script = "rm " + t
		os.system(script)
		
		# setup the figure
		# fig = plt.figure(title)
		# plt.suptitle("SSIM: %.4f" % s)
		# 
		# # show first image
		# ax = fig.add_subplot(1, 2, 1)
		# plt.imshow(imageA, cmap = plt.cm.gray)
		# plt.axis("off")
		# 
		# # show the second image
		# ax = fig.add_subplot(1, 2, 2)
		# plt.imshow(imageB, cmap = plt.cm.gray)
		# plt.axis("off")
		# 
		# # show the images
		# plt.show()
		# plt.close()
	else :
		print_s = "echo " + str(s) + " >> ssim.txt"
		os.system(print_s)
		
    
def start_comparison(r,w) :
	# plt.ion()
	t = str((r.readline()).strip())
    # load the images -- the original, the original + contrast,
    # and the original + photoshop
	original = cv2.imread("images/square_1.png")
	compare = cv2.imread(t)

	# convert the images to grayscale
	original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
	compare = cv2.cvtColor(compare, cv2.COLOR_BGR2GRAY)
	# compare the images
	compare_images(original, compare, t)
