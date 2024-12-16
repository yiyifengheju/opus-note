---
title: 🧩 Rye踩坑记录
comments: true
---

## 壹丨本地算法库更新后，使用`remove`和`add`不能生效

【问题描述】

本地算法库更新后，使用`remove`指令移除算法库，再重新`add`，发现算法库没有更新

【解决方法】

需要在移除算法库后**执行同步**，再重新添加

```bash
# 第一步，移除算法库
rye remove my_project
# 第二步，执行同步
rye sync
# 第三步，重新安装算法库
rye add my_project --path path/to/my_project
# 第四步，执行同步
rye sync
```

## 贰丨网络代理原因导致Rye安装不上

【问题描述】

由于网络代理原因，无法安装Rye，显示拷贝git仓库连接超时

【解决方法 1】

从其他Windows系统上将`~/.rye`文件夹拷贝，然后修改代理（`~/.rye/config.toml`）：

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

【解决方法 2】（适用于Linux）

第一步，设置代理

```bash
export http_proxy='http://<UserName>:<Password>@<IP>:<PORT>'
export https_proxy='http://<UserName>:<Password>@<IP>:<PORT>'
```

第二步，执行`./rye-x86_64-linux`，正常安装

## 叁丨`rye build`报错

【问题描述】

执行`rye build`命令，显示连接超时

【问题解析】

虽然使用了`uv`替代`pip`，但在`rye build`时还是依赖`pip`命令，由于`pip`源的原因，无法直接使用

【解决方法 1】

修改全局`pip`源：位于`~/pip/pip.conf`

【解决方法 2】

修改Rye的`config.toml`，添加源

```toml title="~/.rye/config.toml"
[[sources]]
name = "example"
url = "https://example.cn/simple"
```

## 肆丨添加了弃用的库，导致后续命令一直报错

【问题复现】

```bash
# python=3.12
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

在这之后，使用其他命令依旧报同样的错

【问题解析】

在Python3.12中，distribute库已经弃用，但是上述`rye add distribute`的操作依旧会添加这个依赖

【修复方法】

手动修改`pyproject.toml`文件

```bash
nano pyproject.toml
```

在`[project]`下`dependencies`中，删除`"distribute>=0.7.3"`，然后重新执行同步。

## 伍丨CMake配置错误导致无法安装库

【问题复现】

```bash
mastermao@MasterMao:~/projects/test_py311$ rye add pycaret
Initializing new virtualenv in /home/mastermao/projects/test_py311/.venv
Python version: cpython@3.12.3
Added pycaret>=3.3.2 as regular dependency
Reusing already existing virtualenv
Generating production lockfile: /home/mastermao/projects/test_py311/requirements.lock
Generating dev lockfile: /home/mastermao/projects/test_py311/requirements-dev.lock
Installing dependencies
Resolved 98 packages in 75ms
   Built test-py311 @ file:///home/mastermao/projects/test_py311
error: Failed to prepare distributions
  Caused by: Failed to fetch wheel: lightgbm==4.4.0
  Caused by: Failed to build: `lightgbm==4.4.0`
  Caused by: Build backend failed to build wheel through `build_wheel()` with exit status: 1
--- stdout:
*** scikit-build-core 0.9.8 using CMake 3.30.0 (wheel)
*** Configuring CMake...
loading initial cache file /tmp/tmpxha8pri3/build/CMakeInit.txt
-- Configuring incomplete, errors occurred!
--- stderr:
CMake Error at /home/mastermao/.cache/uv/builds-v0/.tmpGTUObH/lib/python3.12/site-packages/cmake/data/share/cmake-3.30/Modules/CMakeDetermineCCompiler.cmake:49 (message):
  Could not find compiler set in environment variable CC:

  clang -pthread.
Call Stack (most recent call first):
  CMakeLists.txt:36 (project)


CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage

*** CMake configuration failed
---
error: Installation of dependencies failed in venv at /home/mastermao/projects/test_py311/.venv. uv exited with status: exit status: 2
```

【解决方法】

修改`~/.bashrc`，添加：

```bash
export CXX=/usr/bin/g++
export CC=/usr/bin/gcc
```

### 陆丨无法生成虚拟环境

【问题复现】

```bash
PS D:\Projects\PycharmProjects\koko-learn> rye sync
Downloading cpython@3.11.10
Checking checksum
Unpacking
Downloaded cpython@3.11.10
Reusing already existing virtualenv
Generating production lockfile: D:\Projects\PycharmProjects\koko-learn\requirements.lock
Generating dev lockfile: D:\Projects\PycharmProjects\koko-learn\requirements-dev.lock
Installing dependencies
  Caused by: Failed to build `koko-learn @ file:///D:/Projects/PycharmProjects/koko-learn`
  Caused by: Failed to create temporary virtualenv
  Caused by: Could not find a suitable Python executable for the virtual environment based on the interpreter: C:\Users\mastermao\.rye\py\cpython@3.11.8\install\python.exe
error: Installation of dependencies failed in venv at D:\Projects\PycharmProjects\koko-learn\.venv. uv exited with status: exit code: 2
```

【解决方案】

第一步，删除`.venv`目录

第二步，重新`rye sync`

如果不成功，将目录换个名字

### 柒丨证书错误

【问题复现】

```bash
PS C:\Users\mastermao\py311> rye sync
Reusing already existing virtualenv
Generating production lockfile: C:\Users\mastermao\py311\requirements.lock
error: Failed to download `tqdm==4.67.1`
  Caused by: Request failed after 3 retries
  Caused by: error sending request for url (https://files.pythonhosted.org/packages/d0/30/dc54f88dd4a2b5dc8a0279bdd7270e735851848b762aeb1c1184ed1f6b14/tqdm-4.67.1-py3-none-any.whl.metadata)
  Caused by: client error (Connect)
  Caused by: invalid peer certificate: UnknownIssuer
error: could not write production lockfile for project

Caused by:
    Failed to run uv compile C:\Users\mastermao\AppData\Local\Temp\.tmpjWwcb9\requirements.txt. uv exited with status: exit code: 2
```

【解决方案】

方法1：重新链接证书（不奏效）[^1]

方法2：换源（可能和公司网络有关）

```toml
[[sources]]
name = "douban"
url = "https://mirrors.cloud.tencent.com/pypi/simple/"
```



[^1]: Hatena Blog，@もぐわい (id:b1u3)，[Rye で invalid peer certificate が出るので、インストールできない](https://b1u3.hateblo.jp/entry/2024/10/11/233230)
