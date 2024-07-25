---
title: F 常用NPM工具
comments: true
---

### 1. CSSO

CSSO（CSS Optimizer）是一种用于优化CSS（层叠样式表）代码的工具。它可以通过删除不必要的空格、压缩代码、合并选择器等方式来减小CSS文件的大小，提高网页加载速度，并减少网络传输的数据量。

Terminal运行[^1]：

```bash
sudo npm install -g csso-cli
```

### 2. Sass/SCSS

SCSS是一种CSS预处理器，扩展了CSS的功能，包括变量、嵌套规则、混合、继承等，简化了样式表的编写过程。

Terminal运行[^2]：

```bash
sudo npm install -g sass
```

### 3. Less

Less是一种CSS预处理器，增加了变量、嵌套规则、混合等功能，提供更灵活、可维护的样式表编写方式。

Terminal运行：

```bash
npm install --global less
```

### 4. UglifyJS

UglifyJS是一个JavaScript代码压缩工具，能够减小文件大小、提高加载速度，同时保持代码的功能和逻辑不变。

Terminal运行[^3]：

```bash
sudo npm install --g uglify-js
```


[^1]: PyCharm文档，[Minifying CSS](https://www.jetbrains.com/help/pycharm/compressing-css.html#css_before_you_start)
[^2]: PyCharm文档，[Sass, SCSS, and Less](https://www.jetbrains.com/help/pycharm/transpiling-sass-less-and-scss-to-css.html)
[^3]: PyCharm文档，[Minifying JavaScript](https://www.jetbrains.com/help/pycharm/minifying-javascript.html)
