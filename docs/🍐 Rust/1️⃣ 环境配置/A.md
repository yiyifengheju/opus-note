---
title: 🎀 Rust安装
date: 2024.07.01
comments: true
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

