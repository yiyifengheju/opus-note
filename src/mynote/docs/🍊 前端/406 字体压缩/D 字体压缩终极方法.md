---
title: D 字体压缩终极方法
comments: true
---



## 壹丨问题分析

!!! note "前面几种字体压缩方法并不能满足要求"

	使用CloudConvert无法压缩NotoSerifSC字体
	
	使用fonttools压缩后的字体仍然比较大，网页加载慢
	
	使用Fontmin没法为整个博客压缩对应的字体

但是，`fonttools`和`Fontmin`提供了一种简单可行的思路：

1. 先找到网站涉及的所有文字
2. 构成`fonttools`所使用的`sc_unicode.txt`
3. 使用`fonttools`工具压缩字体

## 贰丨代码实现

```python
# -*- coding: utf-8 -*-
"""
====================================
@File Name ：generate_fonts.py
@Time ： 2023/9/5 11:30
@Program IDE ：PyCharm
@Create by Author ： MasterMao
@Motto ："The trick, William Potter, is not minding that it hurts."
@Introduction : 
- 字体压缩实现
- 
====================================
"""
import os

SITE_PATH = '../site'
AIM_FONT = 'NotoSerifSC.otf'
FONTS_PATH = './Fonts'


def get_letters():
    char_list = []
    for root, dirs, files in os.walk(SITE_PATH):
        for file in files:
            if file.endswith('.html'):
                html_path = os.path.join(root, file)
                with open(html_path, 'r', encoding='utf8') as f:
                    contents = f.readlines()
                for content in contents:
                    char_list.extend(list(content))
    char_simple_list = list(set(char_list))
    return char_simple_list


def generate_fonts(letter_list):
    char_unicode = [str(item.encode('unicode_escape').decode()).split('u')[-1].upper() + '\n' for item in
                    letter_list if '\u4e00' <= item <= '\u9fff']
    with open(f'{FONTS_PATH}/sc_unicode.txt', 'w', encoding='utf8') as f:
        f.writelines(char_unicode)

    # pip install fonttools
    cmd = f'cd {os.path.abspath(FONTS_PATH)} && pyftsubset {AIM_FONT} --unicodes-file=sc_unicode.txt'
    re = os.system(cmd)
    assert [1, 0][re], '生成字体失败'


if __name__ == '__main__':
    letters = get_letters()
    generate_fonts(letters)

```

运行后，会在字体文件夹生成新的字体`xxx.subset.otf`

```
.
├── Fonts
│   ├── NotoSerifSC.otf
│   ├── NotoSerifSC.subset.otf
│   └── sc_unicode.txt
└── generate_fonts.py
```

## 叁丨结果分析

以`gallery.mastermao.cn`网站为例，提取的`sc_unicode.txt`文件内含740个汉字的Unicode码，压缩后的字体体积对比：

| NotoSerifSC.otf | NotoSerifSC.subset.otf | 压缩比 |
| :-------------: | :--------------------: | :----: |
|     10952KB     |         234KB          | 2.14%  |