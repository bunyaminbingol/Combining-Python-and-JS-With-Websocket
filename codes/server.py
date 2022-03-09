import asyncio
import json
import base64
import time
import cv2
import numpy as np
import websockets
import random

# create handler for each connection


async def handler(websocket, path):
    fase_cascade = cv2.CascadeClassifier('C:/Users/Pc/CALISMALARIM/Django_web/Toyota/cascade/frontalface.xml')
    new_frame_time=0
    prev_frame_time=0
    while True:
        try:
            data = await websocket.recv()
            encoded_data = data.split(',')[1]
            nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = fase_cascade.detectMultiScale(gray, 1.3, 7)
            if len(faces) > 0:
                x = int(faces[0][0])
                y = int(faces[0][1])
                w = int(faces[0][2])
                h = int(faces[0][3])       

                reply = {
                    "type": "video",
                    "data": {
                        "x": x,
                        "y": y,
                        "w": w,
                        "h": h
                    }
                }
                await websocket.send(json.dumps(reply))
            
            #======= video frame rate ======================
            new_frame_time=time.time()
            fps = 1/(new_frame_time-prev_frame_time)
            prev_frame_time = new_frame_time
            print('CAM FPS : %.2f  ' % fps)   
                
        except websockets.ConnectionClosedOK:
            break
        
PORT = 8000
start_server = websockets.serve(handler, "localhost", PORT)
print("Server running on: " + str(PORT))

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()