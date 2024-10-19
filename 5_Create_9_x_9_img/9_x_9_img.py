from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import math

# Ruta de la imagen original y la ruta de salida
folder_loc = '/Users/charrypastrana/Documents/github/Pixelear_Imagen_Python/'
folder_loc += '0_sources_and_results'
os.chdir(folder_loc)



def unir_imagenes(imagenes):
    # Abrir todas las imágenes
    imagenes_abiertas = [Image.open(img) for img in imagenes]
    
    # Verificar que todas las imágenes sean del mismo tamaño
    tamanio_img = imagenes_abiertas[0].size
    for img in imagenes_abiertas:
        assert img.size == tamanio_img, "Todas las imágenes deben ser del mismo tamaño y cuadradas."

    # Calcular el número de imágenes por fila/columna (9x9 en este caso)
    num_imagenes = len(imagenes_abiertas)
    lado_cuadrado = int(math.sqrt(num_imagenes))  # Lado de la cuadrícula (en este caso, 9)
    
    # Crear una nueva imagen cuadrada para contener todas las imágenes
    tamanio_final = tamanio_img[0] * lado_cuadrado
    nueva_imagen = Image.new('RGB', (tamanio_final, tamanio_final))

    # Pegar las imágenes en la cuadrícula
    for i, img in enumerate(imagenes_abiertas):
        fila = i // lado_cuadrado
        columna = i % lado_cuadrado
        posicion = (columna * tamanio_img[0], fila * tamanio_img[1])
        nueva_imagen.paste(img, posicion)

    # Guardar la imagen final
    nueva_imagen.save("imagen_unida_81.png")
    nueva_imagen.show()

# Lista de rutas de las 81 imágenes cuadradas
# imagenes = [f"imagen{i+1}.png" for i in range(81)]  # Ejemplo: ['imagen1.png', 'imagen2.png', ..., 'imagen81.png']
imagenes = ["5_Saramago.png" for i in range(81)] 

unir_imagenes(imagenes)