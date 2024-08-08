---
title: 🍙 NPM查看软件版本
comments: true
---

> 以PicGo为例

## 壹丨查看服务器上版本信息

### 1. 查看服务器上包的最新版本信息

```bash
npm view picgo version
```

```
1.5.5
```

### 2. 查看`npmjs`服务器上包的最新版本信息

```bash
npm view picgo versions
```

```
[
  '1.0.0',          '1.0.1',          '1.0.2',          '1.0.3',
  ...
  '1.5.5'
]
```

使用`info`获取更多信息


```bash
npm info picgo
```

```
picgo@1.5.5 | MIT | deps: 25 | versions: 97
A tool for picture uploading
https://github.com/PicGo/PicGo-Core#readme

...

dist-tags:
alpha: 1.5.0-alpha.17  latest: 1.5.5          

published a week ago by molunerfinn <marksz@teamsz.xyz>
```

## 贰丨查看本地安装包的版本信息

### 1. 查看本地版本信息

```bash
npm ls picgo
```

```
/home/mastermao/Downloads
└── (empty)
```

### 2. 查看本地全局安装的版本信息

```bash
npm ls picgo -g
```

```
/usr/local/lib
└── picgo@1.5.5
```













