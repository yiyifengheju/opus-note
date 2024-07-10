---
title: 🎃 富士RAF重命名
date: 2023-10-12 23:46:59
comments: true
---

### 1. 下载ExifTool

官网：[ExifTool by Phil Harvey](https://exiftool.org/) 

下载 **Windows Executable** 版本，解压即可得到`exiftool(-k).exe` 

??? note "命令行使用[^1]"

    ```bash
    exiftool(-k).exe $FILE_PATH$
    ```

### 2. 读取拍摄日期 

将`exiftool.exe`放在Python脚本同级目录下，使用`os.popen()`读取`.RAF`文件信息：

```python
terminal_message = os.popen(rf'.\exiftool.exe {raf_path}').read()
```

### 3. 批量重命名脚本

```python
# -*- coding: utf-8 -*-
"""
====================================
@File Name: 001 rename_raf.py
@Time: 2023/4/22 22:05
@Program IDE：PyCharm
@Create by Author: 一一风和橘
@Motto: "The trick, William Potter, is not minding that it hurts."
@Description:
- RAF文件重命名，时间+文件名
====================================
"""
import os
import shutil

import tqdm

PATH = r'J:\RAF'
NEW_PATH = r'J:\RAF_copy'
if not os.path.exists(NEW_PATH):
    os.mkdir(NEW_PATH)


def get_date_original(raf_path):
    terminal_message = os.popen(rf'.\exiftool.exe {raf_path}').read()
    for line in terminal_message.split('\n'):
        if 'Date/Time Original' in line:
            return line.split(' : ')[-1].split(' ')[0].replace(':', '')
    assert 0, 'Find No Date/Time Original'


def run():
    if not os.path.exists(NEW_PATH):
        os.mkdir(NEW_PATH)

    file_list = os.listdir(PATH)
    t_file_list = tqdm.tqdm(file_list)
    for file in t_file_list:
        if file == 'Desktop.ini':
            continue
        t_file_list.set_description(file)
        raf_path = os.path.abspath(f'{PATH}/{file}')
        # 获取原始时间
        pre = get_date_original(raf_path)
        # 新建日期路径
        new_dir = f'{NEW_PATH}/{pre}'
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        # 获取RAF信息
        # info = get_raf_info(raf_path)
        shutil.copy(f'{PATH}/{file}', f'{new_dir}/{pre}_{file.split("_")[0]}.RAF')


if __name__ == '__main__':
    run()

```

[^1]: 知乎，@周德蔚，[读取RAW图像的metadata](https://zhuanlan.zhihu.com/p/439149723)
