---
title: E Ubuntu使用
comments: true
---

## 1. 关闭Python进程

第一步，打开终端

第二步，查看正在运行的Python进程

```bash
ps -aux | grep python
```

第三步，找到想要关闭的Python进程PID，在输出的第二列

第四步，关闭Python进程

```bash
kill <PID>
```

## 2. 删除本文件夹下所有文件

第一步，进入目标文件夹

```bash
cd /path/to/folder
```

第二步，删除目标文件夹下所有文件

```bash
rm *
```

!!! note "删除文件夹本身"

	```bash
	rm -r /path/to/folder
	```