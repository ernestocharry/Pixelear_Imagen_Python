from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import math

# Ruta de la imagen original y la ruta de salida
folder_loc = '/Users/charrypastrana/Documents/github/Pixelear_Imagen_Python/'
folder_loc = '/Users/felix/Documents/github/Pixelear_Imagen_Python/'
folder_loc += '0_sources_and_results'
os.chdir(folder_loc)



def unir_imagenes_con_ejes(imagenes, tamaño_borde=0, color_borde=(0, 0, 0), espacio_ejes=00):
    # Abrir todas las imágenes
    imagenes_abiertas = [Image.open(img) for img in imagenes]
    
    # Verificar que todas las imágenes sean del mismo tamaño
    print( imagenes_abiertas[0].size)
    print( imagenes_abiertas[1].size)
    print( imagenes_abiertas[2].size)
    print( imagenes_abiertas[3].size)


    imagenes_abiertas[0] = imagenes_abiertas[0].resize(imagenes_abiertas[3].size)
    imagenes_abiertas[1] = imagenes_abiertas[1].resize(imagenes_abiertas[3].size)
    imagenes_abiertas[2] = imagenes_abiertas[2].resize(imagenes_abiertas[3].size)


    print( imagenes_abiertas[0].size)
    print( imagenes_abiertas[1].size)
    print( imagenes_abiertas[2].size)
    print( imagenes_abiertas[3].size)


    tamanio_img = imagenes_abiertas[0].size
    for img in imagenes_abiertas:
        assert img.size == tamanio_img, "Todas las imágenes deben ser del mismo tamaño y cuadradas."

    # Calcular el número de imágenes por fila/columna (9x9 en este caso)
    num_imagenes = len(imagenes_abiertas)
    lado_cuadrado = int(math.sqrt(num_imagenes))  # Lado de la cuadrícula (en este caso, 9)
    
    # Crear una nueva imagen cuadrada para contener todas las imágenes, incluyendo espacio para los ejes
    tamanio_final_x = (tamanio_img[0] + tamaño_borde * 2) * lado_cuadrado + espacio_ejes  # Espacio para el eje izquierdo
    tamanio_final_y = (tamanio_img[1] + tamaño_borde * 2) * lado_cuadrado + espacio_ejes  # Espacio para el eje inferior
    
    nueva_imagen = Image.new('RGB', (tamanio_final_x, tamanio_final_y), color=(255, 255, 255))  # Fondo blanco

    # Pegar las imágenes en la cuadrícula con espacio para los ejes
    for i, img in enumerate(imagenes_abiertas):
        # Añadir borde a la imagen
        img_con_borde = ImageOps.expand(img, border=tamaño_borde, fill=color_borde)
        
        fila = i // lado_cuadrado
        columna = i % lado_cuadrado
        posicion = (columna * (tamanio_img[0] + tamaño_borde * 2) + espacio_ejes,
                    fila * (tamanio_img[1] + tamaño_borde * 2))

        nueva_imagen.paste(img_con_borde, posicion)

            # Dibujar los ejes y las etiquetas
    draw = ImageDraw.Draw(nueva_imagen)

    if False: 
        # Fuente para los números (usaremos una fuente estándar del sistema)
        try:
            font_path = "cmu_serif-roman.ttf"  # Cambia por la ruta a tu fuente
            font = ImageFont.truetype(font_path, 80)
        except IOError:
            font = ImageFont.load_default()  # Si no está disponible, usar la fuente predeterminada
        
        # Dibujar las etiquetas del eje horizontal (en la parte inferior)
        # Dibujar las etiquetas del eje horizontal (en la parte inferior)
        for columna in range(lado_cuadrado):
            # Calcular la posición x en el centro de cada columna
            x_pos = espacio_ejes + columna * (tamanio_img[0] + tamaño_borde * 2) + (tamanio_img[0] + tamaño_borde * 2) // 2
            # Ajustar la posición y para centrar mejor el texto en el espacio inferior
            y_pos = tamanio_final_y - (espacio_ejes // 2) + 10  # Desplazamos un poco hacia abajo
            if columna == 0: 
                draw.text((x_pos, y_pos), '256 x 256 píxeles', fill="#444e0f", font=font, anchor="mm")     
            else:
                draw.text((x_pos, y_pos), '1024 x 1024 píxeles', fill="#444e0f", font=font, anchor="mm")
        
        # Dibujar las etiquetas personalizadas del eje vertical ("20 colores" y "4 colores")
        etiquetas_verticales = ["20 colores", "4 colores"]
        

        # Dibujar cada etiqueta del eje vertical
        for i, etiqueta in enumerate(etiquetas_verticales):
            # Crear una nueva imagen de texto para rotar
            text_img = Image.new('RGBA', (600, 160), (255, 255, 255, 0))  # Crear imagen para el texto
            text_draw = ImageDraw.Draw(text_img)
            
            # Dibujar la etiqueta
            text_draw.text((300, 80), etiqueta, fill="#444e0f", font=font, anchor="mm")
            
            # Rotar la imagen del texto 90 grados
            text_img_rotada = text_img.rotate(90, expand=1)
            
            # Calcular la posición centrada para las etiquetas en el eje vertical
            if i == 0:  # "20 colores" en la parte superior del eje vertical
                y_pos = (tamanio_final_y - espacio_ejes) // 4  # Centrado en el primer cuarto del eje
            else:  # "4 colores" en la parte inferior del eje vertical
                y_pos = (3 * (tamanio_final_y - espacio_ejes)) // 4  # Centrado en el tercer cuarto del eje

            # Pegar el texto rotado en la imagen principal
            nueva_imagen.paste(text_img_rotada, (espacio_ejes // 4 - 25, y_pos - text_img_rotada.size[1] // 2), text_img_rotada)

    # Guardar la imagen final
    nueva_imagen.save("imagen_unida_81_con_bordes_y_ejes.png")
    nueva_imagen.show()


# Lista de rutas de las 81 imágenes cuadradas
imagenes = [f"{i+1}.png" for i in range(4)]  # Ejemplo: ['imagen1.png', 'imagen2.png', ..., 'imagen81.png']
imagenes = ["DSC_0155_segmented_04.JPEG" for i in range(4)] 
imagenes = ['DSC_0155_pixe_1024_segmented_15.JPEG', 'DSC_0173_pixe_1024_segmented_12.JPEG', 'DSC_0193_pixe_1024_segmented_08.JPEG', 'DSC_0162_pixe_1024_segmented_08.JPEG'  ]
#imagenes = ["5_Saramago.png" for i in range(81)] 


unir_imagenes_con_ejes(imagenes)