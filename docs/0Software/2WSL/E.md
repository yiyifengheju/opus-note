---
title: ☃️ 调用WSL命令
comments: true
---

## 壹丨调用WSL-git

> 众所周知，Windows使用git需要安装相关软件，这里我们可以调用Linux自带的git功能

**第一步**，创建git.cmd脚本

新建文件：`C:\Users\MasterMao\git\git.cmd`

```bash
@echo off
bash -c "/usr/bin/git %*"
```

**第二步**，添加环境变量

此电脑——属性——高级系统设置——高级-环境变量——Path——编辑——新建，将`git.cmd`文件路径`C:\Users\MasterMao\git`写入。

**第三步**，验证

在Windows Terminal或Pycharm Terminal中查询git版本：

```bash
git --version
# 调用成功：
# git version 2.25.1
```

**最后**，Pycharm使用WSL-git：

1. 可以在终端中直接使用git命令
2. 设置——版本控制——Git中，设置Git可执行文件路径为`C:\Users\MasterMao\git\git.cmd`，点击测试即可看到git版本

<img src="https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/Snipaste_2023-01-05_22-44-57.webp" />

> 但我使用2的时候在右下角总会出现烦人的扫描进度条，不推荐。

## 贰丨调用sass功能

> sass用于前端中将`.SCSS`、`.SASS`文件编译成`.CSS`文件

**第一步**，WSL中安装sass[^1]

```bash
sudo npm install -g sass
```

**第二步**，创建sass.bat脚本

新建文件：`C:\Users\MasterMao\sass\sass.cmd`

```bash
@echo off
bash -c "/usr/bin/sass %*"
```

**第三步**，添加环境变量

此电脑——属性——高级系统设置——高级-环境变量——Path——编辑——新建，将`sass.cmd`文件路径`C:\Users\MasterMao\sass`写入。

**第四步**，验证

在Windows Terminal或Pycharm Terminal中查询sass版本：

```bash
sass --version

# 调用成功
# 1.57.1 compiled with dart2js 2.18.6
```

**最后**，WebStorm调用WSL-sass

设置——工具——File Watcher中，新建File Watcher，此时程序应该默认找到了sass工具，确定即可

<img src="https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/Snipaste_2023-01-05_22-51-19.webp" />

!!! note "其他功能"

	其他功能包括CSSO、SCSS/Sass、Less、UglifyJS等，方法大致相同。附安装命令：
	```
	# CSSO
	sudo npm install -g csso-cli
	# SCSS/Sass
	sudo npm install -g sass
	# Less
	sudo npm install --global less
	# UglifyJS
	sudo npm install --g uglify-js
	```

[^1]: RUNOOB.COM，[Sass安装](https://www.runoob.com/sass/sass-install.html)