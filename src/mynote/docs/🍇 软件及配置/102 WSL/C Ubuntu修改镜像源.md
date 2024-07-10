---
title: C Ubuntu修改镜像源
comments: true
---

常用的镜像源有清华镜像源[^1]、中科大镜像源[^2]等。

第一步，修改配置文件`/etc/apt/sources.list`

```bash
sudo nano /etc/apt/sources.list
```

以Ubuntu 20.04 LTS为例：

```bash title="/etc/apt/sources.list"
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
```

***注意***：要选择对应Ubuntu版本的软件源

第二步，更新索引

```bash
sudo apt update
```

















[^1]: 清华大学开源镜像站，[Ubuntu 镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/)
[^2]: 中科大开源镜像站，[Ubuntu 源使用帮助](https://mirrors.ustc.edu.cn/help/ubuntu.html)