import cv2
from ultralytics import YOLO

# Caminho do stream da câmera do celular
IP_CAM_URL = 'http://10.246.222.218:8080/video'  # Substitua com seu IP Webcam

# Carrega modelo YOLOv8 pré-treinado
model = YOLO('yolov8n.pt')  # 'n' é o mais leve; pode usar 'yolov8m.pt' ou 'yolov8l.pt' também

cap = cv2.VideoCapture(IP_CAM_URL)

print("[INFO] Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERRO] Não foi possível acessar o vídeo.")
        break

    # Executa a inferência
    results = model(frame)[0]

    # Desenha os resultados na imagem
    annotated_frame = results.plot()

    # Mostrar a imagem com detecções
    cv2.imshow("YOLOv8 - Detecção de Objetos", annotated_frame)

    # Tecla para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
