---
title: D CSS设置
comments: true
---

## 壹丨CSS设置

### 1. 字体相关

引入字体

```css
@font-face {
    font-family: 'Lato';
    font-style: normal;
    font-weight: 400;
    src: local('Lato-Italic.ttf'), url('./FONTS/Lato.woff2') format('truetype');
}

@font-face {
    font-family: "Monaco";
    src: local('monaco'), url("./FONTS/MONACO.woff2") format('truetype');
}

@font-face {
    font-family: 'NotoSerifSC';
    font-style: normal;
    font-weight: 400;
    src: local('NotoSerifSC.otf'), url('./FONTS/NotoSerifSC.subset.otf') format('truetype');
}

/*@font-face {*/
/*    font-family: "EBGaramond";*/
/*    font-size: 16px;*/
/*    src: url("./FONTS/woff2/EBGaramond-Regular.woff2");*/
/*}*/

/*@font-face {*/
/*    font-family: "LavishlyYours";*/
/*    font-size: 16px;*/
/*    src: url("./FONTS/woff2/LavishlyYours-Regular.woff2");*/
/*}*/

/*@font-face {*/
/*    font-family: "LiuJianMaoCao";*/
/*    font-size: 16px;*/
/*    src: url("./FONTS/woff2/LiuJianMaoCao-Regular.woff2");*/
/*}*/

/*@font-face {*/
/*    font-family: "Monoton";*/
/*    font-size: 16px;*/
/*    src: url("./FONTS/woff2/Monoton.woff2");*/
/*}*/

/*@font-face {*/
/*    font-family: "PressStart2P";*/
/*    font-size: 16px;*/
/*    src: url("./FONTS/woff2/PressStart2P-Regular.woff2");*/
/*}*/

/*@font-face {*/
/*    font-family: "ZhiMangXing";*/
/*    font-size: 16px;*/
/*    src: url("./FONTS/woff2/ZhiMangXing-Regular.woff2");*/
/*}*/
```

设置字体

```css
:root {
    --md-code-font: "Monaco";
    --md-text-font: "Lato", "NotoSerifSC";
    --md-default-bg-color: #fff;
}
```

导航栏设置

```css
/*导航栏字体大小*/
.md-tabs__link {
    font-size: 0.8rem;
}

.md-nav {
    /*font-size: .75rem;*/
    line-height: 1.3;
}
```

Jupyter插件字体

```css
/*jupyter插件*/
.jupyter-wrapper {
    --jp-code-font-size: 16px !important;
}
```

### 2. 图片相关

```css
.glightbox {
    flex: 1;
    margin-right: 2px;
    display: flex;
    flex-direction: column;
}

.glightbox img {
    max-width: 100%;
    height: 100%;
    object-fit: contain;
}


img {
    -webkit-transition: filter 375ms ease-in .2s, -webkit-transform .6s;
    -moz-transition: filter 375ms ease-in .2s, -moz-transform .6s;
    -o-transition: filter 375ms ease-in .2s, -o-transform .6s;
    -ms-transition: filter 375ms ease-in .2s, -ms-transform .6s;
    transition: filter 375ms ease-in .2s, transform .6s;
}


/*普通图片*/
.md-typeset img {
    max-width: 85%;
    max-height: 480px;
    display: grid;
    box-shadow: 0 5px 10px rgba(20, 20, 20, .2);
    border-radius: 5px;
    padding: 0 !important;
    margin: 0 auto;
}

/*放大图片大小控制*/
.gslide-image img {
    max-width: 75% !important;
}

/*并排图片*/
.inline-img {
    display: flex;
    justify-content: space-between;
}
```

### 3. 表格

```css
/*表格*/
.md-typeset__table {
    min-width: 85%;
    max-width: 100%;
    display: table;
    margin: auto;
}

table {
    border-collapse: collapse;
    border-spacing: 0;
}

.md-typeset table:not([class]) {
    display: table;
    border: 0;
}

thead {
    border-top: 2px solid #000;
    border-bottom: 1px solid #000;
}

tbody {
    border-bottom: 2px solid #000;
}

.md-typeset table:not([class]) td {
    border-top: 0;
}

.md-typeset table:not([class]) td:not([align]), .md-typeset table:not([class]) th:not([align]) {
    text-align: center;
}

.no-line tbody {
    border-bottom: 0;
}

.no-line td {
    text-align: center;
}
```



### 4. 时间线

见[timeline.css](https://github.com/Neoteroi/mkdocs-plugins/blob/main/styles/timeline.scss)

### 5. 其他

```css
/*内容宽度*/
.md-grid {
    /*max-width: 1600px;*/
    max-width: 95%;
}

/*.glightbox {*/
/*    pointer-events: none;*/
/*}*/

/*导航栏缩进*/
.md-nav__item {
    padding-left: 15px !important;
}
```



## 贰丨设置

### 1. 使用`@import`导入

```css
@import "./fonts.min.css";
@import "./image.min.css";
@import "./other.min.css";
@import "./timeline.min.css";
@import "./table.min.css";
```

!!! warning "这样会导致加载的CSS文件多，影响性能"

### 2. 构建时自动合并CSS

```python
# -*- coding: utf-8 -*-
"""
====================================
@File Name: test.py
@Time: 2023/7/1 12:21
@Program IDE：PyCharm
@Create by Author: 一一风和橘
@Motto: "The trick, William Potter, is not minding that it hurts."
@Description:
- 合并CSS文件
====================================
"""
import os
import shutil

PATH_CSS = '../site/stylesheets'


def merge_css():
    min_css = os.listdir(PATH_CSS)
    css_list = []
    for css in min_css:
        if '.min.css' not in css:
            continue
        if css == 'extra.min.css':
            continue
        with open(f'{PATH_CSS}/{css}', 'r', encoding='utf-8') as f:
            content = f.readlines()
        css_list.extend(content)
    shutil.rmtree(PATH_CSS)
    os.mkdir(PATH_CSS)
    with open(f'{PATH_CSS}/extra.css', 'w', encoding='utf-8') as f:
        f.writelines(css_list)


if __name__ == '__main__':
    # 合并CSS
    merge_css()

```