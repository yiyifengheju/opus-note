# -*- coding: utf-8 -*-
"""
====================================
@File Name: auto_git.py
@Time: 2023/7/28 2:24
@Program IDE：PyCharm
@Create by Author: 一一风和橘
@Motto: "The trick, William Potter, is not minding that it hurts."
@Description:
- 
====================================
"""
from git import Repo

# 打开现有的仓库
repo = Repo('./')

# 添加文件
repo.index.add(['file.txt'])

# 提交更改
repo.index.commit('添加文件')