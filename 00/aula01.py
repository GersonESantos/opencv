import cv2

# Lê a imagem do arquivo
imagem = cv2.imread('hello_opencv_output.png')

# Verifica se a imagem foi carregada corretamente
if imagem is None:
    print("Erro: não foi possível carregar a imagem 'teste.jpg'. Verifique o caminho do arquivo.")
else:
    # Exibe a imagem em uma janela
    cv2.imshow('CFBCursos - Primeira Imagem', imagem)

    # Aguarda o pressionamento de qualquer tecla
    cv2.waitKey(0)

    # Fecha todas as janelas abertas
    cv2.destroyAllWindows()

    # Mostra as dimensões da imagem (altura, largura, canais)
    print(imagem.shape)