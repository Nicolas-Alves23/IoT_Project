# Versão para ipwebcam


# import cv2
# from ultralytics import YOLO

# # Caminho do stream da câmera do celular
# IP_CAM_URL = 'http://10.246.222.218:8080/video'  # Substitua com seu IP Webcam

# # Carrega modelo YOLOv8 pré-treinado
# model = YOLO('yolov8n.pt')  # 'n' é o mais leve; pode usar 'yolov8m.pt' ou 'yolov8l.pt' também

# cap = cv2.VideoCapture(IP_CAM_URL)

# print("[INFO] Pressione 'q' para sair.")

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("[ERRO] Não foi possível acessar o vídeo.")
#         break

#     # Executa a inferência
#     results = model(frame)[0]

#     # Desenha os resultados na imagem
#     annotated_frame = results.plot()

#     # Mostrar a imagem com detecções
#     cv2.imshow("YOLOv8 - Detecção de Objetos", annotated_frame)

#     # Tecla para sair
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


#  versão para o modelo com webcam no pc

# -------------------------------Para detectar---------------------------------

# import cv2
# from ultralytics import YOLO

# # Use a webcam do computador (índice 0)
# cap = cv2.VideoCapture(0)

# # Carrega modelo YOLOv8 pré-treinado
# model = YOLO('yolov8n.pt')

# print("[INFO] Pressione 'q' para sair.")

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("[ERRO] Não foi possível acessar a webcam.")
#         break

#     # Inferência
#     results = model(frame)[0]

#     # Extrai boxes, classes e scores
#     boxes = results.boxes.xyxy.cpu().numpy()   # [x_min, y_min, x_max, y_max]
#     classes = results.boxes.cls.cpu().numpy()  # índices das classes
#     scores = results.boxes.conf.cpu().numpy()

#     # Índice da classe 'person'
#     person_class_id = 0

#     # Filtra só pessoas
#     person_boxes = boxes[classes == person_class_id]
#     person_scores = scores[classes == person_class_id]

#     # Desenha só as pessoas
#     annotated_frame = frame.copy()

#     for box in person_boxes:
#         x1, y1, x2, y2 = box.astype(int)
#         cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#         cv2.putText(annotated_frame, "person", (x1, y1 - 10),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

#     # Exibe a imagem
#     cv2.imshow("Apenas Pessoas Detectadas", annotated_frame)

#     # Sai com a tecla 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# ------------------------------Letras detecção----------------------------------

import cv2
import easyocr

reader = easyocr.Reader(['pt', 'en'])  # Português e Inglês

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = reader.readtext(frame)

    for (bbox, text, conf) in results:
        # bbox é a caixa delimitadora do texto
        top_left = tuple([int(val) for val in bbox[0]])
        bottom_right = tuple([int(val) for val in bbox[2]])
        cv2.rectangle(frame, top_left, bottom_right, (0,255,0), 2)
        cv2.putText(frame, f'{text} ({conf:.2f})', (top_left[0], top_left[1]-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    cv2.imshow('OCR', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
