---
title: 🎄 富士RAF解锁胶片模拟
date: 2024-07-06 18:46:59
comments: true
---

## 壹丨引言

富士相机以其独特的胶片模拟滤镜闻名，为摄影师提供了丰富的后期处理风格选择。然而，旧机型不支持最新的胶片模拟。比如我的X-T30不支持CLASSIC Neg、NOSTALGIC Neg等，虽然可以通过Capture One解锁部分，但还是无法用到最新滤镜，如X-T50上的REALA ACE

> 本文介绍一种通过修改EXIF解锁胶片模拟的方法
>
> 工具：ExifTool（[ExifTool by Phil Harvey](https://exiftool.org/) ）

> `exifread`、`pyexiv2`等Python扩展库不支持修改富士RAF

## 贰丨ExifTool修改RAF的Exif信息

查看RAF文件的Exif信息：

```bash
.\exiftool.exe .\DSCF9285.RAF
```

下面摘抄部分：

```bash
ExifTool Version Number         : 12.62
File Name                       : DSCF9285.RAF
Directory                       : .
File Size                       : 59 MB
File Modification Date/Time     : 2024:05:26 15:03:46+08:00
File Access Date/Time           : 2024:07:06 19:19:14+08:00
File Creation Date/Time         : 2024:07:06 17:47:54+08:00
File Permissions                : -rw-rw-rw-
File Type                       : RAF
File Type Extension             : raf
MIME Type                       : image/x-fujifilm-raf
RAF Version                     : 0201
Exif Byte Order                 : Little-endian (Intel, II)
Make                            : FUJIFILM
Camera Model Name               : X-T30
Resolution Unit                 : inches
Software                        : Digital Camera X-T30 Ver2.01
Modify Date                     : 2024:05:26 15:03:46
...
```

其中，`Camera Model Name`代表相机型号，但使用下面的EXIF修改方法并不能真正的修改相机型号，因为实际相机型号标签名是`Model`。（盲猜ExifTool展示的EXIF标签名做了转义）

```bash
exiftool.exe "-Camera Model Name=X-T50" ".\DSCF9285.RAF"
```

因此，要修改相机型号，需要使用：

```bash
exiftool.exe "-Model=X-T50" ".\DSCF9285.RAF"
```

使用Honeyview查看相机型号已经修改成功

![image-20240706213131800](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/image-20240706213131800.png)

![image-20240706214534586](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/image-20240706214534586.png)

最后，导入Capture One，修改后的RAF可选NOSTALGIC Neg和REALA-ACE

![image-20240706215100952](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/image-20240706215100952.png)

## 叁丨重命名脚本

由于相机给照片命名是循环命名，随着照片数量增加，可能会出现重名文件。同时，为了方便管理，我一般使用拍摄日期重命名照片，这里给出重命名脚本：

```python
import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

import tqdm

PATH_EXIFTOOL = Path(__file__).resolve().parent / 'bin/exiftool.exe'


def __run(file, path_src, path_dst, aim_model):
    raf_path = os.path.abspath(f'{path_src}/{file}')
    if aim_model:
        cmd = (f'{PATH_EXIFTOOL} '
               f'"-Model={aim_model}" '
               f'"-FileName<CreateDate" -d "{path_dst}/%Y%m%d/%Y%m%d_%%f.%%e" '
               f'"{raf_path}"')
    else:
        cmd = (f'{PATH_EXIFTOOL} '
               f'"-FileName<CreateDate" -d "{path_dst}/%Y%m%d/%Y%m%d_%%f.%%e" '
               f'"{raf_path}"')
    os.popen(cmd)


def raf_renamer(path_src: str,
                path_dst: str,
                aim_model: str = '',
                max_workers: int = 12
                ) -> None:
    assert os.path.exists(PATH_EXIFTOOL), 'exiftool.exe is not found'

    if not os.path.exists(path_dst):
        os.mkdir(path_dst)

    files = os.listdir(path_src)
    t_file_list = tqdm.tqdm(files)

    with ThreadPoolExecutor(max_workers=max_workers) as t:
        futures = [t.submit(__run, file, path_src, path_dst, aim_model) for file in files if file != 'Desktop.ini']
        for future in as_completed(futures):
            t_file_list.update(1)
            t_file_list.set_description(future.result())
```

调用方法：

```python
if __name__ == '__main__':
    src = r'C:\Users\Artmallo\Desktop\src'
    dst = r'C:\Users\Artmallo\Desktop\dst'
    raf_renamer(src, dst, aim_model='X-T50')
```

`src`为源RAF路径，`dst`为目标保存路径，`aim_model`为修改的相机目标型号

## 注意事项

1. X系列相机不要修改成GFX型号，否则颜色会出现混乱
2. Capture One用最新版，否则无法识别新的相机型号，导致修改后的RAF无法导入
3. 附：X系列相机胶片模拟数量

| 相机型号 | 胶片模拟数 | 独特支持                                                    |
| -------- | ---------- | ----------------------------------------------------------- |
| X100VI   | 20         | CLASSIC Neg、NOSTALGIC Neg、ETERNA BLEACH BYPASS、REALA ACE |
| X-T50    | 20         | CLASSIC Neg、NOSTALGIC Neg、ETERNA BLEACH BYPASS、REALA ACE |
| X-T5     | 19         | CLASSIC Neg、NOSTALGIC Neg、ETERNA BLEACH BYPASS            |
| X-H2     | 19         | CLASSIC Neg、NOSTALGIC Neg、ETERNA BLEACH BYPASS            |
| X-H2s    | 19         | CLASSIC Neg、NOSTALGIC Neg、ETERNA BLEACH BYPASS            |
| X-S20    | 19         | CLASSIC Neg、NOSTALGIC Neg、ETERNA BLEACH BYPASS            |
| X-T30II  | 18         | CLASSIC Neg、ETERNA BLEACH BYPASS                           |
| X-E4     | 18         | CLASSIC Neg、ETERNA BLEACH BYPASS                           |
| X-Pro3   | 17         | CLASSIC Neg                                                 |

