---
title: 😎 MkDocs配置
date: 2023-02-04
comments: true
---

### 1.启用主题&添加YAML支持：

```yaml ./mkdocs.yml
# yaml-language-server: $schema=https://squidfunk.github.io/mkdocs-material/schema.json

theme:
  name: material
```

### 2.个人配置

约定以下界面部分名称：

![navigation-tabs](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/navigation-tabs.webp)

全部配置如下（建议看一遍官网的配置教程）：

```yaml
# yaml-language-server: $schema=https://squidfunk.github.io/mkdocs-material/schema.json

site_name: 一一风和橘's笔记
theme:
  icon:
    repo: fontawesome/brands/git-alt

  # 主题名称
  name: material
  # 扩展材料
  custom_dir: overrides
  # logo
  logo: assets/logo.svg
  # 首页
  #  homepage: mastermao.cn
  # 网站图标
  favicon: assets/favicon.svg
  # 不使用google fonts
  font: false
  # 设置页面语言
  language: zh
  features:
    # ==================页面设置==================
    # 即时加载
    - navigation.instant
    # 锚点跟踪
    - navigation.tracking
    # 锚点跟踪滚动（文章TOC添加到侧边栏）
    #- toc.integrate
    # 返回顶部
    - navigation.top
    # 添加章节索引
    # nav:
    #  - Section:
    #    - section/McDocs.md
    #    - Page 1: section/page-1.md
    #    ...
    #    - Page n: section/page-n.md
    - navigation.indexes
    # ==================导航栏设置==================
    # 导航栏选项卡
    - navigation.tabs
    # 导航栏始终可见
    #- navigation.tabs.sticky
    # ==================侧边栏设置==================
    # 展示方式（多级标题or折叠）
    - navigation.sections
    # 侧边栏不折叠
    #- navigation.expand
    # ==================标头设置==================
    # 搜索突出显示
    - search.highlight
    # 标头自动隐藏
    - header.autohide
    # 公告栏关闭按钮
    - announce.dismiss
    # ==================页脚设置==================
    # 上一页下一页
    #- navigation.footer
    # ==================代码复制==================
    - content.code.copy

  palette:
    # ==================亮色模式==================
    - media: "(prefers-color-scheme: light)"
      # 亮/暗
      scheme: default
      # 主题色
      primary: orange
      # 高亮色
      accent: indigo
      # 切换按钮
      toggle:
        icon: material/brightness-7
        name: 夜间模式
    # ==================暗色模式==================
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: teal
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: 日间模式

# 自定义CSS
extra_css:
  - stylesheets/extra.css

# 自定义js
extra_javascript:
  - javascripts/extra.js
  - javascripts/mathjax.js
  - https://polyfill.io/v3/polyfill.min.js?features=es6
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js

markdown_extensions:

  # Python Markdown
  - abbr
  - admonition
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - toc:
      permalink: true

  # Python Markdown Extensions
  - pymdownx.arithmatex:
      generic: true
  - pymdownx.betterem:
      smart_enable: all
  - pymdownx.caret
  - pymdownx.details
  - pymdownx.emoji:
      emoji_index: !!python/name:materialx.emoji.twemoji
      emoji_generator: !!python/name:materialx.emoji.to_svg
      options:
        custom_icons:
          - overrides/.icons
  - pymdownx.highlight:
      linenums: true
      linenums_style: pymdownx-inline
  - pymdownx.inlinehilite
  - pymdownx.keys
  - pymdownx.mark
  - pymdownx.smartsymbols
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.tilde
  - pymdownx.snippets:
      auto_append:
        - lib/abbreviations.md

# 插件
plugins:
  # 搜索
  - search:
      separator: '[\s\-,:!=\[\]()"/]+|(?!\b)(?=[A-Z][a-z])|\.(?!\d)|&[lg]t;'
  - glightbox

extra:
  # 页脚社交连接
  social:
    - icon: fontawesome/brands/git
      link: https://gitee.com/mastermao
    - icon: fontawesome/brands/500px
      link: https://500px.com.cn/MonsterMao
    - icon: fontawesome/solid/envelope
      link: mailto:wego_mao@hotmail.com
    - icon: fontawesome/brands/weixin
      link: assets/logo.svg

copyright: Copyright &copy; 2023 - 2023 一一风和橘

repo_url: https://github.com/squidfunk/mkdocs-material
repo_name: squidfunk/mkdocs-material

```

