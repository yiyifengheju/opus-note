---
title: ⛄ 安装NodeJS
comments: true
---

## 壹丨安装

=== "Windows"

	[NodeJS官网](https://nodejs.org/zh-cn/)下载安装包并安装

=== "MacOS"

	[NodeJS官网](https://nodejs.org/zh-cn/)下载安装包并安装

=== "Ubuntu"

    以`18.13.0`长期维护版为例
    
    配置版本：
    
    ```bash
    curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    ```
    
    安装：
    
    ```bash
    sudo apt-get install -y nodejs
    sudo apt install npm
    ```

!!! note "验证"

	查看`nodejs`版本
	
	```powershell
	node -v
	```
	
	查看`npm`版本
	
	```
	npm -v
	```

## 贰丨NPM换源

### 1. 修改源

新建并修改`~/.npmrc`

```bash
sudo nano ~/.npmrc
```


```ini title="~/.npmrc"
registry=https://registry.npmmirror.com
```

### 2. 查看源

修改后，查看当前配置的npm源：

```bash
npm config get registry
```

查看完整的npm配置：

```bash
npm config list
```

执行上述命令后，将显示完整的 npm 配置信息，其中包括源（registry）URL、代理设置、缓存路径等。

!!! note "查看全局的npm配置"

    ```bash
    npm config get registry --global
    npm config list --global
    ```

