---
title: I Linux压缩命令汇总
comments: true
date: 2024.02.03
---

Linux压缩命令常用的有：`tar`、`tgz`、`gzip`、`zip`、`rar`

## 零丨汇总

| 压缩类型       | 压缩命令                       | 解压缩命令              |
| -------------- | ------------------------------ | ----------------------- |
| `.tar`         | `tar -cvf file.tar file`       | `tar -xvf file.tar`     |
| `.tgz`（推荐） | `tar -zcvf file.tgz file`      | `tar -zxvf file.tgz`    |
| `.gzip`        | `gzip -r examples.gz examples` | `gunzip -r examples.gz` |
| `.zip`         | `zip -r examples.zip examples` | `unzip examples.zip`    |
| `.rar`         | `rar -a examples.rar examples` | `unrar examples.rar`    |

## 壹丨`tar`

### 1. 压缩命令

```bash
tar -cvf examples.tar files|dir
```

说明：

```bash
-c, --create  create a new archive 创建一个归档文件
-v, --verbose verbosely list files processed 显示创建归档文件的进程
-f, --file=ARCHIVE use archive file or device ARCHIVE  后面要立刻接被处理的档案名,比如--file=examples.tar
```

举例：

```bash
tar -cvf file.tar file1       #file1文件
tar -cvf file.tar file1 file2 #file1，file2文件
tar -cvf file.tar dir         #dir目录
```

### 2. 解压命令

```bash
tar -xvf examples.tar （解压至当前目录下）
tar -xvf examples.tar  -C /path (/path 解压至其它路径)
```

说明：

```bash
-x, --extract, extract files from an archive 从一个归档文件中提取文件
```

举例：

```bash
tar -xvf file.tar
tar -xvf file.tar -C /temp  #解压到temp目录下
```

## 贰丨`tgz`

>`tar`可以通过参数`-z`同时调用`gzip`对tar包进行压缩
>
>`.tar.gz`和`.tgz`格式是相同的，命名不同而已

### 1. 压缩命令

```bash
tar -zcvf examples.tgz examples (examples当前执行路径下的目录)
```

说明：

```bash
-z, --gzip filter the archive through gzip 通过gzip压缩的形式对文件进行归档
```

举例：

```bash
tar -zcvf file.tgz dir
```

### 2. 解压缩命令

```bash
tar -zxvf examples.tar （解压至当前执行目录下）
tar -zxvf examples.tar  -C /path (/path 解压至其它路径)
```

举例：

```bash
tar -zxvf file.tgz
tar -zxvf file.tgz -C /temp
```

## 叁丨`gzip`

> `gzip`只能压缩文件不能打包，并不会将某一目录打包为`xxx.gz`，而是将该目录下的所有文件分别压缩为`.gz`

### 1. 压缩命令

```bash
gzip -r -6 examples.gz examples
```

说明：

```bash
-z, --gzip filter the archive through gzip 通过gzip压缩的形式对文件进行归档
-6 指定压缩效率，默认为6，范围1到9，1的压缩效率最小压缩速度最快，9反之
```

### 2. 解压缩命令

```bash
gzip -dr examples.gz
gunzip -r examples.gz
```

## 肆丨`zip`

>zip 格式是开放且免费的，广泛使用在 Windows、Linux、MacOS 平台。缺点是压缩率不高，不如`rar`及`.tar.gz` 等格式。

### 1. 压缩命令

```bash
zip -r examples.zip examples (examples为目录)
```

说明：

```bash
-r 递归处理，将指定目录下的所有文件和子目录一并处理。
```

### 2. 解压缩命令

```bash
unzip examples.zip
```

## 伍丨`rar`

### 1. 压缩命令

```bash
rar -a examples.rar examples
```

### 2. 解压缩命令

```bash
rar -x examples.rar
unrar examples.rar
```