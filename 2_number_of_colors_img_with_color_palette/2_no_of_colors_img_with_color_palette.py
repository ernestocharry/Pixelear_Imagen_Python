import os
import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


# -----------------------------
# PALETA FIJA (HEX → RGB)
# -----------------------------
colors_hex = [
    "#FCD116",  # Amarillo bandera
    "#0038A8",  # Azul bandera
    "#CE1126",  # Rojo bandera
    "#32CD32",  # Verde
    "#FF8C00",  # Naranja
    "#8A2BE2",  # Violeta
    "#E5E5E5",  # Gris claro
    "#2B2B2B"   # Gris carbón
]

palette = np.array([
    tuple(int(color[i:i+2], 16) for i in (1,3,5))
    for color in colors_hex
])


# -----------------------------
# FUNCIÓN: COLOR MÁS CERCANO
# -----------------------------
def closest_color(pixel, palette):
    distances = np.sqrt(np.sum((palette - pixel)**2, axis=1))
    return np.argmin(distances)


# -----------------------------
# FLOYD–STEINBERG DITHERING
# -----------------------------
def floyd_steinberg_dither(image, palette):
    h, w, _ = image.shape
    dithered = image.astype(np.float32).copy()

    for y in range(h):
        for x in range(w):
            old_pixel = dithered[y, x]
            
            # encontrar el color más cercano de la paleta
            idx = closest_color(old_pixel, palette)
            new_pixel = palette[idx]

            dithered[y, x] = new_pixel
            
            # error = pixel original - pixel nuevo
            error = old_pixel - new_pixel

            # Distribución Floyd–Steinberg
            if x + 1 < w:
                dithered[y, x+1] += error * (7/16)
            if y + 1 < h and x > 0:
                dithered[y+1, x-1] += error * (3/16)
            if y + 1 < h:
                dithered[y+1, x] += error * (5/16)
            if y + 1 < h and x + 1 < w:
                dithered[y+1, x+1] += error * (1/16)

    # limitar valores válidos
    return np.clip(dithered, 0, 255).astype(np.uint8)



# -----------------------------
# CONFIGURACIÓN DE RUTAS
# -----------------------------
print(os.getcwd())

folder_loc = '/Users/charrypastrana/Documents/github/'  # Mac
folder_loc = '/Users/felix/Documents/github/'            # Windows

folder_loc += 'pixelear_imagen/0_sources_and_results'
os.chdir(folder_loc)

files = ['IMG_7773.png', 'IMG_0266.JPEG', 'IMG_3358.JPEG', 'Coca.jpg']


# -----------------------------
# PROCESAMIENTO PRINCIPAL
# -----------------------------
for file_name in files:
    
    file_extention = file_name[file_name.find('.'):]
    
    image = cv2.imread(file_name)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    pixels = image.reshape(-1, 3)

    for i in [2, 3, 4, 5, 6, 7, 8]:

        print(f"Procesando {file_name} con {i} clusters...")

        # ========================
        # 1. K-MEANS
        # ========================
        num_clusters = i
        kmeans = KMeans(n_clusters=num_clusters)
        kmeans.fit(pixels)

        centers = kmeans.cluster_centers_
        labels = kmeans.labels_

        segmented_image = centers[labels].reshape(image.shape).astype(np.uint8)

        # ========================
        # 2. REEMPLAZAR CENTROIDES POR LA PALETA
        # ========================
        new_centers = np.zeros_like(centers)
        for idx, c in enumerate(centers):
            nearest_idx = closest_color(c, palette)
            new_centers[idx] = palette[nearest_idx]

        final_pixels = new_centers[labels]
        final_image = final_pixels.reshape(image.shape).astype(np.uint8)

        # ========================
        # 3. APLICAR DITHERING FLOYD–STEINBERG
        # ========================
        print("Aplicando dithering Floyd–Steinberg...")
        dithered_image = floyd_steinberg_dither(final_image, palette)

        # -----------------------------
        # 4. GUARDAR RESULTADO
        # -----------------------------
        if i < 10:
            color_section = '_NoOfColors_0'
        else:
            color_section = '_NoOfColors_'

        out_name = file_name.replace(
            file_extention,
            color_section + str(num_clusters) + "_PaletteColombia_FS" + file_extention
        )

        plt.imsave(out_name, dithered_image)
        print(f"✔ Guardado con dithering: {out_name}")
