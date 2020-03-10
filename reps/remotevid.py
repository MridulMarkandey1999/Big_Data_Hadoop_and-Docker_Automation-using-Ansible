import cv2

x= cv2.VideoCapture(0)
while True:
	status, photo= x.read()
	cv2.imshow("hi",photo)
	if cv2.waitKey(1) == 13:
		break
cv2.destroyAllWindows()
x.release()

