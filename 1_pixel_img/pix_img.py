from PIL import Image
import os

"""
Codigo para pixelear las imagenes ubicadas en la carpeta:
    img_source_and_results
"""

folder_loc = '/Users/charrypastrana/Documents/github/Pixelear_Imagen_Python/'

folder_loc = '/Users/felix/Documents/github/Pixelear_Imagen_Python/'
folder_loc += '0_sources_and_results'
print('Folder Loc: ', folder_loc)
os.chdir(folder_loc)

files = ['IMG_7699.jpg', 'IMG_7700.jpg']
files = ['IMG_0141.JPEG']

#file_name = 'DSC_0155.JPEG'
for file_name in files: 
    img = Image.open(file_name)

    no_pixels = [8,16,32,64,128,256,512,1024] # No. de Pixels

    # Find the name without the extation (png or jpeg)
    point_loc = file_name.find('.')
    file_name_without_extension = file_name[:point_loc]
    extension = file_name[point_loc:]

    for i in no_pixels:
        print('Number of Pixels: ', i)
        imgSmall = img.resize((i,i), resample=Image.BILINEAR)
        result = imgSmall.resize(img.size, Image.NEAREST)
        result.save(file_name_without_extension + '_pixe_' + str(i) + extension)

