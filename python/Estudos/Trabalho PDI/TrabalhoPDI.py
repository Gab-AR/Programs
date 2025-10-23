import cv2
import numpy as np
import matplotlib.pyplot as plt

IMAGEM_ORIGINAL_PATH = 'einstein.jpg'
IMAGEM_REFERENCIA_PATH = 'lena_gray.bmp'

def carregar_e_converter(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Erro: Arquivo não encontrado em {path}")
    return img

def calcular_histograma(img):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    return hist

def plotar_histograma(hist, title='Histograma de Intensidades', ax=None, color='gray'):
    if ax is None:
        fig, ax = plt.subplots(1, 1)
    ax.plot(hist, color=color)
    ax.set_title(title)
    ax.set_xlabel('Intensidade (0-255)')
    ax.set_ylabel('Frequência (Contagem de Pixels)')
    ax.set_xlim([0, 256])
    return ax

# =========================================================================
# PASSO 1 - Leitura e Análise da Imagem
# =========================================================================
print("--- Passo 1: Leitura e Análise da Imagem ---")

try:
    img_original = carregar_e_converter(IMAGEM_ORIGINAL_PATH)
    hist_original = calcular_histograma(img_original)
    
    # Exibição
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(img_original, cmap='gray')
    plt.title('1. Imagem Original')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plotar_histograma(hist_original, title='Histograma da Imagem Original')
    
    plt.tight_layout()
    plt.show()
    print("Passo 1 concluído.")
    
except FileNotFoundError as e:
    print(e)
    exit()

# =========================================================================
# PASSO 2 - Equalização do Histograma
# =========================================================================
print("\n--- Passo 2: Equalização do Histograma ---")

img_equalizada = cv2.equalizeHist(img_original)

hist_equalizada = calcular_histograma(img_equalizada)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].imshow(img_original, cmap='gray')
axes[0, 0].set_title('2a. Imagem Original')
axes[0, 0].axis('off')

axes[0, 1].imshow(img_equalizada, cmap='gray')
axes[0, 1].set_title('2b. Imagem Equalizada')
axes[0, 1].axis('off')

axes[1, 0].plot(hist_original, color='blue', label='Original')
axes[1, 0].plot(hist_equalizada, color='red', label='Equalizada')
axes[1, 0].set_title('2c. Histogramas Comparativos')
axes[1, 0].set_xlabel('Intensidade (0-255)')
axes[1, 0].set_ylabel('Frequência')
axes[1, 0].legend()
axes[1, 0].set_xlim([0, 256])

plotar_histograma(hist_equalizada, title='2d. Histograma da Equalizada', ax=axes[1, 1], color='red')

plt.tight_layout()
plt.show()


print("Passo 2 concluído.")


# =========================================================================
# PASSO 3 - Especificação do Histograma (Histogram Matching)
# =========================================================================
print("\n--- Passo 3: Especificação do Histograma ---")

try:
    img_referencia = carregar_e_converter(IMAGEM_REFERENCIA_PATH)
    hist_referencia = calcular_histograma(img_referencia)
    
    def especificacao_histograma(img_src, img_ref):
        hist_src, bins = np.histogram(img_src.flatten(), 256, [0, 256])
        cdf_src = hist_src.cumsum()
        cdf_src_norm = cdf_src * 255 / cdf_src.max()

        hist_ref, bins = np.histogram(img_ref.flatten(), 256, [0, 256])
        cdf_ref = hist_ref.cumsum()
        cdf_ref_norm = cdf_ref * 255 / cdf_ref.max()

        tabela_mapeamento = np.zeros(256, dtype=np.uint8)
        for i in range(256):
            j = 0
            while j < 256 and cdf_ref_norm[j] < cdf_src_norm[i]:
                j += 1
            tabela_mapeamento[i] = j
        
        img_resultante = tabela_mapeamento[img_src]
        return img_resultante

    img_resultante = especificacao_histograma(img_original, img_referencia)
    hist_resultante = calcular_histograma(img_resultante)

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))

    axes[0, 0].imshow(img_original, cmap='gray'); axes[0, 0].set_title('3a. Imagem Original'); axes[0, 0].axis('off')
    axes[0, 1].imshow(img_referencia, cmap='gray'); axes[0, 1].set_title('3b. Imagem Referência'); axes[0, 1].axis('off')
    axes[0, 2].imshow(img_resultante, cmap='gray'); axes[0, 2].set_title('3c. Imagem Resultante (Especificada)'); axes[0, 2].axis('off')

    plotar_histograma(hist_original, title='3d. Histograma Original', ax=axes[1, 0])
    plotar_histograma(hist_referencia, title='3e. Histograma Referência', ax=axes[1, 1], color='green')
    plotar_histograma(hist_resultante, title='3f. Histograma Resultante', ax=axes[1, 2], color='orange')

    plt.tight_layout()
    plt.show()
    print("Passo 3 concluído.")
    
except FileNotFoundError as e:
    print(e)
    print("O Passo 3 foi ignorado devido à falta do arquivo de referência.")

print("\n-------------------------------------------------------------")
print("Próximo passo: Responder as questões da Análise Crítica (Passo 4) e compilar o Relatório (PDF).")