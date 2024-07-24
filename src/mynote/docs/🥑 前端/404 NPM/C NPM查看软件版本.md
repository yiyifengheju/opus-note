---
title: B NPM查看软件版本
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
  '1.0.4',          '1.0.5',          '1.0.6',          '1.0.7',
  '1.0.8',          '1.0.9',          '1.0.10',         '1.1.0',
  '1.1.1',          '1.1.2',          '1.1.3',          '1.1.4',
  '1.1.5',          '1.1.6',          '1.1.7',          '1.1.8',
  '1.1.9',          '1.1.10',         '1.1.11',         '1.1.12',
  '1.1.13',         '1.1.14',         '1.1.15',         '1.1.16',
  '1.2.0',          '1.2.1',          '1.2.2',          '1.2.3',
  '1.2.4',          '1.2.5',          '1.2.6',          '1.2.7',
  '1.2.8',          '1.2.9',          '1.2.10',         '1.3.0',
  '1.3.1',          '1.3.2',          '1.3.3',          '1.3.4',
  '1.3.5',          '1.3.6',          '1.3.7',          '1.4.0',
  '1.4.1',          '1.4.2',          '1.4.3',          '1.4.4',
  '1.4.5',          '1.4.6',          '1.4.7',          '1.4.8',
  '1.4.9',          '1.4.10',         '1.4.11',         '1.4.12',
  '1.4.13',         '1.4.14',         '1.4.15',         '1.4.16',
  '1.4.17',         '1.4.18',         '1.4.19',         '1.4.20',
  '1.4.21',         '1.4.23',         '1.4.24',         '1.4.25',
  '1.4.26',         '1.5.0-alpha.0',  '1.5.0-alpha.1',  '1.5.0-alpha.2',
  '1.5.0-alpha.3',  '1.5.0-alpha.4',  '1.5.0-alpha.5',  '1.5.0-alpha.6',
  '1.5.0-alpha.7',  '1.5.0-alpha.8',  '1.5.0-alpha.9',  '1.5.0-alpha.10',
  '1.5.0-alpha.11', '1.5.0-alpha.12', '1.5.0-alpha.13', '1.5.0-alpha.14',
  '1.5.0-alpha.15', '1.5.0-alpha.16', '1.5.0-alpha.17', '1.5.0',
  '1.5.1',          '1.5.2',          '1.5.3',          '1.5.4',
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

keywords: picture, upload, util

bin: picgo

dist
.tarball: https://registry.npmjs.org/picgo/-/picgo-1.5.5.tgz
.shasum: fa9a5d07d3552036c2cc8b1455bec1c3a2086183
.integrity: sha512-GSfDVR+b6SgibYDQ0eqNKmhmiMWDyNVppq+qKNKyf38VATX/U0ompSS2XgoPAn8Lr7pTddbXgqxfmFiLLXN7LA==
.unpackedSize: 808.1 kB

dependencies:
@picgo/i18n: ^1.0.0       cross-spawn: ^6.0.5       image-size: ^0.8.3        mime-types: 2.1.33        
@picgo/store: ^2.0.2      dayjs: ^1.7.4             inquirer: ^6.0.0          minimatch: ^3.0.4         
axios: ^0.27.2            download-git-repo: ^3.0.2 is-wsl: ^2.2.0            minimist: ^1.2.5          
chalk: ^2.4.1             ejs: ^2.6.1               js-yaml: ^4.1.0           qiniu: ^7.2.1             
commander: ^8.1.0         fs-extra: ^6.0.1          lodash: ^4.17.21          resolve: ^1.8.1           
comment-json: ^2.3.1      globby: ^11.0.4           md5: ^2.2.1               rimraf: ^3.0.2            
(...and 1 more.)

maintainers:
- molunerfinn <marksz@teamsz.xyz>

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













