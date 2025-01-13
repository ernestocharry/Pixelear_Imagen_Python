from PIL import Image
import os
import numpy as np

print(os.getcwd())

# ecuation 
# y = a+exp(b*x) 
a = 1
b = -np.log(256)/260

# y = mx + b
b = 1
m = (256-1)/260

print('m: ', m)
print('b: ', b)

i_initial = 0 
i_final = 260+1
delta_i = 1

for i in range(i_initial, i_final): 
    file_name = 'Video_into_frames/frame' + str(i) + '.jpg'
    #print(file_name)
    img = Image.open(file_name)
    size = int(np.round(a*np.exp(-b*float(i)),0))
    size = int(np.round(m*float(i)+b,0))
    print(i, size)

    imgSmall = img.resize((size,size), resample=Image.BILINEAR)
    result = imgSmall.resize(img.size, Image.NEAREST)

    if i < 10: 
        result.save(file_name.replace('/frame', '/pix_frame00'))
    elif i < 100: 
        result.save(file_name.replace('/frame', '/pix_frame0'))
    else: 
        result.save(file_name.replace('/frame', '/pix_frame'))
    
