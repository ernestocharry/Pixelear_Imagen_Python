import cv2
import os



image_folder = './img_segmented'
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

for i in images: 
    print(i)
    # Cargar la imagen

    file_name = '20240817_161744467_iOS_segmented_200.jpg'
    file_name = i
    number = file_name.replace('20240817_161744467_iOS_segmented_', '').replace('.jpg', '')
    image = cv2.imread(image_folder+'/'+file_name)

    #----------------------------
    # Definir el texto a agregar
    texto = "No. de colores:"
    posicion = (round(0.05*image.shape[1]), round(0.95*image.shape[0]))  # Coordenadas donde se ubicará el texto (x, y)
    font = cv2.FONT_HERSHEY_SIMPLEX  # Tipo de fuente
    tamaño_fuente = 5  # Tamaño del texto
    color = (255, 255, 255)  # Color del texto en formato BGR (blanco)
    grosor = 20  # Grosor del texto

    # Agregar el texto a la imagen
    cv2.putText(image, texto, posicion, font, tamaño_fuente, color, grosor, cv2.LINE_AA)

    #---------------------------------
    # Definir el texto a agregar

    posicion = (round(0.4*image.shape[1]), round(0.95*image.shape[0]))  # Coordenadas donde se ubicará el texto (x, y)
    font = cv2.FONT_HERSHEY_SIMPLEX  # Tipo de fuente
    tamaño_fuente = 5  # Tamaño del texto
    color = (255, 255, 255)  # Color del texto en formato BGR (blanco)
    grosor = 20  # Grosor del texto

    # Agregar el texto a la imagen
    cv2.putText(image, number, posicion, font, tamaño_fuente, color, grosor, cv2.LINE_AA)


    # Guardar la imagen resultante
    cv2.imwrite(file_name.replace('.jpg', '_with_text.jpg'), image)

    # Mostrar la imagen resultante (opcional)
    #cv2.imshow('Imagen con Texto', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()