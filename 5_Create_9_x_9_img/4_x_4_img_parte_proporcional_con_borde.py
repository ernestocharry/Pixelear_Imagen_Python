from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import math

# Ruta de la imagen original y la ruta de salida
folder_loc = '/Users/charrypastrana/Documents/github/Pixelear_Imagen_Python/'
folder_loc += '0_sources_and_results'
os.chdir(folder_loc)

def unir_imagenes_por_partes(imagenes, tamaño_borde=5, color_borde=(0, 0, 0), espacio_ejes=00):
    # Asegurarnos de que haya 16 imágenes
    assert len(imagenes) == 4, "Se requieren exactamente 16 imágenes."
    
    # Abrir las 16 imágenes
    imagenes_abiertas = [Image.open(img) for img in imagenes]
    
    # Verificar que todas las imágenes sean del mismo tamaño
    tamanio_img = imagenes_abiertas[0].size
    for img in imagenes_abiertas:
        assert img.size == tamanio_img, "Todas las imágenes deben ser del mismo tamaño y cuadradas."
    
    # Definir el tamaño de la cuadrícula (4x4)
    lado_cuadrado = 2  # 4 filas por 4 columnas
    
    # Calcular el tamaño proporcional de cada sección (tomaremos una parte de cada imagen)
    seccion_ancho = tamanio_img[0] // lado_cuadrado
    seccion_alto = tamanio_img[1] // lado_cuadrado
    
    # Crear una nueva imagen cuadrada final
    # Crear una nueva imagen cuadrada final
    tamanio_final = (seccion_ancho * lado_cuadrado + tamaño_borde * (lado_cuadrado + 0)+ espacio_ejes,
                     seccion_alto * lado_cuadrado + tamaño_borde * (lado_cuadrado + 0)+ espacio_ejes)
    tamanio_final_y = seccion_alto * lado_cuadrado + tamaño_borde * (lado_cuadrado +0)+ espacio_ejes
    nueva_imagen = Image.new('RGB', tamanio_final, color=(255, 255, 255))  # Fondo blanco

    # Recorrer cada imagen y recortar la parte proporcional según su ubicación final en la cuadrícula
    for i, img in enumerate(imagenes_abiertas):
        fila = i // lado_cuadrado  # Posición en la fila (0 a 3)
        columna = i % lado_cuadrado  # Posición en la columna (0 a 3)
        
        # Calcular las coordenadas de recorte para la imagen original
        left = columna * seccion_ancho
        upper = fila * seccion_alto
        right = left + seccion_ancho
        lower = upper + seccion_alto
        
        # Recortar la parte de la imagen que corresponde a su ubicación en la cuadrícula
        parte = img.crop((left, upper, right, lower))
        
                # Añadir bordes a la parte recortada
        parte_con_borde = ImageOps.expand(parte, border=tamaño_borde, fill=color_borde)
        
        # Pegar la parte recortada con borde en la imagen final
        x_offset = columna * (seccion_ancho + tamaño_borde) - 0*tamaño_borde+ espacio_ejes
        y_offset = fila * (seccion_alto + tamaño_borde) - 0*tamaño_borde
        nueva_imagen.paste(parte_con_borde, (x_offset, y_offset))


    # Guardar la imagen final
    nueva_imagen.save("imagen_unida_4_partes_con_borde.png")
    nueva_imagen.show()


# Lista de rutas de las 81 imágenes cuadradas
imagenes = [f"{i+1}.png" for i in range(4)]   # Ejemplo: ['imagen1.png', ..., 'imagen81.png']
#imagenes = ["5_Saramago.png" for i in range(16)] 

unir_imagenes_por_partes(imagenes)