---
title: 📪 联想Y50更换BCM94352z无线网卡
date: 2021-06-29
comments: true
---

第一步，下单

第二步，拆机安装

第三步，出现错误 unauthorized wireless network card is plugged in

**解决方法：去除BIOS无线网卡白名单限制**

## 壹丨准备工作

### 1.工具

修改BIOS的软件、BIOS文件等https://cloud.189.cn/t/36zauuvAnYZj（访问码：il7a）

### 2.升级BIOS（可跳过）

找到合适版本的BIOS点击安装（推荐1.14版本以下的BIOS）

### 3.备份BIOS

升级后重启，在BIOS中升级，再进行备份

开机，管理员权限执行`fptw64/`中的`backup.exe`，生成`bios_bak.bin`

## 贰丨删除白名单

第一步，EzH2O载入BIOS备份（bios_bak.bin）

第二步，选择：组件——模块——删除现有的模块

第三步，选择：GUID-“11D378C2-B472-412F-AD87-1BE4CD8B33A6”——修补

第四步，选择：文件——保存

## 叁丨刷入

第一步，插入U盘，管理员权限运行`rufus`，点击运行，制作U盘启动盘

第二步，将`fpt/`文件夹复制到U盘根目录

第三步，将修改后的BIOS文件复制到U盘根目录，改名为`1.bin`

第四步，重启进入BIOS，设置Legacy Support，保存退出

第五步，重启F12选择DOS系统，显示`C:>`

第六步，输入`cd fpd`，回车

第七步，输入`prr`，回车

第八步，输入`fpt -f 1.bin -bios`，回车

第九步，重启

