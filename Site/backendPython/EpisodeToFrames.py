import cv2
import os
import time

class VideoToFrames:
    def __init__(self, video_path, frames_dir):
        self.video_path = video_path
        self.frames_dir = frames_dir

    def extract_frames(self):
        # Cria uma pasta para salvar os frames, se não existir
        if not os.path.exists(self.frames_dir):
            os.makedirs(self.frames_dir)

        # Captura o vídeo
        video = cv2.VideoCapture(self.video_path)

        # Variável para contar os frames
        frame_count = 0

        # Inicia o cronômetro
        start_time = time.time()

        while True:
            # Lê o frame
            ret, frame = video.read()

            # Se não conseguir ler o frame, sai do loop
            if not ret:
                break

            # Salva o frame como uma imagem
            frame_path = os.path.join(self.frames_dir, f'frame_{frame_count:04d}.jpg')
            cv2.imwrite(frame_path, frame)

            # Incrementa o contador de frames
            frame_count += 1

        # Libera o vídeo
        video.release()

        # Calcula o tempo total e os frames por segundo
        end_time = time.time()
        total_time = end_time - start_time
        fps = frame_count / total_time if total_time > 0 else 0

        print(f'Extração concluída. {frame_count} frames salvos em {self.frames_dir}.')
        print(f'Tempo total: {total_time:.2f} segundos')
        print(f'FPS de processamento: {fps:.2f} frames por segundo')


def process_videos(input_dir):
    # Nome da pasta para salvar os frames
    ep_frames_dir = os.path.join(input_dir, "EpFrames")
    if not os.path.exists(ep_frames_dir):
        os.makedirs(ep_frames_dir)

    # Lista os arquivos no diretório de entrada
    videos = [f for f in os.listdir(input_dir) if f.endswith(('.mp4', '.avi', '.mkv', '.mov'))]
    videos.sort()  # Ordena os vídeos em ordem alfabética

    # Processa os 61 primeiros vídeos
    for i, video in enumerate(videos[:61]):
        video_path = os.path.join(input_dir, video)
        video_frames_dir = os.path.join(ep_frames_dir, f'Episode_{i+1:02d}')

        print(f'Processando vídeo {i+1}: {video_path}')
        v2f = VideoToFrames(video_path, video_frames_dir)
        v2f.extract_frames()

# Exemplo de uso
if __name__ == "__main__":
    print("teste")
    caminho_dos_videos = r".\[Anime Time] One Piece (0001-1071+Movies\Episode 001-206 Uncropped (480p)"
    process_videos(caminho_dos_videos)
