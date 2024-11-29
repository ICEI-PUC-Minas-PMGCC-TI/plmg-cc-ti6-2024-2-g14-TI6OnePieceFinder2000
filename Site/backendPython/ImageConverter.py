import cv2
import os

class ImageConverter:
    def __init__(self, root_folder, output_path):
        self.root_folder = root_folder
        self.output_path = output_path

    def convert_images_to_gray(self):
        """
        Converte todas as imagens dentro de subpastas para escala de cinza
        e salva na estrutura correspondente na pasta de saída.
        """
        # Itera pelas subpastas na pasta raiz
        for subfolder_name in os.listdir(self.root_folder):
            subfolder_path = os.path.join(self.root_folder, subfolder_name)
            
            # Verifica se é uma subpasta
            if os.path.isdir(subfolder_path):
                output_subfolder = os.path.join(self.output_path, subfolder_name)
                os.makedirs(output_subfolder, exist_ok=True)

                # Processa as imagens dentro da subpasta
                for filename in os.listdir(subfolder_path):
                    file_path = os.path.join(subfolder_path, filename)
                    output_file_path = os.path.join(output_subfolder, filename)

                    # Carrega a imagem
                    image = cv2.imread(file_path)
                    if image is None:
                        print(f"Não foi possível carregar o arquivo: {file_path}")
                        continue

                    # Converte para grayscale
                    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                    # Salva a imagem em escala de cinza na pasta de saída
                    cv2.imwrite(output_file_path, gray_image)

# Exemplo de uso
if __name__ == "__main__":
    root_folder = r".\EpFrames20x15"
    output_path = r".\EpFrames20x15_grey"

    # Garantir que a pasta de saída exista
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    converter = ImageConverter(root_folder, output_path)
    converter.convert_images_to_gray()

