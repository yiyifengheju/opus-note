---
title: git-cliff
date: 2024-08-13
comments: true
---

Git-cliff 是一个高度可定制的 Changelog 生成器，它遵循 Conventional Commits 规范[1](https://poe.com/chat/35fhk0utp9utk8nyacu#user-content-fn-1)，它可以从 Git 历史记录中生成 Changelog 文件，并使用正则表达式驱动的自定义解析器。Changelog 模板可以通过配置文件进行定制，以匹配所需的格式。

Git-cliff 的主要特点包括：

- **高度可定制性：** Git-cliff 使用正则表达式驱动的自定义解析器，可以轻松地定制 Changelog 的格式[2](https://poe.com/chat/35fhk0utp9utk8nyacu#user-content-fn-2)。
- **遵循 Conventional Commits 规范：** Git-cliff 可以为遵循 Conventional Commits 规范的任何 Git 仓库生成 Changelog 文件。
- **易于集成：** Git-cliff 可以轻松地集成到 Rust、Python 和 Node.js 项目中，作为命令行工具使用，也可以作为 Rust 项目的库使用。

## 壹丨安装

以Python环境为例：

=== "Rye"
    
    ``` bash
    # 全局安装
    rye install git-cliff
    rye sync
    
    # 当前环境安装
    rye add git-cliff
    rye sync
    ```

=== "pip"
    
    ``` bash
    pip install git-cliff
    ```

## 贰丨简单使用

项目目录下运行：

```bash
git-cliff
```

将自动生成`CHANGELOG.md`文件

## 参考

## Footnotes

1. GitHub，@orhun，[git-cliff](https://github.com/orhun/git-cliff) [↩](https://poe.com/chat/35fhk0utp9utk8nyacu#user-content-fnref-1)
2. [git-cliff.org](https://git-cliff.org/) [↩](https://poe.com/chat/35fhk0utp9utk8nyacu#user-content-fnref-2)