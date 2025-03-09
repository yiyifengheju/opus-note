---
title: 🧁 pacman安装包
comments: true
---

## 壹丨安装基础包

为MinGW64安装：[MSYS2 Packages](https://packages.msys2.org/packages/?repo=mingw64)

> 验证：
>
> ```bash
> pacman -Qs xxx
> ```

安装cmake：

```bash
pacman -S mingw-w64-x86_64-cmake
```

安装gcc：

```bash
pacman -S mingw-w64-x86_64-gcc
```

安装GDB：

```bash
pacman -S mingw-w64-x86_64-gdb
```

### 1. FFTW包

安装命令：

```bash
# 更新数据库
pacman -Syu

pacman -S mingw-w64-x86_64-fftw
```

### 2. gsl包

安装命令：

```bash
pacman -S mingw-w64-x86_64-gsl
```