---
title: 🎃️ 图片压缩(tinypng)
comments: true
---

使用`tinypng`压缩图片，需要注册并替换自己的API Key

```python
# -*- coding: utf-8 -*-
"""
====================================
@File Name: tinypng1.py
@Time: 2023/7/29 1:42
@Program IDE：PyCharm
@Create by Author: 一一风和橘
@Motto: "The trick, William Potter, is not minding that it hurts."
@Description:
- 
====================================
"""
import os
import os.path

import click
import tinify

tinify.key = "xxxxx"  # API KEY
version = "1.0.1"


def compress_core(in_file, out_file, img_width):
    source = tinify.from_file(in_file)
    if img_width != -1:
        resized = source.resize(method="scale", width=img_width)
        resized.to_file(out_file)
    else:
        source.to_file(out_file)


# 压缩一个文件夹下的图片
def compress_path(path, width):
    print("compress_path-------------------------------------")
    if not os.path.isdir(path):
        print("这不是一个文件夹，请输入文件夹的正确路径!")
        return
    else:
        from_file_path = path
        to_file_path = path + "/tiny"
        print("fromFilePath=%s" % from_file_path)
        print("toFilePath=%s" % to_file_path)

        for root, dirs, files in os.walk(from_file_path):
            print("root = %s" % root)
            print("dirs = %s" % dirs)
            print("files = %s" % files)
            for name in files:
                filename, file_suffix = os.path.splitext(name)
                if file_suffix == '.png' or file_suffix == '.jpg' or file_suffix == '.jpeg':
                    to_full_path = to_file_path + root[len(from_file_path):]
                    to_full_name = to_full_path + '/' + name
                    if os.path.isdir(to_full_path):
                        pass
                    else:
                        os.mkdir(to_full_path)
                    compress_core(root + '/' + name, to_full_name, width)
            break  # 仅遍历当前目录


def compress_file(input_file, width):
    print("compress_file-------------------------------------")
    if not os.path.isfile(input_file):
        print("这不是一个文件，请输入文件的正确路径!")
        return
    print("file = %s" % input_file)
    dirname = os.path.dirname(input_file)
    basename = os.path.basename(input_file)
    filename, file_suffix = os.path.splitext(basename)
    if file_suffix == '.png' or file_suffix == '.jpg' or file_suffix == '.jpeg':
        compress_core(input_file, dirname + "/tiny_" + basename, width)
    else:
        print("不支持该文件类型!")


@click.command()
@click.option('-f', "--file", type=str, default=None, help="单个文件压缩")
@click.option('-d', "--dir", type=str, default=None, help="被压缩的文件夹")
@click.option('-w', "--width", type=int, default=-1, help="图片宽度，默认不变")
def run(file, _dir, width):
    print("GcsSloop TinyPng V%s" % version)
    if file is not None:
        compress_file(file, width)
        pass
    elif _dir is not None:
        compress_path(_dir, width)
        pass
    else:
        compress_path(os.getcwd(), width)
    print("结束!")


if __name__ == "__main__":
    run()

```

