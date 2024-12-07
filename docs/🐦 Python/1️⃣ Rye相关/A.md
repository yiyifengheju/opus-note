---
title: 🥎 Rye使用指南
comments: true
---

“Rye 是一个全面的 Python 项目和包管理解决方案。”——[Rye官网](https://rye-up.com/)

> 个人使用rye主要涉及两个用途：
>
> 1. 创建算法库独立工程。这需要明确各依赖项的版本，且与其他项目隔离，以保证最少的额外依赖。
> 2. 作为虚拟环境，供各个小项目使用。

## 壹丨情境一：创建独立工程[^1][^2]

创建一个独立的工程，如新建一个算法库、新建一个大型工程。这里的依赖项避免与其他工程通用

### 第一步，初始化项目

```bash
rye init my_project
```

进入目录，`cd my_project`

### 第二步，指定Python版本

以Python3.11为例：

```bash
rye pin 3.11
```

### 第三步，添加依赖项

以`numpy`、`pandas`为例：

```bash
rye add numpy pandas
```

### 第四步，同步依赖项

将安装Python和依赖包等

```bash
rye sync
```

### 第五步，删除依赖

以`numpy`为例：（之后要执行`rye sync`以同步修改）

```bash
rye remove numpy
rye sync
```

### 第六步，创建工程。

在`src/my_project`下建立工程，目录结构如下：

```bash
my_project
├── README.md
├── dist
│   ├── my_project-0.1.0-py3-none-any.whl
│   └── my_project-0.1.0.tar.gz
├── pyproject.toml
├── requirements-dev.lock
├── requirements.lock
└── src
    └── my_project
        ├── Filtering
        │   ├── __init__.py
        │   └── _hampel.py
        ├── __init__.py
        └── config.py
```

### 第七步，打包

生成可发布的wheel文件。将会在`dist`下创建`.whl`和`.tar.gz`文件，如上述目录结构所示

```bash
rye build
```

### 第八步，上传PyPi

```bash
rye publish
```

## 贰丨情境二：作为虚拟环境

### 第一步，创建虚拟环境

新建环境同上述操作（建议放在用户文件夹下并注明Python版本）

```bash
# 初始化
rye init mao_py311

# 进入项目目录
cd mao_py311

# 设置Python版本
rye pin 3.11

# 添加依赖项
rye add numpy

# 同步依赖
rye sync
```

### 第二步，PyCharm调用

在Pycharm中，右下角 —— 添加新的解释器 —— 添加本地解释器 —— Virtualenv环境 —— 现有 —— 选择上述`~/mao_py311/.venv/Scripts/python.exe`

至此，可以在多个项目中使用同一虚拟环境

### 第三步，添加本地算法库

> 同Rye文档Dependencies —— Git / Local Dependencies

添加本地或git依赖项时，需要传递其他参数，如`--path`、`--git`

```bash
rye add my_project --path path/to/my_project
```


## 参考：

[^1]: Rye，[官方文档](https://rye-up.com/)
[^2]: 个人博客，@Yunfeng，[Rye:一个实验性质的Python包管理系统](https://vra.github.io/2023/05/17/rye-intro/)