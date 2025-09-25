import os
import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

print('hasdas')
# Cargar la imagen
# Ruta de la imagen original y la ruta de salida
folder_loc = '/Users/charrypastrana/Documents/github/Pixelear_Imagen_Python/'
folder_loc = '/Users/felix/Documents/github/Pixelear_Imagen_Python/'
folder_loc += '0_sources_and_results'
os.chdir(folder_loc)


files = ['IMG_0141.JPEG']

for file_name in files: 
    #for i in [2, 3, 4, 5, 6, 7, 8]: 
    for i in [10, 12, 15, 20, 25, 30, 50]: 
        print('We are going in: ', i)
        image = cv2.imread(file_name)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Convertir la imagen en un array 2D de píxeles
        pixels = image.reshape(-1, 3)

        # Número de clusters (colores predominantes)
        num_clusters = 20
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
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.title('Imagen Original')
        plt.imshow(image)
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.title('Imagen Segmentada')
        plt.imshow(segmented_image)
        plt.axis('off')

        #plt.show()

        # plt.imsave(file_name.replace('.jpg', '_original.jpg'), image)
        if i<10:
            plt.imsave(file_name.replace('.JPEG', '_segmented_0' + str(num_clusters) + '.JPEG'), segmented_image)
        else:
            plt.imsave(file_name.replace('.JPEG', '_segmented_' + str(num_clusters) + '.JPEG'), segmented_image)