---
title: D WSL修改初始目录
comments: true
---

## 壹丨WSL初始目录

查看WSL系统文件结构：

```bash
ls /
```

展示出根目录下包含：`dev`、`home`、`media`、`tmp`、`boot`、`etc`、`mnt`、`snap`、`sys`、`usr`等

在打开Terminal时，显示：

```bash
# 在Ubuntu 18.04老版本的WSL上会直接导航到Windows用户目录
mastermao@一一风和橘:/mnt/c/Users/MasterMao$ _

# 在Ubuntu 22.04等新版本上会导航到Linux的用户目录
mastermao@MasterMao:~$ _
```

不论WSL是否将Windows系统的用户文件夹作为初始目录，都不影响其真实home目录为`~`。

## 贰丨修改WSL初始目录[^1]

个人习惯初始目录为Windows的用户文件夹（新安装的WSL2初始文件夹为`~`），修改方法如下：

```bash
sudo nano /etc/profile
```

文件末尾添加：

```
cd /mnt/c/Users/MasterMao
```

[^1]: CSDN，@微步_ym，[Ubuntu：配置环境变量的两种常用方法...](https://blog.csdn.net/yiminghd2861/article/details/98854882)
