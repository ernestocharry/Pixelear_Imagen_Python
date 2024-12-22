from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import math

# Ruta de la imagen original y la ruta de salida
folder_loc = '/Users/charrypastrana/Documents/github/Pixelear_Imagen_Python/'
folder_loc += '0_sources_and_results'
os.chdir(folder_loc)

from PIL import Image

def unir_imagenes_por_partes(imagenes):
    # Asegurarnos de que haya 81 imágenes
    assert len(imagenes) == 81, "Se requieren exactamente 81 imágenes."
    
    # Abrir las 81 imágenes
    imagenes_abiertas = [Image.open(img) for img in imagenes]
    
    # Verificar que todas las imágenes sean del mismo tamaño
    tamanio_img = imagenes_abiertas[0].size
    for img in imagenes_abiertas:
        assert img.size == tamanio_img, "Todas las imágenes deben ser del mismo tamaño y cuadradas."
    
    # Definir el tamaño de la cuadrícula (9x9)
    lado_cuadrado = 9  # 9 filas por 9 columnas
    
    # Calcular el tamaño proporcional de cada sección (tomaremos una parte de cada imagen)
    seccion_ancho = tamanio_img[0] // lado_cuadrado
    seccion_alto = tamanio_img[1] // lado_cuadrado
    
    # Crear una nueva imagen cuadrada final
    tamanio_final = (seccion_ancho * lado_cuadrado, seccion_alto * lado_cuadrado)
    nueva_imagen = Image.new('RGB', tamanio_final)
    
    # Recorrer cada imagen y recortar la parte proporcional según su ubicación final en la cuadrícula
    for i, img in enumerate(imagenes_abiertas):
        fila = i // lado_cuadrado  # Posición en la fila (0 a 8)
        columna = i % lado_cuadrado  # Posición en la columna (0 a 8)
        
        # Calcular las coordenadas de recorte para la imagen original
        left = columna * seccion_ancho
        upper = fila * seccion_alto
        right = left + seccion_ancho
        lower = upper + seccion_alto
        
        # Recortar la parte de la imagen que corresponde a su ubicación en la cuadrícula
        parte = img.crop((left, upper, right, lower))
        
        # Pegar la parte recortada en la imagen final
        nueva_imagen.paste(parte, (columna * seccion_ancho, fila * seccion_alto))

    # Guardar la imagen final
    nueva_imagen.save("imagen_unida_81_partes_segun_posicion.png")
    nueva_imagen.show()


# Lista de rutas de las 81 imágenes cuadradas
#imagenes = [f"imagen{i+1}.png" for i in range(81)]  # Ejemplo: ['imagen1.png', ..., 'imagen81.png']

imagenes = ["5_Saramago.png" for i in range(81)] 

unir_imagenes_por_partes(imagenes)