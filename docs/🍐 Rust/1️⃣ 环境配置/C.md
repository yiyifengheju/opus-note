---
title: Rust相关概念
date: 2024.07.01
---

### 1. 工具链

Rust 的工具链包括 `stable`（稳定版）、`beta`（测试版）和 `nightly`（开发版），以及特定平台的工具链（如 `x86_64-pc-windows-gnu`）

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

### 2. 组件

组件是工具链的一部分，例如 `rust-src`（Rust 源码）、`rust-analysis`（分析工具）等

### 3. 目标三元组

用于指定交叉编译的目标平台，例如 `x86_64-unknown-linux-gnu` 表示 Linux 平台



