---
title: ✌️ PyQt5开发环境配置
comments: true
---
## 壹丨环境

> 包管理器：Anaconda3
>
> IDE：PyCharm

安装：

```bash
pip install pyqt5
```

卸载：


```bash
pip uninstall pyqt5
```



## 贰丨配置QtDesigner和PyUIC

> QtDesigner，可视化UI编辑器
>
> PyUIC，将.ui文件转化为.py文件，以供Python主程序调用。

### 1. Windows下：

PyCharm——Preferences——Tools——External Tools——加号

**QtDesigner：**

>Name：`QtDesigner`
>
>Program：`C:\ProgramData\{Anaconda安装路径}\Library\bin\designer.exe`
>
>Working directory：`$FileDir$`

**PyUIC：**

>Name：`PyUIC`
>
>Program：`C:\ProgramData\{Anaconda安装路径}}\python.exe`
>
>Arguments：`-m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py`
>
>Working directory：`$FileDir$`

### 2. MacOS下：

PyCharm——Preferences——Tools——External Tools——加号

**QtDesigner：**

>Name：`QtDesigner`
>
>Program：`/Users/用户名/opt/anaconda3/bin/Designer.app`
>
>Working directory：`$FileDir$`

**PyUIC：**

>Name：`PyUIC`
>
>Program：`/Users/用户名/opt/anaconda3/bin/python.app`
>
>Arguments：`-m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py`
>
>Working directory：`$FileDir$`



## 叁丨解决logo_rc报错问题

**问题描述：**界面中添加logo，使用PyUIC转换后，以下语句报错

```python
import logo_rc
```

**解决方法：**将`xx.qrc`文件转换为`.py`文件，在命令行：

```bash
pyrcc5 xx.qrc -o xx_rc.py
```

