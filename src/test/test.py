"""
=========================================================================
@File Name: test.py
@Time: 2024/7/25 上午12:19
@Program IDE：PyCharm
@Create by Author: 一一风和橘
@Motto: "The trick, William Potter, is not minding that it hurts."
@Description:
- 
- 
=========================================================================
"""
import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def print_all_emojis():
    all_emojis = []
    url = 'https://unicode.org/Public/emoji/latest/emoji-sequences.txt'
    response = requests.get(url)

    with open('emojis.txt', 'w', encoding='utf-8') as fout:
        for line in response.content.decode('utf8').split('\n'):
            if line.strip() and not line.startswith('#'):
                hexa = line.split(';')[0]
                hexa = hexa.split('..')
                if len(hexa) == 1:
                    # 处理单个 Unicode 代码点
                    ch = ''.join([chr(int(h, 16)) for h in hexa[0].strip().split(' ')])
                    print(ch, end='\n', file=fout)
                    # print(ch, end='\n')
                    all_emojis.append(ch)
                else:
                    # 处理 Unicode 代码点范围
                    start, end = hexa
                    for ch in range(int(start, 16), int(end, 16) + 1):
                        print(chr(ch), end='\n', file=fout)
                        # print(chr(ch), end='\n')
                        all_emojis.append(chr(ch))
    return all_emojis


def get_emoji_color(text: str):
    im = Image.new('RGBA', (100, 100), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('seguiemj.ttf', 64, encoding='unic')
    draw.text((10, 10), text, (255, 255, 255), font=font, embedded_color=True)
    # color = im.getpixel((50, 50))

    pixels = im.getdata()
    # 初始化颜色通道总和
    red_sum = 0
    green_sum = 0
    blue_sum = 0
    total_pixels = 0
    # 遍历所有像素数据，计算颜色通道总和
    for pixel in pixels:
        if pixel[3] == 0:
            continue
        red_sum += pixel[0]
        green_sum += pixel[1]
        blue_sum += pixel[2]
        total_pixels += 1

    # 计算颜色通道平均值
    red_mean = red_sum / total_pixels
    green_mean = green_sum / total_pixels
    blue_mean = blue_sum / total_pixels
    color = [red_mean, green_mean, blue_mean]
    # print(color)
    # assert 0
    return color


if __name__ == '__main__':
    import numpy as np
    from sklearn.cluster import KMeans
    import pandas as pd

    res = print_all_emojis()
    train_x, train_y = [], []
    for emoji in res:
        tmp = get_emoji_color(emoji)
        train_x.append(list(tmp))
        train_y.append(emoji)
    train_x = np.array(train_x)
    train_y = np.array(train_y)

    k = 6
    kmeans = KMeans(n_clusters=k, random_state=22)
    labels = kmeans.fit_predict(train_x)
    tmp = np.array([train_y, labels]).T
    res = pd.DataFrame(tmp, columns=['emoji', 'cls'])
    res.to_csv('kmeans.csv')
