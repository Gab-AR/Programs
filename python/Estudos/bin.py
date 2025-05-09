from PIL import Image
import numpy as np

# ESCOLHA o canal: 0 = R, 1 = G, 2 = B
CANAL = 0

# Abre a imagem como RGB
img = Image.open("Trabalho_ivan.jpg").convert("RGB")

# Redimensiona para 176x144 se necessário
img = img.resize((176, 144))

# Converte para numpy array (formato: altura x largura x 3)
pixels = np.array(img)

# Extrai o canal desejado e achata o array para 1D
canal_pixels = pixels[:, :, CANAL].flatten()

# Gera o vetor .byte para o RARS
with open("imagem_rars.asm", "w") as f:
    f.write(".data\n")
    f.write("imagem: .byte ")
    f.write(", ".join(str(p) for p in canal_pixels))
