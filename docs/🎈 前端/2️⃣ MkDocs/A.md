---
title: 😀 Mkdocs新建环境
comments: true
---

[MkDocs](https://www.mkdocs.org/)是一个快速、简单、华丽的静态站点生成器，适用于构建项目文档。文档源码使用Markdown来撰写，用一个YAML文件作为配置文件。它可以构建静态HTML站点并托管到GitHub Pages等地方。主题可以在[这里](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes)找到。

[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)是一个MkDocs的主题（每月下载量最多），Material for MkDocs特点包括开源、内置搜索、代码注释、社交卡与emoji支持

## 壹丨新建环境

```bash
rye add mkdocs-material mkdocs-glightbox neoteroi-mkdocs fonttools mkdocs-jupyter mkdocstrings-python
```

安装MkDocs

```bash
rye add mkdocs-material
```

安装`glightbox`

```bash
rye add mkdocs-glightbox
```

安装扩展插件

!!! note "[Roberto Prevato编写的几个MkDocs插件](https://www.neoteroi.dev/mkdocs-plugins/)"

```bash
rye add neoteroi-mkdocs
```

!!! note "MkDocs-Jupyter"

    [MkDocs-Jupyter](https://github.com/danielfrg/mkdocs-jupyter#readme)：在MkDocs中使用Jupyter Notebook
    
    ```bash
    rye add mkdocs-jupyter
    ```
    
    当报错`ImportError: cannot import name 'AstRenderer' from 'mistune.renderers' (/home/MasterMao/anaconda3/envs/MasterMaoPy311/lib/python3.11/site-packages/mistune/renderers/__init__.py)`时，需要更新下`mistune`：
    
    ```python
    rye add mistune==3.0.1
    ```

!!! note "字体工具"
	
    ```bash
    rye add fonttools
    ```

!!! note "mkdocstrings-python"
    
    ```
    rye add mkdocstrings-python
    ```

!!! note "管理页面顺序"
    
    ```bash
    rye add mkdocs-awesome-pages-plugin
    ```
    
    ```yaml
    plugins:
      - awesome-pages
    ```


## 贰丨常用命令

创建工程
```bash
mkdocs new [dir-name]
```
实时预览
```bash
mkdocs serve
```
构建站点
```bash
mkdocs build
```
打印帮助信息
```bash
mkdocs -h
```