---
title: 🛌 Hexo公式渲染
date: 2022-05-30
comments: true
---

## 壹丨MathJAX 插件

此前的公式渲染直接使用的是NexT主题自带的MathJAX插件，`_config.next.yml`设置如下：

```yaml
math:
  every_page: true

  mathjax:
    enable: true
    tags: none

  katex:
    enable: true
    copy_tex: true
```

但是存在两个问题：

1. 公式渲染速度慢，打开文章需要等几秒公式才能渲染完成
2. 渲染格式错误、字体诡异

网络搜索后发现很多解决方案，如参考[^1][^2][^3][^4][^5]，由于步骤过于繁琐，没敢尝试。

## 贰丨Hexo Filter MathJax 插件

参考[^6]给出了一种解决方案，可以在Hexo生成过程中将公式渲染为SVG图片，提高渲染速度，测试发现公式格式、字体等问题也完美解决。

插件地址：[Hexo Filter MathJax](https://github.com/next-theme/hexo-filter-mathjax)

### 第一步，准备工作

1. 删除其他与公式渲染相关的插件
2. 禁用NexT主题的公式渲染器

```yaml
math:
  mathjax:
    enable: false
  katex:
    enable: false
```

### 第二步，安装插件

```bash
npm install hexo-filter-mathjax
```

在博客配置文件`_config.yml` 中，添加：

```yaml
mathjax:
  tags: none # or 'ams' or 'all'
  single_dollars: true # enable single dollar signs as in-line math delimiters
  cjk_width: 0.9 # relative CJK char width
  normal_width: 0.6 # relative normal (monospace) width
  append_css: true # add CSS to pages rendered by MathJax
  every_page: false # if true, every page will be rendered by MathJax regardless the `mathjax` setting in Front-matter
  extension_options: {}
    # you can put your extension options here
    # see http://docs.mathjax.org/en/latest/options/input/tex.html#tex-extension-options for more detail
```

### 第三步，使用

`.md`文章头部添加：

```yaml
---
title: xxx
categories: xxx
date: xxx
mathjax: true
---
```

## 参考

[^1]: CSDN，@养猪去，[这次彻底解决在Hexo中渲染MathJax数学公式出现的问题！！！](https://blog.csdn.net/qq_44846324/article/details/114582328)
[^2]: CSDN，@TheBetterKong，[改进 Hexo 中 MathJax 数学公式的渲染](https://blog.csdn.net/weixin_44849403/article/details/117776916)
[^3]: CSDN，@码小余の博客，[如何在hexo中支持Mathjax](https://blog.csdn.net/Cool_breeze_/article/details/115104683)
[^4]: 博客园，@VitaHeng ，[ hexo博客MathJax公式渲染问题](https://www.cnblogs.com/Ai-heng/p/7282110.html)
[^5]: 简书，@治部少辅，[Hexo + Mathjax: 公式离线渲染](https://www.jianshu.com/p/c8964c5ffd7a)
[^6]: 米米的博客，@张书樵，[Hexo 后端 MathJax 渲染](https://zhangshuqiao.org/2020-04/Hexo%E5%90%8E%E7%AB%AFMathJax%E6%B8%B2%E6%9F%93/)
