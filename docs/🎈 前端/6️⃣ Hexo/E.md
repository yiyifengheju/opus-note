---
title: 🛌 NexT主题美化
date: 2021-08-20
comments: true
---

## 壹丨文件介绍

> 下述为目前个人对Hexo项目的理解，不一定正确

`~/source/_data/sidebar.njk`，sidebar配置文件

`~/source/_data/styles.njk`，主题的CSS文件

`~/source/_data/languages.yml`，中英文翻译文件

当修改这些时，会覆盖原有的样式

## 贰丨界面美化

### 1. 设置背景图片

将背景图片放入`~/hexo-site/themes/next/source/images/`

修改`~/hexo-site/_config.next.yml`：

```yaml
+ custom_file_path:
+   style: source/_data/styles.styl
```

新建或修改`~/hexo-site/source/_data/styles.styl`，添加：

```css
// 设置背景图片
body {
  background: url(/images/background.webp);
  background-repeat: no-repeat;
  background-attachment: fixed; //不重复
  background-size: cover; //填充
  background-position: center;
}
```

### 2. 博客文本透明化

打开`~/hexo-site/source/_data/styles.styl`，添加：

```js
// 博客内容透明化
//文章内容的透明度设置
.post-block {
  opacity: 0.85;
}

//侧边框的透明度设置
.sidebar {
  opacity: 0.85;
}

//菜单栏的透明度设置
.header-inner {
  background: rgba(255,255,255,0.85);
}

//搜索框（local-search）的透明度设置
.popup {
  opacity: 0.9;
}
```

### 3. 设置界面圆角

修改  `~/hexo-site/_config.next.yml` ：

```yaml
+ custom_file_path:
+   variable: source/_data/variables.styl
```

新建或修改 `~/hexo-site/source/_data/variables.styl`，添加：

```css
// 圆角设置
$border-radius-inner     = 10px 10px 10px 10px;
$border-radius           = 10px;
```

### 4. 全局字体加粗

```css
* {
  font-weight: 700;
}
```

### 5. 修改卡片间距

```CSS
.posts-expand .post-header {
  margin-bottom: 10px;
}

.post-button {
  margin-top: 10px;
}
```

## 贰丨音乐播放

### 1. 网易云音乐外链播放

网页版网易云音乐生成外链播放器，直接将`iframe`代码粘贴到页面

### 2. 使用`Hexo-Tag-APlayer`插件

APlayer官网：[APlayer](https://aplayer.js.org/#/)

`Hexo-Tag-APlayer`项目开源地址：[Hexo-Tag-APlayer](https://github.com/MoePlayer/hexo-tag-aplayer)

第一步，安装插件。

```bash
npm install --save hexo-tag-aplayer
```

第二步，启用 `MetingJS`。修改 `~/hexo-site/_config.yml`，添加：

```yaml
+ aplayer:
+   meting: true
```

第三步，添加音乐。在网易云音乐中找到歌曲 `id`。

以歌曲id=31192230为例，markdown文件中添加：

```html
{% meting "3986040" "netease" "song" "theme:#555" "mutex:true" "listmaxheight:340px" "preload:auto" %}
```

以歌单id=6922083348为例，添加：

```html
{% meting "6922083348" "netease" "playlist" "theme:#555" "mutex:true" "listmaxheight:340px" "preload:auto" %}
```

## 参考

> [1] CSDN，@hushhw，[Hexo 主题插入音乐之 aplayer 音乐播放器](https://blog.csdn.net/hushhw/article/details/88092728)
> [2] Github，[hexo-tag-aplayer 中文文档](https://github.com/MoePlayer/hexo-tag-aplayer/blob/master/docs/README-zh_cn.md)