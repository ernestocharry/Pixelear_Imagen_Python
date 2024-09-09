from PIL import Image, ImageDraw, ImageFont


def modificar_imagen(imagen_path, 
                     salida_path, 
                     tamaño_cuadrado=3024, 
                     tamaño_borde=500, 
                     texto='Felipe Camilo a cuatro colores'
                     ):
    
    # Abrir la imagen original
    imagen = Image.open(imagen_path)
    ancho, alto = imagen.size

    # Calcular el tamaño del recorte
    if ancho > alto:
        nuevo_ancho = alto
        izquierda = (ancho - nuevo_ancho) / 2
        derecha = ancho - (ancho - nuevo_ancho) / 2
        arriba = 0
        abajo = alto
    else:
        nuevo_alto = ancho
        arriba = (alto - nuevo_alto) / 2
        abajo = alto - (alto - nuevo_alto) / 2
        izquierda = 0
        derecha = ancho

    # Recortar la imagen a un formato cuadrado
    imagen_recortada = imagen.crop((izquierda, arriba, derecha, abajo))

    # Redimensionar la imagen al tamaño deseado
    imagen_cuadrada = imagen_recortada.resize((tamaño_cuadrado, tamaño_cuadrado))

    # Crear una nueva imagen con borde blanco
    imagen_con_borde = Image.new('RGB', (tamaño_cuadrado + 2 * tamaño_borde, tamaño_cuadrado + 2 * tamaño_borde), (255, 255, 255))
    imagen_con_borde.paste(imagen_cuadrada, (tamaño_borde, tamaño_borde))

    # Añadir texto a la imagen
    draw = ImageDraw.Draw(imagen_con_borde)
    try:
        fuente = ImageFont.truetype("QEDaveMergens.ttf", 200)  # Usa una fuente TrueType
    except IOError:
        print("load error")
        fuente = ImageFont.load_default()  # Fuente predeterminada si no se encuentra la especificada

    # Calcular la posición del texto
    print(texto)
    print(draw.textlength(texto, font=fuente))
    ancho_texto = draw.textlength(texto, font=fuente)
    x = (tamaño_cuadrado + 2 * tamaño_borde - ancho_texto) / 2
    y = tamaño_cuadrado + tamaño_borde + 120  # 10 píxeles debajo del borde

    # Dibujar el texto en la imagen
    draw.text((x, y), texto, font=fuente, fill=(0, 0, 0))

    # Guardar la imagen resultante
    imagen_con_borde.save(salida_path)
    print(f'Imagen guardada en {salida_path}')

# Ruta de la imagen original y la ruta de salida
imagen_path = 'IMG_6889_segmented_04.png'
salida_path = 'IMG_6889_imagen_instax_modificada.png'

# Modificar la imagen para que tenga formato Instax
modificar_imagen(imagen_path, salida_path)
