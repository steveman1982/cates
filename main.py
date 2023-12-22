import os
import cv2
from ultralytics import YOLO
from flask import Flask, request
import io

import requests

# optional, get notified
chat_id = <chat_id>
bot_token = <bot_token>


def send_telegram_msg(image, caption='cate?'):
    _, buffer = cv2.imencode('.jpg', image)
    # do not write a temp file, create a jpg file in memory
    bytes_io = io.BytesIO(buffer)

    photo_payload = {'photo': bytes_io}

    data={"chat_id": chat_id, "caption": caption}
    
    requests.post(f"https://api.telegram.org/bot{bot_token}/sendPhoto",
                 files=photo_payload, data=data)

#model = YOLO('yolov8n_saved_model/')
model = YOLO('yolov8l.pt')


app = Flask(__name__)


@app.route('/', methods=['POST'])
def receive():
    data = request.json
    try:
        process(data)
    except Exception as e:
        # TODO bad practice
        print(e)
    finally:
        return "ok"
    

def process(data: dict):
    data = request.json

    path = data['path']
    image = cv2.imread(path)
    print(os.path.exists(path), path)
    parts = path.split('-')

    x_mid = int(parts[-2])
    y_mid = int(parts[-1][:-4])

    x_min = x_mid - 320
    y_min = y_mid - 190

    x_min = max(0, x_min)
    y_min = max(0, y_min)

    if (x_min + 640) > image.shape[1]:  
         x_min = image.shape[1] - 640

    if (y_min + 380) > image.shape[0]:
        y_min = image.shape[0] - 380

    image = image[y_min: y_min + 380, x_min : x_min + 640]
    # this only keeps the last file, add a timestamp if you want to keep all
    cv2.imwrite('', image)
    results = model(path)

    send_message = False

    for r in results:
        for box in r.boxes:
            c = box.cls
            name = model.names[int(c)]
            print(name)

            if name in ['cat', 'dog', 'bear']:
                send_message = True
                # TODO skip the rest of the results once there is a hit...

    print(f"{path} detection" if send_message else f"{path} nothing")
    if send_message:
        send_telegram_msg(image)


if __name__ == '__main__':
    # TODO use something like waitress, disable debug once done tinkering
    app.run(debug=True, port=5000)
