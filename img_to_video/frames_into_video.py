


import cv2
import cv 
import os

image_folder = './img_to_video/'
video_name = 'video_1.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
print(images)

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc('M','J','P','G')

video = cv2.VideoWriter(image_folder+video_name, 0, 2, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()