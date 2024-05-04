from concurrent.futures import ThreadPoolExecutor
import cv2

cameras = [
    'http://97.68.79.162:80/mjpg/video.mjpg',
    'http://75.112.36.194:80/mjpg/video.mjpg',
    'http://97.76.165.226:80/mjpg/video.mjpg',
    'http://97.68.104.34:80/mjpg/video.mjpg',
    'http://80.28.111.68:81/mjpg/video.mjpg',
    'http://217.86.173.126:80/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER',
    'http://213.3.5.199:80/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER',
    'http://85.220.149.7:80/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER'
]

def abrir_camera(id_thread, camera):
    cap = cv2.VideoCapture(camera)
    contador_frames = 0
    while True:
        if contador_frames == 100: break
        ret, frame = cap.read() 
        if not ret:
            print('Stream offline')
        else:
            if contador_frames % 10 == 0:
                cv2.imwrite(f'thread_{id_thread} frame_{contador_frames}.jpg', frame)
                print(f'thread_{id_thread} Frame salvo: frame_{contador_frames}.jpg')  
        contador_frames += 1
        
if __name__ == '__main__':
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        for i, camera in enumerate(cameras):
            executor.submit(abrir_camera, i, camera)