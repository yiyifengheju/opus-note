---
title: A Mkdocs新建环境
comments: true
---

## 壹丨新建环境

安装MkDocs

```bash
pip install mkdocs-material
```

安装glightbox

```bash
pip install mkdocs-glightbox
```

安装扩展插件

!!! note "[Roberto Prevato编写的几个MkDocs插件](https://www.neoteroi.dev/mkdocs-plugins/)"

```bash
pip install neoteroi-mkdocs
```

!!! note "MkDocs-Jupyter"

    [MkDocs-Jupyter](https://github.com/danielfrg/mkdocs-jupyter#readme)：在MkDocs中使用Jupyter Notebook
    
    ```bash
    pip install mkdocs-jupyter
    ```
    
    当报错`ImportError: cannot import name 'AstRenderer' from 'mistune.renderers' (/home/MasterMao/anaconda3/envs/MasterMaoPy311/lib/python3.11/site-packages/mistune/renderers/__init__.py)`时，需要更新下`mistune`：
    
    ```python
    pip install mistune==3.0.1
    ```

!!! note "字体工具"
	
    ```bash
    pip install fonttools
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