import cv2
vidcap = cv2.VideoCapture('IMG_3323 2023-11-30 04_27_07.mov')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1