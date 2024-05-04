from skimage import feature, color

import imageio
import cv2

import time


video = 'video.mp4'
video_curto = 'video_curto.mp4'


def tempo(funcao, caminho_video):
    start_time = time.time()
    funcao(caminho_video)
    end_time = time.time()
    return (f'{funcao.__name__.upper()} -> {round((end_time - start_time), 2)} segundos')


def iterar_video_opencv(caminho_video):
    cap = cv2.VideoCapture(caminho_video)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

def iterar_video_imageio(caminho_video):
    reader = imageio.get_reader(caminho_video)
    for frame in reader:
        pass

    
def filtro_cinza_opencv(caminho_video):
    cap = cv2.VideoCapture(caminho_video)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def filtro_cinza_imageio(caminho_video):
    reader = imageio.get_reader(caminho_video)
    for frame in reader:
        frame.mean(axis=2).astype('uint8')
        
        
def detectar_borda_opencv(caminho_video):
    cap = cv2.VideoCapture(caminho_video)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.Laplacian(gray, cv2.CV_64F)
        
def detectar_borda_imageio(caminho_video):
    reader = imageio.get_reader(caminho_video)
    for frame in reader:
        gray = color.rgb2gray(frame)
        feature.canny(gray)


if __name__ == '__main__':
    
    funcoes = [
        iterar_video_opencv,
        filtro_cinza_opencv,
        detectar_borda_opencv,
        iterar_video_imageio,
        filtro_cinza_imageio,
        detectar_borda_imageio
        ]

    for response in [tempo(funcao, video_curto) for funcao in funcoes]:
        print(response)
        
    for response in [tempo(funcao, video) for funcao in [funcoes[0], funcoes[3]]]:
        print(response)