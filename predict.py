from ultralytics import YOLO
import cv2

video_path = "./videos/video.mp4"

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(video_path)

while True:
    if cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()
        if success:

            # Execute a inferência YOLOv8
            results = model(frame, device=0,  imgsz=640)

            for r in results:
                boxes = r.boxes
                for box in boxes:
                    x1,y1,x2,y2 = box.xyxy[0]
                    x1,y1,x2,y2 =  int(x1), int(y1), int(x2), int(y2)
                    conf = int (box.conf[0]*100)
                    cls = int (box.cls[0])
                    cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 255, 0), 2)
                
            cv2.imshow("YOLOv8", frame)
            # Pressione 'x' para interromper a execução
            if cv2.waitKey(1) & 0xFF == ord("x"):
                break
        else:
            # Encerre o loop quando o final do vídeo for alcançado
            break

# Libere o objeto de captura de vídeo e feche a janela de exibição
cap.release()
cv2.destroyAllWindows()