import lmdb
import cv2
import os

def save_images_to_lmdb(folder_path, lmdb_path):
    """
    Converte imagens de uma pasta para um banco LMDB.

    :param folder_path: Caminho da pasta com imagens.
    :param lmdb_path: Caminho onde o banco LMDB será salvo.
    """
    # Define o tamanho máximo do banco de dados
    map_size = 40 * 1024 * 1024  # 10 GB, ajuste conforme necessário
    
    # Cria o ambiente LMDB
    env = lmdb.open(lmdb_path, map_size=map_size)
    
    with env.begin(write=True) as txn:
        for filename in sorted(os.listdir(folder_path)):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):  # Verifica se é um arquivo
                img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    # Codifica a imagem para um formato binário
                    img_encoded = cv2.imencode('.png', img)[1].tobytes()
                    # Usa o nome do arquivo como chave
                    txn.put(filename.encode('ascii'), img_encoded)
    print(f"Imagens salvas em LMDB: {lmdb_path}")

def process_subfolders(parent_folder):
    """
    Processa subpastas de uma pasta principal e salva imagens em arquivos LMDB separados.

    :param parent_folder: Caminho da pasta principal que contém subpastas.
    """
    for subfolder in sorted(os.listdir(parent_folder)):
        subfolder_path = os.path.join(parent_folder, subfolder)
        if os.path.isdir(subfolder_path):  # Verifica se é uma subpasta
            lmdb_path = os.path.join(parent_folder, f"{subfolder}.lmdb")
            print(f"Processando subpasta: {subfolder_path}")
            save_images_to_lmdb(subfolder_path, lmdb_path)

# Exemplo de uso
process_subfolders(r".\t2")
