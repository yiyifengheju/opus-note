---
title: 🍉 Ubuntu安装PicGo
date: 2023.10.13
comments: true
---

## 壹丨使用`npm`安装

### 1. 安装`nodejs`

```bash
sudo apt install npm
```

查看`npm`版本

```
npm -v
```

### 2. 安装`PicGo-Core`

查看当前最新版本

```bash
npm view picgo version
```

```
1.5.5
```

安装

```bash
sudo npm install picgo@1.5.5 -g
```

### 3. 修改配置文件

```bash
sudo nano ~/.picgo/config.json
```

```json
{
  "picBed": {
    "current": "tcyun",
    "uploader": "tcyun",
    "tcyun": {
      "_configName": "cos",
      "version": "v5",
      "secretId": "AKxxxxxxxxxxxxxxxxxx",
      "secretKey": "i9xxxxxxxxxxxxxxxxxxxxxx",
      "appId": "13xxxxxxxxxxxxx",
      "bucket": "mxxxxxxxxxxxxxxx",
      "area": "axxxxxxxxx",
      "path": "mxxxxxxxxxxxxxx"
    }
  }
}
```

## 贰丨安装`PicGo` APP[^1]

官方网站：https://molunerfinn.com/PicGo/

下载后安装

```bash
sudo snap install picgo_2.4.0-beta.4_amd64.snap --dangerous
```

其中`--dangerous`为忽略签名。

!!! warning "使用Typora上传图片出错"


[^1]: @码客说，[Ubuntu常用环境配置及常用软件安装](https://www.psvmc.cn/article/2022-05-30-ubuntu-software.html)
