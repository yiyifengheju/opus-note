---
title: 🍓 系统安装记录
date: 2023.10.13
comments: true
---

## 壹丨安装-GUN GRUB解析[^1]

第一步，首页显示：

```
* Ubuntu
* Advanced options for Ubuntu
```

> `Ubuntu`——直接进入Ubuntu系统

第二步，选择`Advanced options for Ubuntu`页：

```
* resume			Resume normal boot
* clean				Try to make free space
* dpkg				Repair broken packages
* fsck				Check all file systems
* grub				Update grub bootloader
* network			Enable networking
* root				Drop to root shell prompt
* system-summary	System summary
```

> `resume`：恢复正常启动，有的人选这个就可以进入系统
> `clean`：清除磁盘中不必要的文档
> `dpkg`：修复受损的安装包
> `fsck`：磁盘检查与修复
> `grub`：更新grub引导
> `network`：带网络连接的shell界面
> `root`：最高管理员的shell界面
> `system-summary`：查看系统的信息，资料

## 贰丨踩坑记录

### 1. 无法正常进入系统

> Nidia显卡驱动导致开机卡在：
>
> ```
> /dev/sda1: clean, ***files, ***blocks
> ```

原因：显卡驱动问题，导致无法直接进入系统[^2]

进入`Advanced options for Ubuntu`——`resume`可以正常进入系统，然后在`软件和更新`——`附加驱动`中安装推荐的显卡驱动，重启即可

### 2. 从NVIDIA下载安装显卡驱动后无法进入系统

开机卡的位置和上面相同，需要卸载显卡驱动[^3][^4]，再重新安装

选择`Advance Options`，选择`root`，进入管理员模式

#### 方法一：

查看显卡驱动及版本安装情况

```bash
ls /usr/src | grep nvidia
```

进入安装目录，使用自带的卸载命令卸载驱动

```bash
cd /usr/bin
ls nvidia-*
sudo nvidia-uninstall
```

再次查看是否卸载干净

```bash
ls /usr/src | grep nvidia
```

卸载干净所有英伟达驱动

```bash
sudo apt-get remove --purge nvidia-*
```

??? warning "慎用"

	```bash
	sudo apt autoremove
	```

#### 方法二：

查看已安装显卡驱动：

```bash
ls /usr/src | grep nvidia
```

直接卸载显卡驱动

```bash
sudo ./显卡驱动包名称 --uninstall
```

卸载干净

```bash
sudo apt-get purge nvidia*
sudo apt autoremove
```

### 3. 未安装显卡驱动时仍然会卡住

> 报错：
>
> ```
> snd_hda_intel xxx
> ```

原因：HDMI声卡驱动问题，进入Ubuntu后安装显卡驱动即可



参考：

[^1]: CSDN，@ 小白hemu，[ubuntu踩坑笔记--开机进入recovering journal解决方法](https://blog.csdn.net/github_38060285/article/details/130227333)
[^2]: CSDN，@Y1皇_，[Nvidia显卡驱动导致Ubuntu开机卡在/dev/sda1：clean，xxxfiles, xxxblocks的解决](https://blog.csdn.net/YiWHuang/article/details/124624003)
[^3]: CSDN，@竫言，[ubuntu卸载显卡驱动](https://blog.csdn.net/weixin_43387480/article/details/131947256)
[^4]: CSDN，@道阻且长行则将至！，[Ubuntu18-22.04安装和干净卸载nvidia显卡驱动——超详细、最简单](https://blog.csdn.net/Perfect886/article/details/119109380)