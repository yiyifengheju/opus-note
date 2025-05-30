---
title: 📪 黑苹果安装问题总结
date: 2021-06-29
comments: true
---


## 壹丨安装问题

### 1.安装过程卡加号

__原因__：drivers64UEFI 里的一个efi文件有问题

第一步，`/EFI/CLOVER/drivers64UEFI/`下删除：

```bash
OsxAptioFix2Drv-64.efi
OsxLowMemFixDrv-64.efi
```

第二步，`config.plist`中删掉`slide=XXX`

第三步，如果仍旧无法启动, 表明内核请求分配的空间仍旧太大。将`CsrActiveConfig`设置成`0x67`

### 2.正常安装完成后开机出现死循环，报错：AMFI:Denying core dump for pid *** too many corpses being created

第一步，第一次重启安装后，一直进入`preboot`来安装，会重启几次，安装完成后可以进入系统，但只能从`preboot`进入

第二步，在`config.plist`中把以下这段删除（不隐藏`preboot`）

```xml
<key>
	Hide
</key>
<array>
	<string>
		Preboot
	</string>
</array>
```

### 3.“xxx安装副本损坏”

终端修改date。实践发现，每次使用不同安装包修改的 date 是不同的，规律是修改到一年前的此时此刻。

### 4.睡眠睡死、取消睡眠后自动重启

定制USB。参考：[黑苹果Catalina 15.x USB定制（Asrock Z370）](https://blog.csdn.net/LeoForBest/article/details/103247824)

### 5.八苹果花屏

BIOS里设置：

```yaml
Legacy Boot (but UEFI first): enabled
```

### 6.无法直接开机，需要进一次Windows系统重启才能进入黑苹果/启动系统没有声音

启动参数加入`slide=0`

## 贰丨使用问题

### 1. xxx is not in the sudoers file. This incident will be reported.

Linux或Mac中，使用sudo命令，提示“xxx is not in the sudoers file. This incident will be reported.”，需要修改/etc/sudoers文件

__第一步__，添加文件写权限

```bash
sudo chmod u+w /etc/sudoers
```

__第二步__，编辑/etc/sudoers文件

```bash
nano /etc/sudoers
```

__第三步__，修改如下内容：

```bash
root ALL=(ALL) ALL
xxx ALL=(ALL) ALL # xxx是用户名
```

__第四步__，撤销文件写权限

```bash
sudo chmod u-w /etc/sudoers
```

