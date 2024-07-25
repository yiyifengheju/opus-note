---
title: 🐎️ 视频截取图片
comments: true
---

使用`OpenCV`从视频里面截取画面

```python
import cv2
import os
import threading

video_path = "./video"
pic_path = "./images"
video_path, pic_path = os.path.abspath(video_path), os.path.abspath(pic_path)
filelist = os.listdir(video_path)
if not os.path.exists(pic_path):
    os.mkdir(pic_path)


def video2pic(filename):
    cnt = 0
    dnt = 0
    _image_path = os.path.join(pic_path, filename[:-4])
    if not os.path.exists(_image_path):
        os.mkdir(_image_path)
    cap = cv2.VideoCapture(os.path.join(video_path, filename))
    while True:
        ret, image = cap.read()
        if image is None:
            break
        if (cnt % 10) == 0:
            cv2.imencode('.jpg', image)[1].tofile(os.path.join(_image_path, f'{filename[:-4]}{dnt}.jpg'))
            print(os.path.join(_image_path, f'{filename[:-4]}{dnt}.jpg'))
            dnt = dnt + 1
        cnt = cnt + 1
    cap.release()


if __name__ == '__main__':
    for file in filelist:
        threading.Thread(target=video2pic, args=(file,)).start()

```

