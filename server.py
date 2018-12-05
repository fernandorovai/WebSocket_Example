import asyncio
import websockets
import cv2
import base64
from io import BytesIO
from PIL import Image
import functools

# buffered = BytesIO()
# image.save(buffered, format="JPEG")
# img_str = buffered.getvalue()

# Send 
async def sendFrame(websocket, path, extra_argument):
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read()
        _, img_str = cv2.imencode('.jpg', frame)
        img_str = img_str.tobytes()
        await websocket.send(img_str)

bound_handler = functools.partial(sendFrame, extra_argument="")
start_server = websockets.serve(bound_handler, '127.0.0.1', 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()