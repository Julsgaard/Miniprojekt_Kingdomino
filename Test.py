import cv2

# reading the image in grayscale mode
image = cv2.imread("Output.png",0)


# findcontours
cnts = cv2.findContours(image, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2]

# filter by area
s1 = -1
s2 = 10
xcnts = []

for cnt in cnts:
	if s1<cv2.contourArea(cnt) <s2:
		xcnts.append(cnt)

# printing output
print("\nDots number: {}".format(len(xcnts)))
