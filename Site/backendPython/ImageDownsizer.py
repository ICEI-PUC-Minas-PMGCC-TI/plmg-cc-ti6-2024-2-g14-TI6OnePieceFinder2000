import cv2
import os

class ImageDownsizer:
    def __init__(self, scale_factor=0.0625):
        self.scale_factor = scale_factor

    def downscale_image(self, image):
        """
        Reduz a escala da imagem pelo fator de escala fornecido.
        """
        height, width = image.shape[:2]
        new_dimensions = (int(width * self.scale_factor), int(height * self.scale_factor))
        return cv2.resize(image, new_dimensions, interpolation=cv2.INTER_AREA)

    def downscale_folder_images(self, input_folder, output_folder):
        """
        Reduz a escala de todas as imagens na pasta de entrada, percorrendo subpastas, 
        e salva na pasta de saída mantendo a estrutura de diretórios.
        """
        for root, dirs, files in os.walk(input_folder):
            # Cria o caminho correspondente na pasta de saída
            relative_path = os.path.relpath(root, input_folder)
            current_output_folder = os.path.join(output_folder, relative_path)

            if not os.path.exists(current_output_folder):
                os.makedirs(current_output_folder)

            # Processa todos os arquivos na pasta atual
            for filename in files:
                input_path = os.path.join(root, filename)

                # Verifica se é um arquivo de imagem
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                    # Carrega a imagem
                    image = cv2.imread(input_path)

                    if image is not None:  # Confirma que a imagem foi carregada corretamente
                        # Reduz a escala da imagem
                        downscaled_image = self.downscale_image(image)

                        # Define o caminho de saída
                        output_path = os.path.join(current_output_folder, filename)

                        # Salva a imagem redimensionada na pasta de saída
                        cv2.imwrite(output_path, downscaled_image)

# Uso do código
root_folder = r"C:\Users\arthu\OneDrive\Documentos\puc6periodo\TI6\TI6OnePieceFinder2000\EpFrames"
output_path = r"C:\Users\arthu\OneDrive\Documentos\puc6periodo\TI6\EpFrames40x30"

downsizer = ImageDownsizer(scale_factor=0.0625)
downsizer.downscale_folder_images(root_folder, output_path)