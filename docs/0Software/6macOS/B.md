---
title: 📪 黑苹果安装记录
date: 2021-06-29
comments: true
---

 ## 前言

黑苹果安装简单，难在驱动。在装了很多次后发现，一个好的安装包可以为装驱动省去很多麻烦。

目前个人感觉`macOS Catalina`系统安装最好用的安装包是：`黑果小兵 macOS Catalina 10.15.4(19E2269) Installer for Clover 5116 and WEPE.dmg`，其他的安装包，即便也是来自黑果小兵网站，还是不如这个安装包好用。

至于`macOS Bigsur`系统，装过两次，安装成功后没及时记录，忘了用的哪个安装包。

下面是遇到的一些主机的黑苹果安装、驱动记录。

## 壹丨联想Y50-70

基本配置：

|   型号   |                      联想 Y50-70AM-IFI                      |
| :------: | :---------------------------------------------------------: |
|  处理器  |        Intel Core i5-4200H(2.8GHz/L3 3M) Haswell架构        |
|   内存   | 4GB DDR3L 1600MHz（自行安装一条三星DDR3L 1600MHz扩容至8GB） |
|   硬盘   |         1TB HDD（自行更换三星860 EVO 500G固态硬盘）         |
|   显卡   |   NVIDIA GeForce GTX 860M+Intel HD 4600（BIOS中屏蔽独显）   |
|   USB    |                      1xUSB2.0+2xUSB3.0                      |
| 其他接口 |                   HDMI接口、3.5mm耳机...                    |

### 1.准备工作

BIOS设置：

```yaml
UEFI boot: enabled
secure boot: disabled
```

镜像：[黑果小兵](https://blog.daliansky.net)

系统安装流程不再赘述，按照指示安装即可。

### 2.安装驱动

第一步，安装 Xcode

```bash
xcode-select --install
```

第二步，克隆 git 仓库

```bash
mkdir ~/Projects
```

```bash
cd ~/Projects
```

```bash
git clone https://github.com/RehabMan/Lenovo-Y50-DSDT-Patch y50.git
```

第三步，安装驱动

```bash
cd ~/Projects/y50.git
```

```bash
./download.sh
```

```bash
./install_downloads.sh
```

第四步，编译

```bash
cd ~/Projects/y50.git
```

```bash
make
```

```bash
make install
```

第五步，修复休眠

```bash
sudo pmset -a hibernatemode 0
```

```bash
sudo rm /var/vm/sleepimage
```

```bash
sudo mkdir /var/vm/sleepimage
```

第六步，移动到 EFI 分区

```bash
cd ~/Projects/y50.git
```

```bash
./mount_efi.sh
```

```bash
cd ~/Projects/y50.git
```

```bash
cp config.plist /Volumes/EFI/EFI/Clover/config.plist
```

## 贰丨Samsung 270E5K

一款2015年左右上市的三星笔记本，使用5代i5，独显是NVIDIA GeForce 920M，据说920是开普勒架构，愚以为开普勒架构的N卡都可以免驱，安装macOS 10.13.6及以前的版本，不断地装机、爬贴，发现WebDriver并不能驱动。

后来查到，920M是GK208核心，没办法驱动的。（另外，macOS 10.13是真的老了，有效的资料太少）

## 叁丨Intel 8500+华硕xx主板（台式机）

主板只有VGA，在硬件底层就已经被macOS砍掉了。虽然据说是主板上的DP口改出来的VGA，但最终没能驱动成功

## 肆丨Intel 9700+华硕Prime B365M-K（台式机，主板只有DVI和VGA）

### 1.显卡驱动：

**尝试一**，安装完成后，核显没驱动，DVI正常输出，仿冒`IDIntelGFX`设置为`3E9B8086`、`ig-platform-id`设置`3E9B0007`后，开机黑屏。（核心显卡正常驱动后DVI/HDMI没有输出）

**尝试二**，注入不同显卡id，没用；修改机型为`Macmini 8.1`，没用；FB打缓冲帧补丁，没用。。。。

**尝试三**，在网上找了一段plist设置代码，真神奇，竟然可以了！（当传家宝保存下来）

### 2.定制USB：

参考：[黑苹果Catalina 15.x USB定制（Asrock Z370）](https://blog.csdn.net/LeoForBest/article/details/103247824)

### 3.声卡驱动：

查了声卡型号，ALC巴拉巴拉，网络上搜到的注入ID，好多好多，真的是改个数重启一下，重启了十来回，声卡注入`11`成功驱动。

### 4.其他问题：

1. DVI转HDMI后屏幕发紫（RGB色彩空间问题）

   ***解决方法***：强制RGB，注入EDID

2. 无法开启HiDPI，设置1080p，字体模糊；设置高分辨率，不能全屏；HiDPI只能开启960x540。

   ***解决方法***：换个显示器后效果变好了（同样1920*1080的屏幕，玄学）

## 伍丨Lenovo ThinkPad Centre M8600t 6700+H110（品牌台式机）

6700核显免驱！！修修补补定制USB、声卡驱动就可近乎完美，教程不再赘述。

## 参考

> [1] CSDN，@LeoForBest，[黑苹果Catalina 15.x USB定制（Asrock Z370）](https://blog.csdn.net/LeoForBest/article/details/103247824)
>
> [2] tonymacx86.com，@RehabMan，[[Guide] Lenovo Y50 (UHD or 1080p) using Clover UEFI ](https://www.tonymacx86.com/threads/guide-lenovo-y50-uhd-or-1080p-using-clover-uefi.261723/)
>
> [3] [黑果小兵](https://blog.daliansky.net/)

