from PIL import Image, ImageDraw, ImageFont, ImageOps

'''
Code copy - paste from ChatGPT
In order to create a instax efect in a photo. 
'''

# Función para dividir el texto en líneas que encajen dentro de un ancho dado
def dividir_texto(draw, texto, font, max_width):
    palabras = texto.split(' ')
    lineas = []
    linea_actual = []
    
    for palabra in palabras:
        linea_actual.append(palabra)
        linea_ancho = draw.textlength(' '.join(linea_actual), font=font)
        if linea_ancho > max_width:
            linea_actual.pop()  # Sacar la última palabra
            lineas.append(' '.join(linea_actual))
            linea_actual = [palabra]
    
    if linea_actual:
        lineas.append(' '.join(linea_actual))
    
    return lineas

def create_blank_img_with_text(width, height): 
    image = Image.new("RGB", (width, height), "white")

    # Crear un objeto para dibujar en la imagen
    draw = ImageDraw.Draw(image)

    # Cargar una fuente estilo periódico (serif)
    # Puedes usar una fuente como "Times New Roman" o alguna fuente serif descargada
    font_path = "RobotoCondensed-VariableFont_wght.ttf"  # Cambia por la ruta a tu fuente
    font = ImageFont.truetype(font_path, 100)

    # Texto simulado de periódico
    f = open('texto_song.txt')
    yourList = f.read() 
    texto = yourList.replace("\n", " ")
    texto = texto + " " + texto + " " + texto + " " + texto + " " + texto  
    print(texto)

    # Definir columnas y márgenes
    columnas = 1
    margen = 10
    espacio_entre_columnas = 40
    column_width = (width - (margen * 2) - espacio_entre_columnas) // columnas
    line_height = 100
    #line_height = font.getsize(texto)[1] + 10  # Espaciado entre líneas


    # Crear el texto en columnas
    y_offset = margen
    for i in range(columnas):
        x_offset = margen + i * (column_width + espacio_entre_columnas)
        texto_lineas = dividir_texto(draw, texto, font, column_width)
        
        for linea in texto_lineas:
            if y_offset + line_height >= height - margen:
                break
            text_width = draw.textlength(linea, font=font)
            x_offset = (width - text_width) // 2  # Cálculo para centrar horizontalmente
            draw.text((x_offset, y_offset), linea, font=font, fill="#eeeeee")
            y_offset += line_height

    # Añadir borde a la imagen para darle aspecto de periódico
    image = ImageOps.expand(image, border=20, fill="black")
    return image

def modificar_imagen(imagen_path, 
                     salida_path, 
                     tamaño_cuadrado, 
                     tamaño_borde, 
                     texto
                     ):
    '''
    This function create a white board arount a picture with a square size 
    with a text in the lower part.
    '''
    
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
    imagen_con_borde = Image.new('RGB', 
                                 (tamaño_cuadrado + 2 * tamaño_borde, 
                                  tamaño_cuadrado + 2 * tamaño_borde), 
                                  (255, 255, 255)
                                  )
    imagen_con_borde = create_blank_img_with_text(
                                            tamaño_cuadrado + 2 * tamaño_borde, 
                                            tamaño_cuadrado + 2 * tamaño_borde
                                            )
    imagen_con_borde.paste(imagen_cuadrada, (tamaño_borde, tamaño_borde))

    # Añadir texto a la imagen
    draw = ImageDraw.Draw(imagen_con_borde)
    try:
        # Usa una fuente TrueType
        fuente = ImageFont.truetype("QEDaveMergens.ttf", 200)  
    except IOError:
        print("load error")
        # Fuente predeterminada si no se encuentra la especificada
        fuente = ImageFont.load_default()  

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
    imagen_con_borde.show()
    print(f'Imagen guardada en {salida_path}')

# Ruta de la imagen original y la ruta de salida
imagen_path = 'example.png'
salida_path = 'example_instax_modificada.png'

# Modificar la imagen para que tenga formato Instax
tamaño_cuadrado=3024
tamaño_borde=500
texto='I used to scream ferociously, 3'

modificar_imagen(imagen_path, salida_path, tamaño_cuadrado, tamaño_borde, 
                 texto)