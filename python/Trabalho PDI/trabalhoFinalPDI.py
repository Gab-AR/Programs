import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

def processamento_imagens_moedas():
    # --- 0. Carregar imagem de exemplo (direto da web para teste) ---
    # Usaremos uma imagem clássica de moedas ou células. Aqui, moedas.
    url = "https://upload.wikimedia.org/wikipedia/commons/d/da/NCI_Visuals_Food_Hamburger_%28cropped%29.jpg" 
    # Obs: O link acima é um exemplo. Para moedas ideais, use a imagem 'coins.jpg' do dataset do skimage 
    # ou uma foto local. Abaixo, simulo o carregamento de uma imagem de moedas via skimage para garantir que funcione.
    from skimage import data
    img_original = data.coins() # Imagem em escala de cinza nativa (uint8)
    
    # Se fosse uma imagem colorida carregada localmente:
    # img_original = cv2.imread('sua_foto_moedas.jpg')
    # img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
    
    # Como o dataset do skimage já vem em cinza, usamos direto:
    img_gray = img_original.copy()

    # =========================================================================
    # 1. PRÉ-PROCESSAMENTO
    # =========================================================================
    # Aplica Gaussian Blur para reduzir ruído de alta frequência (suavização)
    # Isso ajuda a não detectar texturas da moeda como bordas falsas.
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # =========================================================================
    # 2. SEGMENTAÇÃO
    # =========================================================================
    # Limiarização de Otsu: Encontra automaticamente o melhor valor para separar 
    # fundo e objeto (binarização).
    ret, thresh = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # =========================================================================
    # 3. OPERAÇÕES MORFOLÓGICAS
    # =========================================================================
    kernel = np.ones((3,3), np.uint8)

    # A) Remoção de Ruído (Abertura: Erosão seguida de Dilatação)
    # Remove pequenos pontos brancos no fundo.
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # B) Fechamento (Dilatação seguida de Erosão) - Opcional
    # Útil para fechar pequenos buracos DENTRO das moedas.
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)

    # C) Extração de Bordas (Gradiente Morfológico)
    # Diferença entre Dilatação e Erosão mostra apenas o contorno.
    morph_gradient = cv2.morphologyEx(closing, cv2.MORPH_GRADIENT, kernel)

    # D) Separação de Objetos Colados (Transformada de Distância + Watershed)
    # Para separar moedas que se tocam, precisamos encontrar o "centro" seguro de cada uma.
    
    # Área de fundo garantida (Dilatação aumenta a área do objeto, o que sobra é fundo)
    sure_bg = cv2.dilate(closing, kernel, iterations=3)
    
    # Área de frente garantida (Distance Transform)
    # Calcula a distância de cada pixel até o pixel zero mais próximo.
    dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 5)
    
    # Limiariza para pegar apenas os picos (centros das moedas)
    ret, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    
    # Região desconhecida (Borda entre moedas coladas)
    unknown = cv2.subtract(sure_bg, sure_fg)

    # Rotulação de componentes conectados (Labeling)
    ret, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1 # Adiciona 1 para que o fundo seja 1, não 0
    markers[unknown == 255] = 0 # Marca a região desconhecida com 0 para o Watershed

    # Aplica Watershed (algoritmo de inundação para segmentar)
    # Note: Watershed precisa da imagem colorida (3 canais) para desenhar, 
    # aqui converteremos a cinza para BGR apenas para visualização final.
    img_result = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
    markers = cv2.watershed(img_result, markers)
    
    # Pinta as bordas encontradas de vermelho
    img_result[markers == -1] = [0, 0, 255]

    # =========================================================================
    # 4. CONTAGEM E MEDIÇÃO
    # =========================================================================
    # Encontrar contornos na imagem binária processada ('sure_fg' ou 'closing')
    # Usaremos 'closing' para contagem geral, ou os labels do watershed.
    # Vamos usar os contornos da imagem 'closing' para medir área.
    contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    total_moedas = len(contours)
    
    # Classificação simples baseada na área
    pequenas = 0
    grandes = 0
    area_media_limiar = 2000 # Valor arbitrário, depende da resolução da imagem

    print(f"--- Relatório de Análise ---")
    print(f"Total de objetos detectados: {total_moedas}")
    
    img_final_visual = img_result.copy()
    
    for i, c in enumerate(contours):
        area = cv2.contourArea(c)
        # Ignora ruídos muito pequenos
        if area < 100: 
            continue
            
        if area < area_media_limiar:
            tipo = "Pequena"
            pequenas += 1
            color = (0, 255, 0) # Verde
        else:
            tipo = "Grande"
            grandes += 1
            color = (255, 0, 0) # Azul
            
        # Desenha contorno e texto
        cv2.drawContours(img_final_visual, [c], -1, color, 2)
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.putText(img_final_visual, f"#{i+1}", (cX - 20, cY), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    print(f"Classificação: {pequenas} pequenas, {grandes} grandes.")

    # =========================================================================
    # 5. GERAR RESULTADOS VISUAIS (PLOT)
    # =========================================================================
    titles = ['Original', 'Limiarização (Otsu)', 'Morfologia (Fechamento)', 
              'Bordas Morfológicas', 'Separador (Dist. Transform)', 'Resultado Final']
    images = [img_gray, thresh, closing, 
              morph_gradient, dist_transform, img_final_visual]

    plt.figure(figsize=(16, 8))
    for i in range(6):
        plt.subplot(2, 3, i+1)
        if i == 5: # A última imagem é colorida (BGR) -> Converter para RGB p/ Matplotlib
            plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
        elif i == 4: # Mapa de distância precisa de color map
            plt.imshow(images[i], cmap='jet')
        else:
            plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    processamento_imagens_moedas()