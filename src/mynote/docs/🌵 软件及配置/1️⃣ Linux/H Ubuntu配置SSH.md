---
title: 🎈 Ubuntu配置SSH
comments: true
date: 2023.11.28
---

### 第一步，更新

```bash
sudo apt update
```

```bash
sudo apt upgrade
```

### 第二步，配置SSH

安装SSH服务：

```bash
sudo apt-get install ssh
```

启动SSH：

```
sudo service ssh start
```

设置开机启动：

```bash
sudo systemctl enable ssh
```

修改配置文件：

```bash
sudo nano /etc/ssh/sshd_config
```

```bash
# 端口，默认22
Port 22
```

!!! note "其他操作"

	关闭SSH：
	
	```bash
	sudo service ssh stop
	```
	
	查看SSH状态：
	
	```bash
	sudo service ssh status
	```

### 3. 启动ssh服务

```bash
sudo service ssh --full-restart
```

