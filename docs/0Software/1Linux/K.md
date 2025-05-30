---
title: 🐞 配置curl代理
date: 2023.10.13
comments: true
---



家目录新建`.curlrc` 

```bash
sudo nano ~/.curlrc
```

配置代理：

```bash
proxy="http://usr:passwd@ip:port
```

| 关键字   | 含义     | 举例              |
| -------- | -------- | ----------------- |
| `usr`    | 用户名   | `mastermao`       |
| `passwd` | 密码     | `123456`          |
| `ip`     | 代理网址 | `www.example.com` |
| `port`   | 端口号   | `8080`            |

则：

```bash
proxy="http://mastermao:123456@www.example.com:8080
```

验证配置：

```bash
curl www.baidu.com
```

```
<!DOCTYPE html><!--STATUS OK--><html><head><meta http-equiv="Content-Type" content="text/html;charset=utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><meta content="always" name="referrer"><meta name="theme-color" content="#ffffff"><meta name="description" content="全球领先的中文搜索引擎、致力于让网民更便捷地获取信息，找到所求。百度超过千亿的中文网页数据库，可以瞬间找到相关的搜索结果。">
```

