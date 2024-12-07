---
title: 🐱 PySide6踩坑记
date: 2021-11-28
comments: true
---
## 壹丨环境配置

第一步，Pycharm 中新建工程，命名 `MasterFusion`

第二步，pip 安装pyside6

```bash
pip install PySide6
```

第三步，配置 QtDesigner

Settings —— Tools —— External Tools —— 加号

```bash
# name
QtDesigner6
# Program
C:\Users\MasterMao\anaconda3\envs\MasterFusion\Lib\site-packages\PySide6\designer.exe
# Working directory
$FileDir$
```

文件资源管理器定位到 `C:\Users\MasterMao\anaconda3\envs\MasterFusion\Lib\site-packages\PySide6`，新建文件夹 `./bin`，将PySide6根目录下 的`uic.exe`、`Qt6Core.dll` 拷贝到 `bin` 目录下



## 贰丨使用 PyDracula 模板

项目地址：https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6

文件说明：

> **main.py**: 初始化文件
>
> **main.ui**: Qt Designer 工程文件
>
> **resouces.qrc**: Qt Designer 资源文件，使用 Designer 添加资源
>
> **setup.py**: 使用 cx-Freeze 编译程序
>
> **themes/**: 主题文件
>
> **modules/**: PyDracula GUI 的模块
>
> **modules/app_funtions.py**: 此处添加应用程序
>
> **modules/app_settings.py**: 用户界面全局变量
>
> **modules/resources_rc.py**: 使用Python命令编译resource.qrc文件，命令为 `pyside6-rcc resources.qrc -o resources_rc.py`
>
> **modules/ui_functions.py**: 仅为与用户界面相关的功能
>
> **modules/ui_main.py**: Qt Designer导出的界面文件。可编译命令：`pyside6-uic main.ui> ui_main.py `
>
> 需要将原文中 `import resources_rc` 改为 `from. Resoucers_rc import *` 
>
> **images/**: 将图片和图标放在此处。 `pyside6-rcc resources.qrc -o resources_rc.py`.