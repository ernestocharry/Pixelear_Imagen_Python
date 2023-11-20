from PIL import Image
import os

print(os.getcwd())

file_name = 'DSC_0061.jpg'
img = Image.open(file_name)

print(img.size)

imgSmall = img.resize((1,1), resample=Image.BILINEAR)
result = imgSmall.resize(img.size, Image.NEAREST)
result.save('pixe_0001_'+file_name.replace('.jpeg', '.png'))

imgSmall = img.resize((2,2), resample=Image.BILINEAR)
result = imgSmall.resize(img.size, Image.NEAREST)
result.save('pixe_0002_'+file_name.replace('.jpeg', '.png'))

imgSmall = img.resize((4,4), resample=Image.BILINEAR)
result = imgSmall.resize(img.size, Image.NEAREST)
result.save('pixe_0004_'+file_name.replace('.jpeg', '.png'))


imgSmall = img.resize((8,8), resample=Image.BILINEAR)
result = imgSmall.resize(img.size, Image.NEAREST)
result.save('pixe_0008_'+file_name.replace('.jpeg', '.png'))


imgSmall = img.resize((16,16), resample=Image.BILINEAR)
result = imgSmall.resize(img.size, Image.NEAREST)
result.save('pixe_0016_'+file_name.replace('.jpeg', '.png'))

imgSmall = img.resize((32,32), resample=Image.BILINEAR)
result = imgSmall.resize(img.size, Image.NEAREST)
result.save('pixe_0032_'+file_name.replace('.jpeg', '.png'))


imgSmall = img.resize((64,64), resample=Image.BILINEAR)
result = imgSmall.resize(img.size, Image.NEAREST)
result.save('pixe_0064_'+file_name.replace('.jpeg', '.png'))


imgSmall = img.resize((128,128), resample=Image.BILINEAR)
result = imgSmall.resize(img.size, Image.NEAREST)
result.save('pixe_0128_'+file_name.replace('.jpeg', '.png'))

imgSmall = img.resize((256,256), resample=Image.BILINEAR)
result = imgSmall.resize(img.size, Image.NEAREST)
result.save('pixe_0256_'+file_name.replace('.jpeg', '.png'))

imgSmall = img.resize((512,512), resample=Image.BILINEAR)
result = imgSmall.resize(img.size, Image.NEAREST)
result.save('pixe_0512_'+file_name.replace('.jpeg', '.png'))

imgSmall = img.resize((1024,1024), resample=Image.BILINEAR)
result = imgSmall.resize(img.size, Image.NEAREST)
result.save('pixe_1024_'+file_name.replace('.jpeg', '.png'))