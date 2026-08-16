import cv2
import numpy as np

def main():
    print(f"OpenCV version: {cv2.__version__}")

    # Cria uma imagem em branco (fundo azul escuro)
    width, height = 640, 360
    img = np.full((height, width, 3), (60, 30, 0), dtype=np.uint8)

    # Desenha o texto "Hello, OpenCV!"
    text = "Hello, OpenCV!"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.2
    thickness = 2
    (text_w, text_h), _ = cv2.getTextSize(text, font, font_scale, thickness)
    x = (width - text_w) // 2
    y = (height + text_h) // 2
    cv2.putText(img, text, (x, y), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)

    # Desenha um retângulo e um círculo de exemplo
    cv2.rectangle(img, (20, 20), (width - 20, height - 20), (0, 200, 255), 2)
    cv2.circle(img, (width // 2, y + 60), 20, (0, 255, 0), -1)

    output_path = "hello_opencv_output.png"
    cv2.imwrite(output_path, img)
    print(f"Imagem salva em: {output_path}")

    # Tenta exibir a janela (funciona se houver ambiente gráfico disponível)
    try:
        cv2.imshow("Hello OpenCV", img)
        print("Pressione qualquer tecla na janela para fechar...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except cv2.error as e:
        print(f"Não foi possível abrir uma janela (ambiente sem GUI): {e}")

if __name__ == "__main__":
    main()
