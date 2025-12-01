import cv2
import numpy as np
import skimage
from skimage.util import random_noise
from skimage.metrics import mean_squared_error, peak_signal_noise_ratio
import matplotlib.pyplot as plt

# --- Setup: Carregamento e Configuração ---

# ATENÇÃO: Altere os caminhos abaixo para suas imagens
PATH_ROSTO = 'rosto.jpg'
PATH_PAISAGEM = 'Paisagem.jpg'
PATH_URBANA = 'Cena_Urbana.jpg'
PATH_DOCUMENTO = 'texto.jpg'

# Carrega as imagens em escala de cinza
img_rosto = cv2.imread(PATH_ROSTO, cv2.IMREAD_GRAYSCALE)
img_paisagem = cv2.imread(PATH_PAISAGEM, cv2.IMREAD_GRAYSCALE)
img_urbana = cv2.imread(PATH_URBANA, cv2.IMREAD_GRAYSCALE)
img_documento = cv2.imread(PATH_DOCUMENTO, cv2.IMREAD_GRAYSCALE)

# Verificação
if img_rosto is None or img_paisagem is None or img_urbana is None or img_documento is None:
    print("Erro: Uma ou mais imagens não foram carregadas.")
    print("Verifique os caminhos (PATH_...) no início do script.")
    # Cria imagens de placeholder se falhar, apenas para o código não quebrar
    img_rosto = np.random.randint(0, 256, (256, 256), dtype=np.uint8)
    img_paisagem = np.random.randint(0, 256, (256, 256), dtype=np.uint8)
    img_urbana = np.random.randint(0, 256, (256, 256), dtype=np.uint8)
    img_documento = np.random.randint(0, 256, (256, 256), dtype=np.uint8)

# Define uma imagem padrão para os testes
img = img_rosto

print("--- Início do Processamento da Atividade Prática 02 ---")

# --- Etapa (a) Convolução Manual [cite: 14] ---

print("Executando Etapa (a): Convolução Manual...")

# Kernel de Média 3x3
kernel_media_3x3 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype=np.float32) / 9.0
img_media_manual = cv2.filter2D(img, -1, kernel_media_3x3)

# Kernel Laplaciano 3x3 (4-vizinhança)
kernel_laplaciano_3x3 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float32)
img_laplaciano_manual = cv2.filter2D(img, cv2.CV_64F, kernel_laplaciano_3x3)
img_laplaciano_visual = cv2.convertScaleAbs(img_laplaciano_manual)

# Plotagem (a)
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(img_media_manual, cmap='gray')
plt.title("Convolução Manual: Média 3x3")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(img_laplaciano_visual, cmap='gray')
plt.title("Convolução Manual: Laplaciano")
plt.axis('off')
plt.show()

# --- Etapa (b) Suavização [cite: 16] ---

print("Executando Etapa (b): Suavização...")

# i. Média [cite: 17]
img_media_3x3 = cv2.blur(img, (3, 3))
img_media_5x5 = cv2.blur(img, (5, 5))
img_media_7x7 = cv2.blur(img, (7, 7))

# Plotagem (b.i)
plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(img_media_3x3, cmap='gray')
plt.title("Filtro de Média 3x3")
plt.axis('off')
plt.subplot(2, 2, 3)
plt.imshow(img_media_5x5, cmap='gray')
plt.title("Filtro de Média 5x5")
plt.axis('off')
plt.subplot(2, 2, 4)
plt.imshow(img_media_7x7, cmap='gray')
plt.title("Filtro de Média 7x7")
plt.axis('off')
plt.suptitle("Comparação: Filtro de Média", fontsize=16)
plt.show()

# ii. Gaussiano [cite: 18]
img_gaussiano_s0_8 = cv2.GaussianBlur(img, (5, 5), 0.8)
img_gaussiano_s1_6 = cv2.GaussianBlur(img, (5, 5), 1.6)

# Plotagem (b.ii)
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(img_gaussiano_s0_8, cmap='gray')
plt.title("Gaussiano (k=5, $\sigma=0.8$)")
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(img_gaussiano_s1_6, cmap='gray')
plt.title("Gaussiano (k=5, $\sigma=1.6$)")
plt.axis('off')
plt.suptitle("Comparação: Filtro Gaussiano", fontsize=16)
plt.show()

# iii. Mediana [cite: 19]
img_mediana_3x3 = cv2.medianBlur(img, 3)
img_mediana_5x5 = cv2.medianBlur(img, 5)
img_mediana_7x7 = cv2.medianBlur(img, 7)

# Plotagem (b.iii)
plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(img_mediana_3x3, cmap='gray')
plt.title("Filtro de Mediana 3x3")
plt.axis('off')
plt.subplot(2, 2, 3)
plt.imshow(img_mediana_5x5, cmap='gray')
plt.title("Filtro de Mediana 5x5")
plt.axis('off')
plt.subplot(2, 2, 4)
plt.imshow(img_mediana_7x7, cmap='gray')
plt.title("Filtro de Mediana 7x7")
plt.axis('off')
plt.suptitle("Comparação: Filtro de Mediana", fontsize=16)
plt.show()

# --- Etapa (c) Realce/Nitidez [cite: 22] ---

print("Executando Etapa (c): Realce/Nitidez...")

# i. Unsharp Masking [cite: 23]
img_blur = cv2.GaussianBlur(img, (5, 5), 1.0)
mask = cv2.subtract(img, img_blur)
img_unsharp = cv2.add(img, mask)

# ii. High Boost [cite: 24]
k = 2.5
img_highboost = cv2.addWeighted(img, 1.0 + k, img_blur, -k, 0)

# iii. Laplaciano (kernel único para realce) [cite: 25]
kernel_laplaciano_realce = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
img_laplaciano_realce = cv2.filter2D(img, -1, kernel_laplaciano_realce)

# Plotagem (c)
plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(img_unsharp, cmap='gray')
plt.title("Unsharp Masking")
plt.axis('off')
plt.subplot(2, 2, 3)
plt.imshow(img_highboost, cmap='gray')
plt.title("High Boost (k=2.5)")
plt.axis('off')
plt.subplot(2, 2, 4)
plt.imshow(img_laplaciano_realce, cmap='gray')
plt.title("Realce Laplaciano")
plt.axis('off')
plt.suptitle("Comparação: Filtros de Realce/Nitidez", fontsize=16)
plt.show()

# --- Etapa (d) Bordas/Gradiente [cite: 26] ---

print("Executando Etapa (d): Bordas/Gradiente...")

# i. Sobel
grad_x_sobel = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
grad_y_sobel = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
grad_sobel = cv2.magnitude(grad_x_sobel, grad_y_sobel)
img_sobel = cv2.convertScaleAbs(grad_sobel)

# i. Prewitt
kernel_prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
kernel_prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)
grad_x_prewitt = cv2.filter2D(img, cv2.CV_64F, kernel_prewitt_x)
grad_y_prewitt = cv2.filter2D(img, cv2.CV_64F, kernel_prewitt_y)
grad_prewitt = cv2.magnitude(grad_x_prewitt, grad_y_prewitt)
img_prewitt = cv2.convertScaleAbs(grad_prewitt)

# i. Otsu (Limiarização, não detector de borda)
otsu_threshold, img_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# ii. Canny (opcional) [cite: 29]
img_canny = cv2.Canny(img, 100, 200)

# Plotagem (d)
plt.figure(figsize=(15, 10))
plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')
plt.subplot(2, 3, 2)
plt.imshow(img_sobel, cmap='gray')
plt.title("Sobel")
plt.axis('off')
plt.subplot(2, 3, 3)
plt.imshow(img_prewitt, cmap='gray')
plt.title("Prewitt")
plt.axis('off')
plt.subplot(2, 3, 4)
plt.imshow(img_otsu, cmap='gray')
plt.title(f"Limiar de Otsu (T={otsu_threshold})")
plt.axis('off')
plt.subplot(2, 3, 5)
plt.imshow(img_canny, cmap='gray')
plt.title("Canny (Ref.)")
plt.axis('off')
plt.suptitle("Comparação: Detectores de Borda/Limiar", fontsize=16)
plt.show()

# --- Etapa (e) Ruído + Filtro Adequado [cite: 30] ---

print("Executando Etapa (e): Ruído e Filtros...")

# Converte a imagem para float (0-1) para o scikit-image
img_float = skimage.util.img_as_float(img)

# i. Adiciona Ruídos [cite: 31]
sigma_gauss = 10.0 / 255.0 # Assumindo 10 em escala 0-255
img_ruido_gauss = random_noise(img_float, mode='gaussian', mean=0, var=sigma_gauss**2)
img_ruido_sp_5 = random_noise(img_float, mode='s&p', amount=0.05)

# Converte de volta para 8-bit (0-255)
img_ruido_gauss_8bit = skimage.util.img_as_ubyte(img_ruido_gauss)
img_ruido_sp_5_8bit = skimage.util.img_as_ubyte(img_ruido_sp_5)

# ii. Avalia filtros no Ruído Gaussiano
img_gauss_filtrada_media = cv2.blur(img_ruido_gauss_8bit, (5, 5))
img_gauss_filtrada_gauss = cv2.GaussianBlur(img_ruido_gauss_8bit, (5, 5), 1.0)
img_gauss_filtrada_mediana = cv2.medianBlur(img_ruido_gauss_8bit, 5)

# iii. Métricas para Ruído Gaussiano [cite: 33]
psnr_g_media = peak_signal_noise_ratio(img, img_gauss_filtrada_media)
psnr_g_gauss = peak_signal_noise_ratio(img, img_gauss_filtrada_gauss)
psnr_g_mediana = peak_signal_noise_ratio(img, img_gauss_filtrada_mediana)

# Plotagem (e.1) - Ruído Gaussiano
plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1)
plt.imshow(img_ruido_gauss_8bit, cmap='gray')
plt.title("Ruído Gaussiano ($\sigma=10$)")
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(img_gauss_filtrada_media, cmap='gray')
plt.title(f"Filtro Média (PSNR: {psnr_g_media:.2f} dB)")
plt.axis('off')
plt.subplot(2, 2, 3)
plt.imshow(img_gauss_filtrada_gauss, cmap='gray')
plt.title(f"Filtro Gaussiano (PSNR: {psnr_g_gauss:.2f} dB)")
plt.axis('off')
plt.subplot(2, 2, 4)
plt.imshow(img_gauss_filtrada_mediana, cmap='gray')
plt.title(f"Filtro Mediana (PSNR: {psnr_g_mediana:.2f} dB)")
plt.axis('off')
plt.suptitle("Análise: Filtros em Ruído Gaussiano", fontsize=16)
plt.show()

# ii. Avalia filtros no Ruído Sal e Pimenta
img_sp_filtrada_media = cv2.blur(img_ruido_sp_5_8bit, (5, 5))
img_sp_filtrada_gauss = cv2.GaussianBlur(img_ruido_sp_5_8bit, (5, 5), 1.0)
img_sp_filtrada_mediana = cv2.medianBlur(img_ruido_sp_5_8bit, 5)

# iii. Métricas para Ruído S&P [cite: 33]
psnr_sp_media = peak_signal_noise_ratio(img, img_sp_filtrada_media)
psnr_sp_gauss = peak_signal_noise_ratio(img, img_sp_filtrada_gauss)
psnr_sp_mediana = peak_signal_noise_ratio(img, img_sp_filtrada_mediana)

# Plotagem (e.2) - Ruído Sal e Pimenta
plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1)
plt.imshow(img_ruido_sp_5_8bit, cmap='gray')
plt.title("Ruído Sal e Pimenta (5%)")
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(img_sp_filtrada_media, cmap='gray')
plt.title(f"Filtro Média (PSNR: {psnr_sp_media:.2f} dB)")
plt.axis('off')
plt.subplot(2, 2, 3)
plt.imshow(img_sp_filtrada_gauss, cmap='gray')
plt.title(f"Filtro Gaussiano (PSNR: {psnr_sp_gauss:.2f} dB)")
plt.axis('off')
plt.subplot(2, 2, 4)
plt.imshow(img_sp_filtrada_mediana, cmap='gray')
plt.title(f"Filtro Mediana (PSNR: {psnr_sp_mediana:.2f} dB)")
plt.axis('off')
plt.suptitle("Análise: Filtros em Ruído Sal e Pimenta", fontsize=16)
plt.show()

# iv. Relatório [cite: 34]
print("\n--- Resultados (e) ---")
print(f"PSNR (Gauss): Média={psnr_g_media:.2f}, Gauss={psnr_g_gauss:.2f}, Mediana={psnr_g_mediana:.2f}")
print(f"PSNR (S&P 5%): Média={psnr_sp_media:.2f}, Gauss={psnr_sp_gauss:.2f}, Mediana={psnr_sp_mediana:.2f}")
if psnr_g_gauss > psnr_g_media and psnr_g_gauss > psnr_g_mediana:
    print("-> Filtro Gaussiano venceu para Ruído Gaussiano.")
if psnr_sp_mediana > psnr_sp_media and psnr_sp_mediana > psnr_sp_gauss:
    print("-> Filtro Mediana venceu para Ruído Sal e Pimenta.")


# --- Etapa (f) Mini-estudo: kernel, borda, métrica [cite: 35] ---
# O objetivo aqui é gerar a tabela.
# A plotagem é apenas uma evidência visual do efeito das bordas.

print("\nExecutando Etapa (f): Mini-estudo (Efeito das Bordas)...")

# Escolhe a imagem de documento
img_teste_bordas = img_documento

# Aplica o filtro (ex: Média 9x9) com 3 tratamentos de borda
k = 9
img_borda_zero = cv2.blur(img_teste_bordas, (k, k), borderType=cv2.BORDER_CONSTANT)
img_borda_replicar = cv2.blur(img_teste_bordas, (k, k), borderType=cv2.BORDER_REPLICATE)
img_borda_espelhar = cv2.blur(img_teste_bordas, (k, k), borderType=cv2.BORDER_REFLECT_101)

# Plotagem (f) - Efeito do tratamento de borda
plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1)
plt.imshow(img_teste_bordas, cmap='gray')
plt.title("Documento Original")
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(img_borda_zero, cmap='gray')
plt.title(f"Borda: Zero (CONSTANT) - k={k}")
plt.axis('off')
plt.subplot(2, 2, 3)
plt.imshow(img_borda_replicar, cmap='gray')
plt.title(f"Borda: Replicar (REPLICATE) - k={k}")
plt.axis('off')
plt.subplot(2, 2, 4)
plt.imshow(img_borda_espelhar, cmap='gray')
plt.title(f"Borda: Espelhar (REFLECT_101) - k={k}")
plt.axis('off')
plt.suptitle("Análise: Efeito do Tratamento de Borda", fontsize=16)
plt.show()

# (Para as métricas, você deve rodar os cálculos e anotar na sua tabela)
print("\nPara a tabela da Etapa (f):")
print("Execute os cálculos de métrica (contraste/nitidez) em cada imagem gerada")
print("e anote os resultados no seu relatório.")

print("\n--- Fim do Processamento ---")