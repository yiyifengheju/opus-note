---
title: G Ubuntu设置Jupyter Lab远程访问
comments: true
date: 2023.11.28
---


背景：公司电脑没有GPU，平时使用Pycharm的SSH连接到GPU服务器，但在使用过程中存在一些问题，包括：

* Pycharm有`浏览远程主机`小工具，但我经常把不同项目的同步目录搞乱，有时也搞不清文件是否已经同步
* Pycharm的Notebook支持有代码补全、自动格式化等功能，但界面并没有很好用，比如必须切换英文输入才能使用`a`或`b`新增块
* 代码修改后执行，需要对GPU服务器上传帮助文件，反应很慢

解决方案：配置远程GPU服务器的Jupyter Lab，在本地远程访问。

| 优点                                          | 缺点                                           |
| --------------------------------------------- | ---------------------------------------------- |
| 1. Jupyter Lab清洁、轻量化<br />2. 响应速度快 | 1. 没有自动格式化<br />2. 代码补全功能不够强大 |

## 壹丨安装配置Jupyter Lab[^1]

> 这里用个人电脑的WSL模拟远程GPU服务器

首先，确保远程服务器安装了Anaconda或Miniconda

### 第一步，安装Jupyter Lab

```bash
conda install -c conda-forge jupyterlab -y
```

![image-20231118020414410](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/202311180204959.png)

### 第二步，设置Jupyter Lab访问密码

命令行输入：

```
ipython
```

生成hash密码

```
>>> from jupyter_server.auth import passwd
>>> passwd()
# 根据提示输入密码，会得到类似下面的秘钥，将秘钥记录
```

![image-20231118021133061](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/202311180211572.png)

输入`exit()`退出ipython环境

### 第三步，生成配置文件

```bash
jupyter-lab --generate-config
```

返回：

```
Writing default config to: /home/mastermao/.jupyter/jupyter_lab_config.py
```

### 第四步，修改配置文件

```bash
sudo nano ~/.jupyter/jupyter_lab_config.py
```

```ini
c.ServerApp.allow_remote_access = True
c.ServerApp.ip = '*'

# 启动时不自动打开浏览器 
c.ServerApp.open_browser = False
c.LabServerApp.open_browser = False
c.ExtensionApp.open_browser = False
c.LabApp.open_browser = False

c.ServerApp.password_required = True
# 添加刚刚生成的密钥
c.ServerApp.password = 'argon2:$argon2id$v=19$m=10240,t=10,p=8$WPTImP4LkbLfUZEArh/lgQ$dqxJA33ztdvsFM4OcH0/hnVIcG87hwHMhhpetvOo67Y'

# 修改端口号(可选)
c.ServerApp.port = 8800
```

### 第五步，设置开机启动（可选）

添加`jupyter.service`到`/etc/systemd/system/`目录

```
sudo nano /etc/systemd/system/jupyter.service
```

```ini
[Unit]
Description=Jupyter Notebook
After=network.target
[Service]
Type=simple
ExecStart=/home/mastermao/anaconda3/bin/jupyter-lab --config=/home/mastermao/.jupyter/jupyter_lab_config.py --no-browser
User=user
Group=user
WorkingDirectory=/home/mastermao/
Restart=always
RestartSec=10
[Install]
WantedBy=multi-user.target
```

设置开机启动

```bash
sudo systemctl enable jupyter.service
sudo systemctl start jupyter.service
```

## 贰丨远程访问

### 第一步，SSH连接目标服务器

```bash
ssh mastermao@192.168.0.107 -p 22
```

### 第二步，启动Jupyter Lab

```bash
jupyter lab
```

![image-20231118022621784](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/202311180226269.png)

### 第三步，浏览器访问

浏览器输入`192.168.0.107:8800`

输入密码即可进入

![image-20231118022651168](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/202311180226219.png)

![image-20231118022738029](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/202311180227081.png)

## 叁丨配置`jupyter lab`

### 1. 中文支持（可选）

```bash
pip install jupyterlab-language-pack-zh-CN -i https://pypi.tuna.tsinghua.edu.cn/simple
```

在Settings —— Language —— 选择中文

### 2. 代码自动补全（可选）[^2]

```bash
pip install jupyterlab-lsp -i https://pypi.tuna.tsinghua.edu.cn/simple
 
pip install -U jedi-language-server -i https://pypi.tuna.tsinghua.edu.cn/simple
```

开启自动补全：

设置 —— 设置编辑器 —— 代码补全 —— 勾选`启用自动补全`

![image-20231118024321236](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/202311180243386.png)

## 肆丨Pycharm配置远程jupyter lab

新建`.ipynb`文件 —— 配置Jupyter服务器 —— 配置的服务器 —— 输入目标Jupyter Lab的IP及端口，如：

```bash
http://192.168.0.108:8889
```



[^1]: 知乎，@Saito，[Ubuntu22.04配置jupyter-lab并开启远程访问与开机自启动](https://zhuanlan.zhihu.com/p/573899572)
[^2]: 博客园，@oneDonkey，[Jupyter Lab安装，中文设置，自动补全与代码提示](https://www.cnblogs.com/gitLab/p/17398483.html)
