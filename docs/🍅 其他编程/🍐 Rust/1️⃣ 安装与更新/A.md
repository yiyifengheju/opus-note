---
title: 🎀 Rust安装
date: 2024.07.01
---


第一步，官网下载`rustup-init.ext`到`~/Downloads`

第二步，打开Powershell，配置代理

```powershell
$proxy='http://<UserName>:<Password>@<IP>:<PORT>'

$ENV:HTTP_PROXY=$proxy 
$ENV:HTTPS_PROXY=$proxy
```

然后：

```powershell
$ENV:RUSTUP_DIST_SERVER='https://mirrors.ustc.edu.cn/rust-static' 
$ENV:RUSTUP_UPDATE_ROOT='https://mirrors.ustc.edu.cn/rust-static/rustup'
```

第三步，安装

```powershell
cd Downloads
.\rustup-init.exe
```

> 使用GNU版本，避免安装Visual Studio
>
> 第一步，选择`2)  Customize installation`
>
> 第二步，`Default host triple? [x86_64-pc-windows-msvc]`下输入`x86_64-pc-windows-gnu`，即自定义成GNU；其他默认
>
> 第三步，修改完成后显示：
>
> ```bash
> Current installation options:
> 
> 
> default host triple: x86_64-pc-windows-gnu
>   default toolchain: stable
>             profile: default
> modify PATH variable: yes
> ```
>
> 选择`1) Proceed with selected options (default - just press enter)`完成安装

## 踩坑指南

### 1. 报错`error: linking with `C:\mingw64\bin\gcc.exe` failed: exit code: 1`

【问题分析】

mingw64不兼容导致，需要替换为UCRT runtime的版本[^1][^2]

【解决方法】

从winlibs.com[^2]下载MinGW64，然后替换原有文件





[^1]: GitHub Issues，[error: linking with x86_64-w64-mingw32-gcc failed: exit code: 1 #91146](https://github.com/rust-lang/rust/issues/91146#issuecomment-1556081181)
[^2]: winlibs.com，[WinLibs standalone build of GCC and MinGW-w64 for Windows](https://winlibs.com/)
