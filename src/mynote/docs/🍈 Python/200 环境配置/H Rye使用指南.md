---
title: Rye使用指南
comments: true
---

“Rye 是一个全面的 Python 项目和包管理解决方案。”——[Rye官网](https://rye-up.com/)

> 个人使用rye主要涉及两个用途：
>
> 1. 创建算法库独立工程。这需要明确各依赖项的版本，且与其他项目隔离，以保证最少的额外依赖。
> 2. 作为虚拟环境，供各个小项目使用。

## 壹丨情境一：创建独立工程

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


## 叁丨踩坑指南

### 1. 更新本地算法库

问题描述：本地算法库更新后，使用`remove`指令，再重新`add`，发现算法库没有更新


解决方法：需要在移除后执行同步，再重新添加

```bash
rye remove my_project
rye sync
```

然后重新安装，再执行同步

```bash
rye add my_project --path path/to/my_project
rye sync
```

### 2. Rye安装不上

问题描述：由于网络原因，无法安装Rye，显示拷贝git仓库连接超时

解决方法：从其他Windows系统上将`~/.rye`文件夹拷贝，然后修改代理（`~/.rye/config.toml`）：

```toml title="~/.rye/config.toml"
[proxy]
# the proxy to use for HTTP (overridden by the http_proxy environment variable)
http = "http://example.com:8080"
# the proxy to use for HTTPS (overridden by the https_proxy environment variable)
https = "http://example.com:8080"
```

然后执行Rye升级命令

```bash
rye self update
```

然后将`~/.rye/shims`路径添加到系统环境变量

### 3. `rye build`报错

问题描述：执行`rye build`命令，显示连接超时

问题解析：虽然使用了uv替代pip，但在build时还是依赖pip命令，由于pip源的原因，无法直接使用

解决方法：修改全局pip源（位于`~/pip/pip.conf`）或修改Rye的`config.toml`

```toml title="~/.rye/config.toml"
[[sources]]
name = "example"
url = "https://example.cn/simple"
```

### 4. 添加了弃用的库，导致一直报错

问题复现：

```bash
rye add distribute

# Added distribute>=0.7.3 as regular dependency
# Reusing already existing virtualenv
# Generating production lockfile: /home/mao/py312/requirements.lock
# error: Failed to download and build: distribute==0.7.3
#   Caused by: Failed to build: distribute==0.7.3
#   Caused by: Build backend failed to determine metadata through `prepare_metadata_for_build_wheel`:
# --- stdout:
# 
# --- stderr:
# usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
#    or: setup.py --help [cmd1 cmd2 ...]
#    or: setup.py --help-commands
#    or: setup.py cmd --help
#
# error: invalid command 'dist_info'
# ---
# error: could not write production lockfile for project
#
# Caused by:
#     failed to generate lockfile
```

在这之后使用其他命令依旧报同样的错

问题解析：在Python3.12中，distribute库已经弃用，但是上述`rye add distribute`的操作依旧会添加这个依赖（是Bug）

修复方法：手动修改`pyproject.toml`文件

```bash
nano pyproject.toml
```

在`[project]`下`dependencies`中，删除`"distribute>=0.7.3",`，然后重新同步。

## 参考：

[^1]: Rye，[官方文档](https://rye-up.com/)
[^2]: 个人博客，@Yunfeng，[Rye:一个实验性质的Python包管理系统](https://vra.github.io/2023/05/17/rye-intro/)