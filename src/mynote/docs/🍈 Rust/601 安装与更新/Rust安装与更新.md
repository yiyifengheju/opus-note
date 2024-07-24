---
title: Rust安装与更新
date: 2024.02.15
---

## 壹丨安装更新常用命令

更新Rust：

```bash
rustup update
```

卸载：

```bash
rustup self uninstall
```

添加组件：

```bash
rustup component add rustfmt
```

查看版本：

```bash
rustup --version
```

??? note "Rust两种版本：Stable和Nightly"

	Stable：稳定可靠版本，适用于大多数生产环境
	
	Nightly：每日构建的最新版本，包含实验性特性，不适用于生产环境
	
	安装：
	
	```bash
	rustup install stable/nightly
	```
	
	切换：
	
	```bash
	rustup default stable/nightly
	```









