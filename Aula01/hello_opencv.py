import cv2

def main():
    print(f"OpenCV version: {cv2.__version__}")

    # Inicializa a câmera (0 é a webcam padrão)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erro: Não foi possível acessar a câmera.")
        return

    # Captura um único frame da câmera
    ret, frame = cap.read()
    cap.release()  # Libera a câmera imediatamente

    if not ret:
        print("Erro ao capturar a imagem da câmera.")
        return

    # Pega as dimensões da imagem capturada
    height, width, _ = frame.shape

    # Desenha o texto "Hello, OpenCV!" sobre a imagem da câmera
    text = "Hello, OpenCV!"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.2
    thickness = 2
    (text_w, text_h), _ = cv2.getTextSize(text, font, font_scale, thickness)
    x = (width - text_w) // 2
    y = (height + text_h) // 2
    cv2.putText(frame, text, (x, y), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)

    # Desenha o retângulo e o círculo sobre a foto capturada
    cv2.rectangle(frame, (20, 20), (width - 20, height - 20), (0, 200, 255), 2)
    cv2.circle(frame, (width // 2, y + 60), 20, (0, 255, 0), -1)

    # Salva a imagem em disco
    output_path = "foto_camera_output.png"
    cv2.imwrite(output_path, frame)
    print(f"Imagem gravada com sucesso em: {output_path}")

    # Exibe a foto na tela (se houver interface gráfica)
    try:
        cv2.imshow("Foto Capturada", frame)
        print("Pressione qualquer tecla na janela para fechar...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except cv2.error as e:
        print(f"Não foi possível abrir a janela: {e}")

if __name__ == "__main__":
    main()