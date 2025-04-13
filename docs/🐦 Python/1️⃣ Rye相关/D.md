---
title: 配置项目A调用项目B
date: 2025.04.11
---

## 壹丨背景：怎样调用自己本地算法库`koko_learn`？

### 方法1：将算法库`koko_learn`打包，然后在目标项目中安装

> 缺点：
> * 算法库有一点改动都要重新打包、重新安装，非常麻烦
> * 存在算法库依赖与新项目依赖版本不一致问题。如算法库基于`python 3.11`，新项目依赖于`python 3.12`，个人使用实在没必要去解决一些兼容性问题

!!! warning "所以最好所有项目都使用同一个python大版本，例如当前使用的3.11.x版本"


### 方法2：将目标项目放在算法库`koko_learn`同级目录下

例如，目录设置为：

```bash
D:\PROJECTS\PYCHARMPROJECTS\KOKO_LEARN
├─.venv
└─src
    ├─koko_learn
    └─Test0411
```

在项目`Test0411`中可以直接使用：

```python
from koko_learn import xxx
```

>缺点：使用`ruff`作为格式化工具时，当整个工程变得庞大后，`ruff`将运行缓慢，十分影响效率

### 方法3：使用绝对路径引用

在目标项目的`pyproject.toml`中添加依赖：

```toml
dependencies = [
    "koko_learn @ file:///D:/Projects/PycharmProjects/koko_learn"
]
```

* windows路径需要三个斜杠（`file:///`）
* 指向的目标路径要包含`pyproject.toml`或`setup.py`

缺点：依旧需要使用`koko_learn`的相关依赖


参考：
[1]:https://github.com/astral-sh/uv/issues/10641