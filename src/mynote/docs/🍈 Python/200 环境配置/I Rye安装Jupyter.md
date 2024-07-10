---
title: Rye安装Jupyter
comments: true
---

目标：Ubuntu使用Rye虚拟环境安装Jupyter，并在Windows端实现远程访问

前提环境及路径：

```bash
# rye安装在用户目录下：
~/.rye

# 用户目录下创建虚拟环境`mao_py311`：
~/mao_py311
```

## 壹丨安装Jupyter

第一步，安装Jupyter：

```bash
# 安装notebook
rye add notebook

# or安装jupyter lab
rye add jupyterlab

# 更新环境
rye sync
```

第二步，激活虚拟环境：

```bash
. .venv/Scripts/activate
```

第三步，启动jupyter：

```bash
# 启动notebook
jupyter notebook

# 启动jupyter lab
jupyter lab
```

## 贰丨配置远程访问

### 第一步，配置Jupyter Lab访问密码

激活jupyter环境并启动ipython

```bash
cd ~/mao_py311
# 激活环境
. .venv/bin/activate
# 打开IPython
ipython
```

生成hash密码

```python
>>> from jupyter_server.auth import passwd
>>> passwd()
# 根据提示输入密码，会得到类似下面的秘钥，将秘钥记录
# 'argon2:$argon2id$v=19$m=10240,t=10,p=8$CNeWCHTKLLYWMefcQf92YQ$UtKecua0NRgBiv554kegnT6lHPP57ccOvT5mlLibG9o'
```

输入`exit()`退出ipython环境

### 第二步，生成配置文件

同样在上述路径和jupyter环境下

```bash
jupyter-lab --generate-config
# 返回：Writing default config to: /home/mao/.jupyter/jupyter_lab_config.py
```

### 第三步，修改配置文件

修改上述配置文件

```bash
sudo nano ~/.jupyter/jupyter_lab_config.py
```

```python
# 允许远程访问
c.ServerApp.allow_remote_access = True
c.ServerApp.ip = '*'

# 启动时不自动打开浏览器 
c.ServerApp.open_browser = False
c.LabServerApp.open_browser = False
c.ExtensionApp.open_browser = False
c.LabApp.open_browser = False

c.ServerApp.password_required = True
# 添加刚刚生成的密钥
c.ServerApp.password = 'argon2:$argon2id$v=19$m=10240,t=10,p=8$CNeWCHTKLLYWMefcQf92YQ$UtKecua0NRgBiv554kegnT6lHPP57ccOvT5mlLibG9o'

# 修改端口号(可选)
c.ServerApp.port = 8880
```

### 第四步，验证

启动jupyter lab

```
# 启用虚拟环境
. ~/mao_py311/.venv/bin/activate

# 启用jupyter lab
jupyter lab
```

然后，在本地Windows上打开目标服务器地址：`xx.xx.xx.xx:8880`，输入在ipython中设置的明文密码即可使用

## 叁丨踩坑指南

### 1. 虚拟环境无法直接使用jupyter lab【问题已过期】

问题描述：

```bash
(mao-py311) mao@pekshcsitd33451:~/Project/009_PWV/EP02_mao$ jupyter lab

Command 'jupyter' not found, but can be installed with:
```

问题解析：没有按照`--include-dep`方法安装jupyter，导致`jupyter`命令没有添加到`~/.rye/shims`

解决方法：卸载重装

```bash
rye uninstall jupyter
rye install jupyter --include-dep jupyter-core
```

### 2. 激活虚拟环境失败

问题描述：

```powershell
PS C:\Users\Artmallo\py311> . .\.venv\Scripts\activate
. : 无法加载文件 C:\Users\Artmallo\py311\.venv\Scripts\activate.ps1，因为在此系统上禁止运行脚本。有关详细信息，请参阅 https:/go.microsoft.com/fwlink/?LinkID=135170 中的 about_Execution_Policies。
```

问题解析：Windows中运行`activate.bat`会在同级目录生成`activate.ps1`，PowerShell默认不允许执行`*.ps1`脚本

解决方法：

第一步：管理员打开PowerShell

第二步：

```powershell
Set-ExecutionPolicy RemoteSigned
```

## 参考：

[^1]: Rye，[官方文档](https://rye-up.com/guide/commands/install/)
[^2]: Github issues，[`rye install jupyter` does not add `jupyter` to ~/.rye/shims #65 ](https://github.com/astral-sh/rye/issues/65)
[^3]: 一一风和橘's笔记，@一一风和橘，[Ubuntu设置Jupyter Lab远程访问](https://note.mastermao.cn/100%20%E8%BD%AF%E4%BB%B6%E5%8F%8A%E9%85%8D%E7%BD%AE/101%20Linux/G%20Ubuntu%E9%85%8D%E7%BD%AEJupyterLab%E8%BF%9C%E7%A8%8B%E8%AE%BF%E9%97%AE/)