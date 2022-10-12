import os
import glob
import cv2
import numpy as np

class RoiHandler:
    def __init__(self):
        self.points = []
    def grab_click_position(self,event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if len(self.points) >= 4:
                self.points = []
            self.points.append((x,y))

def load_image(image_file_number):
    image = cv2.imread(image_files[image_file_number])
    image_small = cv2.resize(image, (1200,800))
    return (image, image_small)

image_files = glob.glob("DSC_*.JPG")
image_file_number = 0
image, image_small = load_image(image_file_number)

roi = RoiHandler()
dst_points = np.array(((0,0),(500,0),(500,500),(0,500)))

output_file_number = 1

cv2.namedWindow("Input image")
cv2.setMouseCallback('Input image', roi.grab_click_position)

while True:
    image_small_lines = image_small.copy()
    cv2.polylines(image_small_lines, [np.array(roi.points, dtype=np.int32)], True, (0, 255, 0))
    cv2.imshow('Input image',image_small_lines)
    key = cv2.waitKey(20) & 0xFF
    if key == 27: # ESC
        break
    elif len(roi.points) == 4 and key == 32: # Space
        src_points = np.array([(x*5, y*5) for x, y in roi.points])
        transform, _ = cv2.findHomography(src_points, dst_points)
        adjusted_image = cv2.warpPerspective(image, transform, (500,500))
        filename = f"{output_file_number}.jpg"
        cv2.imwrite(filename, adjusted_image)
        print(f"Saved {filename}.")
        output_file_number += 1
    elif key == 100: # d
        image_file_number = max(0, image_file_number-1)
        image, image_small = load_image(image_file_number)
    elif key == 102: #
        image_file_number = min(len(image_files)-1, image_file_number+1)
        image, image_small = load_image(image_file_number)
    elif key != 255:
        print(key)
    if cv2.getWindowProperty('Input image',cv2.WND_PROP_VISIBLE) < 1:        
        break  
        

cv2.destroyAllWindows()