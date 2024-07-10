---
title: A WSL安装安装指定版本
comments: true
---



## 壹丨准备工作

### 1. 启用适用于Linux的Windows子系统

PowerShell执行：

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

> 此时安装的是WSL 1

### 2. 启用虚拟机功能

```powershell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

> WSL 2必须开启虚拟机平台功能

## 贰丨切换WSL版本（可选）

### 1. 下载Linux内核更新包（WSL 1升级到WSL 2）

下载地址：[适用于 x64 计算机的 WSL2 Linux 内核更新包](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi){:target="_blank"}

下载后安装`.msi`文件

### 2. 将WSL 2设置为默认版本

```powershell
wsl --set-default-version 2
```

## 叁丨安装指定分发版本

### 1. 第一种，`Microsoft Store`安装Linux分发版（略）

### 2.第二种，`wsl`命令在线安装

首先，使用`wsl --list --online`展示可安装有效分发列表：

```
NAME            FRIENDLY NAME
Ubuntu          Ubuntu
Debian          Debian GNU/Linux
kali-linux      Kali Linux Rolling
openSUSE-42     openSUSE Leap 42
SLES-12         SUSE Linux Enterprise Server v12
Ubuntu-16.04    Ubuntu 16.04 LTS
Ubuntu-18.04    Ubuntu 18.04 LTS
Ubuntu-20.04    Ubuntu 20.04 LTS
```

然后使用`wsl --install -d <分发>`安装，如：

```powershell
wsl --install -d Ubuntu-18.04
```

!!! note

	上述分发列表可能不包含自己想安装的版本，比如`Ubuntu 22.04`

### 3. 第三种，手动下载安装

[官方教程：旧版 WSL 的手动安装步骤](https://learn.microsoft.com/zh-cn/windows/wsl/install-manual#step-2---check-requirements-for-running-wsl-2)提供的可安装版本包括：

```
Ubuntu
Ubuntu 22.04 LTS
Ubuntu 20.04
Ubuntu 20.04 ARM
Ubuntu 18.04
Ubuntu 18.04 ARM
Ubuntu 16.04
Debian GNU/Linux
Kali Linux
SUSE Linux Enterprise Server 12
SUSE Linux Enterprise Server 15 SP2
SUSE Linux Enterprise Server 15 SP3
openSUSE Tumbleweed
openSUSE Leap 15.3
openSUSE Leap 15.2
Oracle Linux 8.5
Oracle Linux 7.9
Fedora Remix for WSL
```

以安装`Ubuntu 22.04 LTS`为例：

下载安装包：

```powershell
Invoke-WebRequest -Uri https://aka.ms/wslubuntu2204 -OutFile Ubuntu.appx -UseBasicParsing
```

安装包位于当前PowerShell目录下，然后安装

```powershell
Add-AppxPackage .\Ubuntu.appx
```