import cv2
import os



image_folder = './img_segmented'

file_name = '20240817_161744467_iOS_segmented_01.jpg'

number = file_name.replace('20240817_161744467_iOS_segmented_', '').replace('.jpg', '')
image = cv2.imread(image_folder+'/'+file_name)

# Parametros generales
font = cv2.FONT_HERSHEY_SIMPLEX  # Tipo de fuente
tamaño_fuente = 5  # Tamaño del texto
color = (255, 255, 255)  # Color del texto en formato BGR (blanco)
grosor = 20  # Grosor del texto

#----------------------------
# Definir el texto a agregar
texto = "Cuantos"
posicion = (round(0.05*image.shape[1]), round(0.60*image.shape[0]))  
# Coordenadas donde se ubicará el texto (x, y)
cv2.putText(image, texto, posicion, font, tamaño_fuente, color, grosor, cv2.LINE_AA)
#-------------------------------------------------------------------------------
texto = "colores"
posicion = (round(0.05*image.shape[1]), round(0.65*image.shape[0]))  
cv2.putText(image, texto, posicion, font, tamaño_fuente, color, grosor, cv2.LINE_AA)
#-------------------------------------------------------------------------------
texto = "son"
posicion = (round(0.05*image.shape[1]), round(0.70*image.shape[0]))  
cv2.putText(image, texto, posicion, font, tamaño_fuente, color, grosor, cv2.LINE_AA)
#-------------------------------------------------------------------------------
texto = "necesarios"
posicion = (round(0.05*image.shape[1]), round(0.75*image.shape[0]))  
cv2.putText(image, texto, posicion, font, tamaño_fuente, color, grosor, cv2.LINE_AA)
#-------------------------------------------------------------------------------
texto = "para"
posicion = (round(0.05*image.shape[1]), round(0.80*image.shape[0]))  
cv2.putText(image, texto, posicion, font, tamaño_fuente, color, grosor, cv2.LINE_AA)
#-------------------------------------------------------------------------------
texto = "transmitir"
posicion = (round(0.05*image.shape[1]), round(0.85*image.shape[0]))  
cv2.putText(image, texto, posicion, font, tamaño_fuente, color, grosor, cv2.LINE_AA)
#-------------------------------------------------------------------------------
texto = "la"
posicion = (round(0.05*image.shape[1]), round(0.90*image.shape[0]))  
cv2.putText(image, texto, posicion, font, tamaño_fuente, color, grosor, cv2.LINE_AA)
#-------------------------------------------------------------------------------
texto = "informacion"
posicion = (round(0.05*image.shape[1]), round(0.95*image.shape[0]))  
cv2.putText(image, texto, posicion, font, tamaño_fuente, color, grosor, cv2.LINE_AA)


# Guardar la imagen resultante
cv2.imwrite(file_name.replace('.jpg', '_with_text_0_link.jpg'), image)

# Mostrar la imagen resultante (opcional)
#cv2.imshow('Imagen con Texto', image)
cv2.waitKey(0)
cv2.destroyAllWindows()