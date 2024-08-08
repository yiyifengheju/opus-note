---
title: 🏈 Conda常用操作
comments: true
---

### 1. 常用操作

查看版本

```bash
conda -V
```

### 2. Conda新建环境

以Python 3.11为例：

```bash
conda create -n MasterMao311 python=3.11
```

激活虚拟环境

```bash
conda activate MasterMao311
```

退出虚拟环境

```bash
conda deactivate
```

??? note "取消自动激活conda环境（不推荐）"

    安装Anaconda后，每次启动终端都会自动进入base环境。
    
    每次手动退出conda：
    
    ```bash
    conda deactivate
    ```
    
    上述命令需要每次执行，可添加配置：
    
    ```bash
    conda config --set auto_activate_base false
    ```
    
    *进入conda环境对正常操作无影响，所以没必要取消自动激活conda*

