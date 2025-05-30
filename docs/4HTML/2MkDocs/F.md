---
title: 😎 mkdocstrings-python经验总结
date: 2024-09-24
comments: true
---

`mkdocstrings[python]` 用于自动化Python项目的文档生成。它与 MkDocs 配合使用，可以从源代码中提取文档字符串，并将它们转换为易于阅读的格式，从而为项目创建文档。

## 壹丨安装及配置

__1. 安装方法__

```bash
rye add mkdocstrings[python]
```

__2. 配置__

```
```



## 贰丨经验总结

1. 直接定位到函数

```markdown
# Fetch202LongTimeBP

::: PyPulse.DataSets.Fetch202LongTime
```
2. 不要在main中引入本包，否则会引发循环引用错误
3. 文档中直接定位到函数就不会进入脚本开头的注释



