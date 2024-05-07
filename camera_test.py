import json
import requests
import cv2

def abrir_camera(id_thread, camera):
    cap = cv2.VideoCapture(camera)
    contador_frames = 0
    while True:
        if contador_frames == 100: break
        ret, frame = cap.read() 
        if not ret:
            print('Stream offline')
            break
        else:
            if contador_frames % 10 == 0:
                cv2.imwrite(f'thread_{id_thread} frame_{contador_frames}.jpg', frame)
                print(f'thread_{id_thread} Frame salvo: frame_{contador_frames}.jpg')  
        contador_frames += 1
        
if __name__ == '__main__':
    
    link = 'http://api-gestor-homologacao-env.eba-pquymxvp.us-east-2.elasticbeanstalk.com/api/safe/midia/streaming/selecionados'
    headers = {
        'x-access-token': 'XemK%RMP98m!FF45BmO*EnkwZ9W@c+RMlLarc'    
    }

    response = requests.get(link, headers=headers)
    response_data = json.loads(response.text)
    
    streams_hls = [camera['streamHls'] for camera in response_data['dados'][0]['cameras']]
    
    for i, camera in enumerate(streams_hls):
            abrir_camera(i, camera)