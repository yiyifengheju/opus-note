---
title: 🐖 使用nuitka打包Python工具
date: 2025.05.30
comments: true
---

### 第一步，安装`Nuitka`

```bash
rye add nuitka
```

### 第二步，准备Python脚本

确保脚本正常运行不报错

### 第三步，使用`Nuitka`打包

命令行中：

```bash
nuitka --standalone --onefile main.py
```

> * `--standalone`：生成独立的可执行文件，包含所有依赖项
> * `--onefile`：将所有内容打包为一个单独的exe文件



!!! note "注意事项"
	
	1. Nuitka会下载C编译器（MinGW或MSVC）
	2. 确保依赖库都已安装