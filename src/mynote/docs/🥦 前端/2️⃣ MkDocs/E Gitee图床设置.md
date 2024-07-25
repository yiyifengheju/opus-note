---
title: E Gitee图床设置
comments: true
---

!!! warning "适用于更新频率较低的gallery.mastermao.cn网站"

!!! warning "直接使用PicGo上传到Gitee，再同步到GitHub效果也是相同的"

	具体做法为，将picbed设置为双线部署，即同时上传到GitHub和Gitee

## 壹丨需求分析

市面上的图床无非几种：

| 类型             | 优点               | 缺点                               |
| ---------------- | ------------------ | ---------------------------------- |
| 腾讯云、阿里云…… | 速度快、稳定       | 收费项繁多，只做图床实在浪费       |
| 七牛云、又拍云…… | 速度快、有免费套餐 | 域名需要备案，还需要部署在服务器上 |
| sm.ms、meotu……   | 免费               | 不稳定，没准哪天倒闭，慢           |
| 自建图床         | 速度快、免费       | 需要公网IP、不好维护               |
| GitHub           | 免费               | 速度慢                             |
| Gitee            | 速度快、免费       | 可能会挂                           |

鉴于Gitee可以同步GitHub仓库，所以可以图片上传到GitHub，再把图片链接改了嘛！！

## 贰丨操作步骤

### 1. 准备工作

第一步，GitHub新建仓库`picbed`

第二步，Gitee新建仓库`picbed`，选择从GitHub导入

第三步，Gitee开启Gitee Pages服务

### 2. 配置PicGo

第一步，创建GitHub的token：Settings——Developer settings——Personal access tokens——generate new token

第二步，PicGo中配置图床

```
设定仓库名: yiyifengheju/picbed
设定分支名: main
设定Token: xxxxxxxxxxxxxxxxxxx
指定存储路径: 空
```

然后设置为默认图床

第三步，配置CDN加速。上传图片并获取图片链接，粘贴到[JSDELIVR](https://www.jsdelivr.com/github)，获得加速链接，如：

```
GitHub
https://github.com/yiyifengheju/picbed/blob/main/alpkslgy/20230708_20230708_DSCF4654.webp

JSDELIVR
https://cdn.jsdelivr.net/gh/yiyifengheju/picbed@main/alpkslgy/20230708_20230708_DSCF4654.webp
```

将获取到的`https://cdn.jsdelivr.net/gh/yiyifengheju/picbed@main`字段设置在图床配置的`设定自定义域名`



!!! note "为啥要配置CDN加速呢？"

	使用Typora写文档、使用`mkdocs serve`命令预览时还是要使用GitHub图床，所以能快就快点嘛！

### 3. 部署及修改图床链接

基本思路：

1. 使用`mkdocs build`命令，生成`./site`网站文件
2. 遍历网站文件，找到GitHub图片链接，修改为Gitee图片链接

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
- 修改图床链接
- 
====================================
"""
import os

ROOT_PATH = '../'
SITE_PATH = '../site'
GITHUB_BED = 'https://cdn.jsdelivr.net/gh/yiyifengheju/picbed@main/'
GITEE_BED = 'https://mastermao.gitee.io/picbed/'


def switch_pic_bed(contents):
    new_contents = [line.replace(GITHUB_BED, GITEE_BED) for line in contents]
    return new_contents


def edit_picbed():
    for root, dirs, files in os.walk(SITE_PATH):
        for file in files:
            if file.endswith('.html'):
                html_path = os.path.join(root, file)
                with open(html_path, 'r', encoding='utf8') as f:
                    contents = f.readlines()
                new_contents = switch_pic_bed(contents)
                with open(file, 'w', encoding='utf8') as f:
                    f.writelines(new_contents)


def build():
    cmd = f'cd {os.path.abspath(ROOT_PATH)} && mkdocs build'
    re = os.system(cmd)
    assert [1, 0][re], '构建失败'


if __name__ == '__main__':
    # 构建
    build()
    # 修改图床
    edit_picbed()

```
