from PIL import Image
import os

"""
Codigo para pixelear las imagenes ubicadas en la carpeta:
    0_sources_and_results
"""

# MacOS
folder_loc = '/Users/charrypastrana/Documents/github/'
# Windows
folder_loc = '/Users/felix/iCloudDrive/Documents/github/'

folder_loc += 'Pixelear_Imagen_Python/0_sources_and_results'

print('Folder Loc: ', folder_loc)
os.chdir(folder_loc)

files = ['DSC00295.png', 'IMG_7700.jpg']

files = ['img.png']

#file_name = 'DSC_0155.JPEG'
for file_name in files: 
    img = Image.open(file_name)
    no_pixels = [8,16,32,64,128,256,512,1024] # No. de Pixels
    no_pixels = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49] # No. de Pixels

    # Find the name without the extation (png or jpeg)
    point_loc = file_name.find('.')
    file_name_wo_extension = file_name[:point_loc]
    extension = file_name[point_loc:]

    for i in range(60, 160):
        print('File: ', file_name, 'and number of pixels: ', i)
        imgSmall = img.resize((i,i), resample=Image.BILINEAR)
        result = imgSmall.resize(img.size, Image.NEAREST)
        result.save(file_name_wo_extension + '_pixe_' + str(i) + extension)