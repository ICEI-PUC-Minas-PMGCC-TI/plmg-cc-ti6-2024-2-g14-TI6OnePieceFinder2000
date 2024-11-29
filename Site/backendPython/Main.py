import cv2
import time
import os
from concurrent.futures import ThreadPoolExecutor
from skimage.metrics import structural_similarity as ssim
import ImageFinder
from PIL import Image

def get_lmdb_files(folder_path):
    return [f for f in os.listdir(folder_path) if f.endswith('.lmdb')]

def processar_episodios(imagem_path):
    finder = ImageFinder()

    # Caminho para a imagem do usuário, recebido via argumento
    imagem = cv2.imread(imagem_path)  # Usando o caminho da imagem enviada

    # Redimensionar para 20x15 e converter para tons de cinza
    imagem_cinza_20x15 = cv2.resize(imagem, (20, 15))
    imagem_cinza_20x15 = cv2.cvtColor(imagem_cinza_20x15, cv2.COLOR_BGR2GRAY)

    # Redimensionar para 40x30 mantendo as cores originais
    imagem_colorida_40x30 = cv2.resize(imagem, (40, 30))

    # Caminho para a pasta com arquivos lmdb
    folder_path = 'BasedeDados'

    lmdb_files = get_lmdb_files(folder_path)
    all_top_matches = []

    for lmdb_file in lmdb_files:
        episode_number = lmdb_file.split('_')[1].split('.')[0]
        lmdb_file_path = os.path.join(folder_path, lmdb_file)

        top_matches = finder.compare_images(imagem_cinza_20x15, lmdb_file_path)

        for score, filename in top_matches:
            all_top_matches.append((score, filename, episode_number))

    # Ordena todas as correspondências e pega as 100 melhores
    all_top_matches.sort(reverse=False, key=lambda x: x[0])
    top100_matches = all_top_matches[:100]

    print("As 100 imagens mais semelhantes são:")
    for score, filename, episode_number in top100_matches:
        print(f"{filename} do Episódio {episode_number} com PIXEL X PIXEL: {score:.4f}")

    start_time1 = time.time()
    ImagensUpscale = finder.upScaleTop100Images('EpFrames40x30', top100_matches)
    end_time1 = time.time()
    total_time1 = end_time1 - start_time1
    print(f"Tempo total de Upscale: {total_time1:.2f} segundos")

    top3 = finder.compare_imagesImgPaths(imagem_colorida_40x30, ImagensUpscale)

    print("As 3 imagens mais semelhantes são:")
    for score, filename, episodenumber in top3:
        print(f"{filename} com SSIM: {score:.4f} do Episódio {episodenumber}")

    # Extraindo o número do nome
    number_str = filename.split('_')[1].split('.')[0]  # Divide pelo '_' e depois pega o número antes de '.'
    number = int(number_str)

    # Realizando os cálculos
    result = (number / 44300) * 1.440

    # Aproximando o valor (arredondando para o inteiro mais próximo)
    result_rounded = round(result)

    # Criando e retornando o dicionário
    return {
        "Episodio": episodenumber,
        "result": result_rounded
    }

if __name__ == '__main__':
    resultado = processar_episodios()
    print("Resultado final:", resultado)
