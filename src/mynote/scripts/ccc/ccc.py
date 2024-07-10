"""
=========================================================================
@File Name: ccc.py
@Time: 2024/6/16 下午9:45
@Program IDE：PyCharm
@Create by Author: 一一风和橘
@Motto: "The trick, William Potter, is not minding that it hurts."
@Description:
- 
- 
=========================================================================
"""
import os

path = r'C:\Users\Artmallo\Desktop\wech'
files = os.listdir(path)
for i, file in enumerate(files):
    tail = file.split('.')[-1]
    os.rename(f'{path}/{file}', f'{path}/{i}.{tail}')
