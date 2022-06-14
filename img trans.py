#==============================

# Bai tap lon Xu ly anh nhom 2-L01:

# BIEN DON HINH HOC (GEOMETRIC TRANSFORMATIONS)

# Nguyen Trong Tin - 1814343
# Nguyen Duc Thang - 1814094
# Truong Quang Linh - 1711986

#==============================

from matplotlib import pyplot as plt
import cv2
import numpy as np
import math

def gui():
	print("=== BIEN DOI HINH HOC ===\n")
	print("1. Phep phong dai anh (Scale)")
	print("2. Phep dich chuyen anh (Translation)")
	print("3. Phep xoay anh (Rotation)")
	print("4. Phep truot nghieng (Shear)")
	print("5. Phep bien doi Affine (Affine Transformation)")
	print("6. Phep bien doi phoi canh (Perspective Transformation)")
	choose = int(input("\nLua chon cua ban: "))
	# choose = 1
	return choose

def swit(choose, img):
	new = img
	if choose == 1: 
		new, uselib = scale_trans(img)
	if choose == 2: 
		new, uselib = translation(img)
	if choose == 3: 
		new, uselib = rotation_trans(img)
	if choose == 4: 
		new, uselib = shear_trans(img)
	if choose == 5: 
		new, uselib = affine_trans(img)
	# else: exit()
	return new, uselib

def warp_affine(img, M, op="None", arow=0, acol=0):
	rows, cols = img.shape[:2]
	orig = np.indices((cols, rows)).reshape(2, -1)	
	origF = np.vstack((orig, np.ones(rows*cols)))
	trans = np.dot(M, origF)
	trans = trans.astype(np.int)
	if op == "Yes":
		rows = rows + arow
		cols = cols + acol
	indices = np.all((trans[1]<rows, trans[0]<cols, trans[1]>=0, trans[0]>=0), axis=0)
	imgTrans = np.zeros((rows, cols, 3), dtype=np.uint8)
	imgTrans[trans[1][indices], trans[0][indices]] = img[orig[1][indices], orig[0][indices]]
	return imgTrans

def scale_trans(img):
	h = int(input("Ti le keo gian chieu cao: "))
	w = int(input("Ti le keo gian chieu rong: "))
	rows, cols = img.shape[:2]
	M = M = np.array([[w, 0, 0], [0, h, 0]], dtype=np.float32)
	imgScale = warp_affine(img, M, op="Yes", arow=rows*(h-1), acol=cols*(w-1))
	imgLib = cv2.resize(img, (int(w*cols), int(h*rows)), interpolation = cv2.INTER_LINEAR)
	return imgScale, imgLib

def translation(img):
	transx = int(input("Do dich chuyen qua phai: "))
	transy = int(input("Do dich chuyen xuong duoi: "))
	rows, cols = img.shape[:2]
	M = np.array([[1, 0, transx], [0, 1, transy]], dtype=np.float32)
	imgTrans = warp_affine(img, M, op="Yes", arow=positive(transy), acol=positive(transx))
	imgLib = cv2.warpAffine(img, M, (cols+transx, rows+transy))
	return imgTrans, imgLib

def rotation_trans(img):
	ang = int(input("Goc xoay: "))
	ang = -ang*math.pi/180
	rows, cols = img.shape[:2]
	M = np.array([[math.cos(ang), -math.sin(ang), 0], [math.sin(ang), math.cos(ang), 0]], dtype=np.float32)
	imgRota = warp_affine(img, M)
	imgLib = cv2.warpAffine(img, M, (cols, rows))
	return imgRota, imgLib

def shear_trans(img):
	shx = int(input("Do keo qua phai: "))
	rows, cols = img.shape[:2]
	M = np.float32([[1, shx/rows, 0], [0, 1, 0], [0, 0, 1]])
	M2 = np.float32([[1, shx/rows, 0], [0, 1, 0]])
	imgShear = warp_affine(img, M, op="Yes", acol=positive(shx))
	imgLib = cv2.warpAffine(img, M2, (cols+shx, rows))
	return imgShear, imgLib

def affine_trans(img):
	rows, cols = img.shape[:2]
	pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
	pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
	M = cv2.getAffineTransform(pts1, pts2)
	imgAffine = warp_affine(img, M)
	imgLib = cv2.warpAffine(img, M, (cols, rows))
	return imgAffine, imgLib

def pers_trans(name):
	global format
	img = cv2.imread(name)
	row, col = img.shape[:2]
	# peak, edges = corner_detect(img)
	# peakSwap = swap_xy(peak)
	pts1 = np.float32(mat)
	pts2 = np.float32([[0, 0], [col/2, 0], [col/2, row/2], [0, row/2]])
	M = cv2.getPerspectiveTransform(pts1, pts2)
	imgPers = cv2.warpPerspective(img,M,(int(col/2), int(row/2)))
	return imgPers

def click():
	pass

def corner_detect(image, minVal=100, maxVal=200):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray, (5, 5), 0)
	edges = cv2.Canny(blur, minVal, maxVal)

	row, col = edges.shape
	corr = 0
	peak = [0, 0, 0, 0]

	for r in range(0, row):
		key = ""
		for c in range(0, col):
			if edges[r, c] == 255:
				for i in range(0, 3):
					for j in range(0, 3):
						corr = corr + edges[r+i, c-1+j]
				if ((corr >= 255*4) and (peak[0] == 0)):
					peak[0] = [r, c]
					key = "top"
					break
				corr = 0
		if key == "top": break
	peak[1] = other_corner(edges, peak, 0, key)

	corr = 0
	for r in range(row-1, 0, -1):
		key = ""
		for c in range(col-1, 0, -1):
			if edges[r, c] == 255:
				for i in range(0, 3):
					for j in range(0, 3):
						corr = corr + edges[r-j, c+1-i]
				if ((corr >= 255*4) and (peak[2] == 0)):
					peak[2] = [r, c]
					key = "bottom"
					break
				corr = 0
		if key == "bottom": break
	peak[3] = other_corner(edges, peak, 2, key)

	return peak, edges

def other_corner(edges, res, numpeak, key):
	rl = {"right": -1, "left": 1}
	tb = {"top": 1, "bottom": -1}

	if edges[res[numpeak][0], res[numpeak][1]+10] == 0:
		side = "right"
	else:
		side = "left"

	runc = 0
	runr = 0
	count = 0
	temp = 0

	for i in range(0,500):
		runc = runc + rl.get(side)
		run = edges[res[numpeak][0]+runr, res[numpeak][1]+runc]
		if run == 0:
			runr = runr + tb.get(key)
			count = 1
			if temp == 1:
				count = 2
		else:
			count = 0
		temp = count
		if count == 2:
			res[numpeak+1] = [res[numpeak][0]+runr, res[numpeak][1]+runc]
			break

	return res[numpeak+1]

def swap_xy(mat):
	temp = 0
	for i in range(0, 4):
		temp = mat[i][0]
		mat[i][0] = mat[i][1]
		mat[i][1] = temp
	return mat

def positive(n):
	if n < 0:
		return 0
	return n

def onclick(event):
	global i
	global mat
	mat[i, 0] = event.xdata
	mat[i, 1] = event.ydata
	print('x = %d, y = %d'%(mat[i, 0], mat[i, 1]))
	circle = plt.Circle((mat[i, 0], mat[i, 1]), 5, color="r")
	ax.add_artist(circle)
	fig.canvas.draw()
	fig.canvas.flush_events()
	if (i >= 3):
		fig.canvas.mpl_disconnect(cid)
		plt.close()
	i = i+1
	

i = 0
mat = np.zeros((4, 2), dtype=np.float32)

c = gui()
if c < 6:
	img = cv2.imread("jr.png")
	imgNew, imgLib = swit(c, img)
	imgCvt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	imgNewCvt = cv2.cvtColor(imgNew, cv2.COLOR_BGR2RGB)
	imgLibCvt = cv2.cvtColor(imgLib, cv2.COLOR_BGR2RGB)
	plt.subplot(131), plt.imshow(imgCvt), plt.title('Ảnh gốc')
	plt.subplot(132), plt.imshow(imgNewCvt), plt.title('Ảnh đã biến đổi')
	plt.subplot(133), plt.imshow(imgLibCvt), plt.title('Bằng OpenCV')
	plt.show()
else:
	name = input("Ten anh: ")
	img = cv2.imread(name)
	fig = plt.figure()
	ax = fig.add_subplot(111)
	imgCvt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	plt.imshow(imgCvt), plt.title("Ảnh cần biến đổi")
	cid = fig.canvas.mpl_connect('button_press_event', onclick)
	plt.show()
	imgNew = pers_trans(name)
	imgNewCvt = cv2.cvtColor(imgNew, cv2.COLOR_BGR2RGB)
	plt.subplot(121), plt.imshow(imgCvt), plt.title('Ảnh gốc')
	plt.subplot(122), plt.imshow(imgNewCvt), plt.title('Ảnh đã biến đổi')
	plt.show()

