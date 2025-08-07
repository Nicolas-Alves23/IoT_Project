import cv2

# Altere isso para o IP fornecido pelo IP Webcam
# Exemplo: 'http://192.168.42.129:8080/video'
# Se estiver usando ADB port forwarding, use 'http://127.0.0.1:8080/video'
IP_CAM_URL = 'https://10.246.222.218:8080/video'

# --- (Opcional) Ative a detecção de pessoas ---
DETECTAR_PESSOAS = True
HAAR_CASCADE_PATH = 'haarcascade_fullbody.xml'  # baixe esse arquivo do repositório do OpenCV

# Inicia o stream de vídeo
cap = cv2.VideoCapture(IP_CAM_URL)

if DETECTAR_PESSOAS:
    body_cascade = cv2.CascadeClassifier(HAAR_CASCADE_PATH)

print("[INFO] Pressione 'c' para capturar imagem, 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERRO] Não foi possível capturar o vídeo.")
        break

    if DETECTAR_PESSOAS:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corpos = body_cascade.detectMultiScale(gray, 1.1, 3)

        for (x, y, w, h) in corpos:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Câmera do Celular", frame)

    key = cv2.waitKey(1) & 0xFF

    # Capturar imagem
    if key == ord('c'):
        cv2.imwrite("imagem_capturada.jpg", frame)
        print("[INFO] Imagem salva como imagem_capturada.jpg")

    # Sair
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
