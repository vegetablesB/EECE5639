'''
Author: Cao Ning
Date: 2022-06-06 13:52:14
FilePath: toVideo.py
Assignment:
Course: EECE5639
'''

import cv2
import os
from os.path import isfile, join
# pathIn= '../Office/'
# pathOut = './Videos/Office.mp4'
# pathIn= '../RedChair/'
# pathOut = './Videos/RedChair.mp4'
# pathIn= './Output/office_output/'
# pathOut = './Videos/OfficeMotion.mp4'


pathIn = './pics/'
pathOut = './Output/redchair_output/RedChairMotion.mp4'
# pathIn = './pics/'
# pathOut = './Output/office_output/OfficeMotion.mp4'
fps = 17  # 24fps for office video & 12fps for redchair seem okay

files = [f for f in os.listdir(pathIn) if isfile(
    join(pathIn, f))]
# for sorting the file names properly
print(len(files))
files.sort(key=lambda x: x[5:-4])
files.sort()
height, width, layers = cv2.imread(os.path.join(pathIn, files[0])).shape
size = (width, height)
frame_array = []

for i in range(len(files)):
    filename = pathIn + files[i]
    # reading each files
    img = cv2.imread(filename)
    frame_array.append(img)

out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()
