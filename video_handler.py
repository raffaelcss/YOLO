import cv2
import os

class VideoHandler:
    def __init__(self, video_path):
        self.video_path = video_path

    def extract_frames(self, output_folder, frame_interval):
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            print("Erro ao abrir o vídeo.")
            return

        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        video_duration = total_frames / fps
        num_frames_to_extract = int(video_duration / frame_interval)

        os.makedirs(output_folder, exist_ok=True)

        for i in range(num_frames_to_extract):
            timestamp = int(i * frame_interval * fps)
            cap.set(cv2.CAP_PROP_POS_FRAMES, timestamp)
            success, frame = cap.read()
            if success:
                frame_filename = os.path.join(output_folder, f"frame_{timestamp}.jpg")
                cv2.imwrite(frame_filename, frame)

        cap.release()
        print(f"Extraídos {num_frames_to_extract} frames com sucesso em {output_folder}.")

# Parâmetros
video_path = "./videos/video.mp4"
video_name = os.path.splitext(os.path.basename(video_path))[0]
output_folder = f"./frames/{video_name}/"
frameInterval = 1

# Cria uma instância da classe e executa a extração
video_handler = VideoHandler(video_path)
video_handler.extract_frames(output_folder, frameInterval)
