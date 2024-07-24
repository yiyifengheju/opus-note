"""
=========================================================================
@File Name: test2.py
@Time: 2024/7/25 上午12:23
@Program IDE：PyCharm
@Create by Author: 一一风和橘
@Motto: "The trick, William Potter, is not minding that it hurts."
@Description:
- 
- 
=========================================================================
"""

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import os

im = Image.new('RGBA', (100, 100), (255, 255, 255,0))
draw = ImageDraw.Draw(im)
font = ImageFont.truetype('seguiemj.ttf', 64, encoding = 'unic')
textToDraw = u'😀'
print(textToDraw)
draw.text((10,10), textToDraw, (255,255,255), font=font, embedded_color=True)
im.show()
color = im.getpixel((50, 50))
print(color)
