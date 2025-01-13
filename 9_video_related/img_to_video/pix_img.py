from PIL import Image
import os

os.chdir("./img_to_video/")


print(os.getcwd())

file_name = 'IMG_4431.jpg'
img = Image.open(file_name)

for i in range(1,1024+1): 
    imgSmall = img.resize((i,i), resample=Image.BILINEAR)
    result = imgSmall.resize(img.size, Image.NEAREST)
    if i < 10: 
        result.save('pixe_000' + str(i) +file_name.replace('.jpeg', '.png'))
    elif i < 100:
        result.save('pixe_00' + str(i) +file_name.replace('.jpeg', '.png'))
    elif i < 1000:
        result.save('pixe_0' + str(i) +file_name.replace('.jpeg', '.png'))
    else: 
        result.save('pixe_' + str(i) +file_name.replace('.jpeg', '.png'))

