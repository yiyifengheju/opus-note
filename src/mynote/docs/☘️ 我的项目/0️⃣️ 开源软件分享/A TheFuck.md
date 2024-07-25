---
title: 🤩️ TheFuck
comments: true
---

<img src="https://raw.githubusercontent.com/nvbn/thefuck/master/example.gif">

功能：纠正输入错误的cmd命令

开源链接：https://github.com/nvbn/thefuck

!!! tip "安装（Ubuntu）"

    第一步，安装：
    
    ```bash
    sudo apt update
    sudo apt install python3-dev python3-pip python3-setuptools
    pip3 install thefuck --user
    ```
    
    第二步，添加环境变量：
    
    ```bash
    sudo nano ~/.bashrc
    ```
    
    添加：
    
    ```bash
    eval $(thefuck --alias)
    # You can use whatever you want as an alias, like for Mondays:
    eval $(thefuck --alias FUCK)
    ```
    
    第三步，激活环境：
    ```bash
    source ~/.bashrc
    ```



!!! note "升级"

    ```bash
    pip3 install thefuck --upgrade
    ```
