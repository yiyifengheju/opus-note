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


### 1. FFTW包

安装命令：

```bash
pacman -S mingw-w64-clang-x86_64-fftw
```

### 2. gsl包

安装命令：

```bash
pacman -S mingw-w64-clang-x86_64-gsl
```

### 3. Lapack包

依赖BLAS，这里安装`openblas`：

```bash
pacman -S mingw-w64-clang-x86_64-openblas
pacman -S mingw-w64-clang-x86_64-openblas64
```

```bash
pacman -S mingw-w64-clang-x86_64-blas
pacman -S mingw-w64-clang-x86_64-blas64
pacman -S mingw-w64-clang-x86_64-cblas
pacman -S mingw-w64-clang-x86_64-cblas64
pacman -S mingw-w64-clang-x86_64-lapack
pacman -S mingw-w64-clang-x86_64-lapack64
pacman -S mingw-w64-clang-x86_64-lapacke
pacman -S mingw-w64-clang-x86_64-lapacke64
```

> 只安装下面64位的会出现找不到BLAS的情况
