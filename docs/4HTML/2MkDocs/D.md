---
title: 😎 MkDocs插件
comments: true
---

### 1. Jupyter插件

插件地址：https://github.com/danielfrg/mkdocs-jupyter

安装：

```bash
pip install mkdocs-jupyter
```

配置：

```yaml title='mkdocs.yml'
plugins:
  - mkdocs-jupyter:
      ignore: [ ".ipynb_checkpoints/*.ipynb" ]
```

### 2. 文档加密

插件地址：https://unverbuggt.github.io/mkdocs-encryptcontent-plugin/

```yaml
- encryptcontent:
    title_prefix: '[LOCK]'
    summary: '本文档为加密内容'
    placeholder: '输入密码，按CTRL+ENTER解锁'
    decryption_failure_message: '密码错误！！'
    encryption_info_message: ''
    input_class: 'md-search__form md-search__input'
    button_class: 'md-search__icon'
```

### 3. 页脚信息

插件地址：https://github.com/sondregronas/mkdocs-footermatter

> 需要将`.css`、`.html`等文件复制到MkDocs的对应文件夹下

### 4. 一个新的主题



### 5. 导出PDF

插件地址：https://pypi.org/project/mkdocs-exporter/

> 还没试过

### 6. 插入PDF

插件地址：https://pypi.org/project/mkdocs-pdf/

或者使用`embed`语法

```html
<embed src="path/to/pdf" width="100%" height="900">
```

### 7. 卡片、时间轴

插件地址：https://www.neoteroi.dev/mkdocs-plugins/

> 强烈推荐

### 8. 拼写检查

插件地址：https://pypi.org/project/mkdocs-spellcheck/

### 9. 视频插件

插件地址：https://pypi.org/project/mkdocs-video/