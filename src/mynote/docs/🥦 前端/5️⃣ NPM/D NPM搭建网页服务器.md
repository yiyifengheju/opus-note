---
title: D NPM搭建网页服务器
comments: true
---

本地快速搭建一个简单的Web服务器来展示网页

### 1. http-server工具

一个简单的命令行工具，可以启动一个基于Node.js的HTTP服务器

```bash
npm install -g http-server
```

进入项目目录，执行：

```bash
http-server
```

然后在`http://localhost:8000`展示项目

### 2. live-server

一个支持热重载的开发服务器，在保存文件时自动重新加载页面

```bash
npm install -g live-server
```

进入项目目录，执行：

```bash
live-server
```

然后在`http://localhost:8080`展示项目



!!! note "上述工具仅适合本地开发测试，如果要在生产环境中托管项目，需要使用Nginx或Apache等服务器"