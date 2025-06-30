import os
import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Cargar la imagen
# Ruta de la imagen original y la ruta de salida
print(os.getcwd())

# MacOS
folder_loc = '/Users/charrypastrana/Documents/github/'
# Windows
folder_loc = '/Users/felix/'

folder_loc += 'Pixelear_Imagen_Python/0_sources_and_results'
os.chdir(folder_loc)

files = ['DSC00405.png', 'DSC00391.png']
files = ['DSC_0034.jpg']

for file_name in files: 
    
    # Identificar si es png or jpg
    file_extention = file_name[file_name.find('.'):]

    #for i in [3, 4, 5, 7, 8]: 
    for i in [10, 12, 15, 18, 20, 25]: 
    #for i in [18]: 
        print('File: ', file_name, 'and number of colors: ', i)
        image = cv2.imread(file_name)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Convertir la imagen en un array 2D de píxeles
        pixels = image.reshape(-1, 3)

        # Número de clusters (colores predominantes)
        num_clusters = i

        # Aplicar K-means
        kmeans = KMeans(n_clusters=num_clusters)
        kmeans.fit(pixels)

        # Obtener los colores centrales y etiquetas de cada píxel
        centers = kmeans.cluster_centers_
        labels = kmeans.labels_

        # Crear una imagen segmentada con los colores del K-means
        segmented_image = centers[labels].reshape(image.shape).astype(np.uint8)

        # Mostrar la imagen original y la imagen segmentada
        if False:
            plt.figure(figsize=(10, 5))
            plt.subplot(1, 2, 1)
            plt.title('Imagen Original')
            plt.imshow(image)
            plt.axis('off')

            plt.subplot(1, 2, 2)
            plt.title('Imagen Segmentada')
            plt.imshow(segmented_image)
            plt.axis('off')

            plt.show()

        # plt.imsave(file_name.replace('.jpg', '_original.jpg'), image)
        if i<10:
            color_section = '_NoOfColors_0'
        else:
            color_section = '_NoOfColors_'

        plt.imsave(
            file_name.replace(
                file_extention, 
                color_section + str(num_clusters) + file_extention
                ), segmented_image
        )