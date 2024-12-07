---
title: 🛌 NexT主题启用PJAX
date: 2021-08-31
comments: true
---



<!--more-->

## 壹丨什么是 PJAX？

PJAX，即 PushState + Ajax，封装成一个 jQuery 扩展以方便使用。PJAX 主要用来解决 HTML 页面局部刷新 url 不更新和不支持后退和前进的问题，提升用户体验。

通俗来讲：

没有 PJAX 时：点击页面上的按钮，网页将清除当前显示页，载入指向页的全部内容，加之网络延迟等原因，会出现短暂的整幅网页为空白页。

开启 PJAX 时：点击页面上的按钮，指向页和当前页相同的元素，如导航栏、音乐播放器等不需要重新加载，而不同的局部页面内容将刷新并加载。




## 贰丨NexT主题使用 PJAX

Hexo 的 NexT 主题已经集成 PJAX：

修改`~/hexo-site/_config.next.yml`：

```yaml
- pjax: 
+ pjax: true
```

仅仅在主题文件中启用 PJAX 局部刷新后，一些插件会失效，本博客失效的插件有：gallery视图插件`hexo-next-photos`、豆瓣电影插件`hexo-douban`、音乐插件`aplayer`、`meting`。




## 叁丨解决插件失效问题

> 原理：在添加插件的位置重新加载CSS、JS文件。

### 1. APlayer、Meting 音乐插件——切换界面音乐不停

这类可以通过修改 HTML 代码导入 CSS、JS 文件：

**【侧边栏添加全局音乐播放插件】**

第一步，修改 `~/hexo-site/_config.next.yml`  ：

```yaml
- #sidebar: source/_data/sidebar.njk
+ sidebar: source/_data/sidebar.njk
```

第二步，`~/hexo-site/source/_data/` 中，增加文件 `sidebar.njk` ，编辑如下：

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title></title> 
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/aplayer/dist/APlayer.min.css">
        <script src="https://cdn.jsdelivr.net/npm/aplayer/dist/APlayer.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/meting@2.0.1/dist/Meting.min.js"></script>
    </head>
    <body>
    	<meting-js server="netease" type="playlist" id="6922083348" autoplay="true" order="random" list-folded="true"></meting-js>    
    </body>
</html>
```



### 2. 画廊插件 `hexo-next-photos`

使用图床模式，插件将 `~/hexo-site/node_modules/hexo-next-photos/lib/figureBed.js` 生成 `photo.js` ，丢到 `~/hexo-site/public/js/` 下

插件失效解决原理：检测到 `ImageGrid` 的类，就重新加载一次CSS、JS。

修改 `~/hexo-site/themes/next/source/js/pjax.js`，添加：

```js
const pjax = new Pjax({....)}
...
//添加以下代码
var dynamicLoading = {
    css: function(path){
    	if(!path || path.length === 0){
        	throw new Error('argument "path" is required !');
    	}
    	var head = document.getElementsByTagName('head')[0];
    	var link = document.createElement('link');
    	link.href = path;
    	link.rel = 'stylesheet';
    	link.type = 'text/css';
    	head.appendChild(link);
	},
    js: function(path){
        if(!path || path.length === 0){
            throw new Error('argument "path" is required !');
        }
        var head = document.getElementsByTagName('head')[0];
        var script = document.createElement('script');
        script.src = path;
        script.type = 'text/javascript';
        head.appendChild(script);
    }
}
```

然后再添加：

```js
document.addEventListener('pjax:success', () => {
...
NexT.utils.updateSidebarPosition();

// 添加以下代码
if(document.getElementsByTagName("ImageGrid")){
	//动态加载 CSS 文件
	dynamicLoading.css("/css/gallery.css");
	//动态加载 JS 文件
	dynamicLoading.js("/js/photo.js");
}
```

### 3. 豆瓣电影插件 `hexo-douban`

根据以上思路，只要在 `pjax.js` 中添加进要加载的 CSS、JS 即可，当然最重要的是找到要追踪的类名。

**第一步**，定位插件显示位置，位于 `<div class="post-body animated fadeInDown">` 下：

**第二步**，逐行分析：

```html
<blockquote> ... </blockquote> <!--这是一开始的那个quote块-->
<style> ... </style> <!--这是样式（CSS）文件>
<div class="hexo-douban-tabs"> ... </div> <!--这是显示豆瓣电影 在看/想看/已看 的div标签-->
<div> ... </div> <!--这里放的是 首页/上一页/页码/下一页/尾页 的标签-->
<script> ... </script> <!--这里是JS文件-->
```

所以，把 `<style> ... </style>` 内容保存为 `douban.styl` ，放在 `~/hexo-site/themes/next/source/css/` 下；把 `<script> ... </script>` 保存为 `douban.js` ，放在 `~/hexo-site/themes/next/source/js/` 下；

因为，在执行 `hexo g` 的时候，`~/hexo-site/themes/next/source/css/` 和 `~/hexo-site/themes/next/source/js/` 两个文件夹中的文件会拷贝到 `~/hexo-site/public/css` 和 `~/hexo-site/public/js` 文件夹下。

**第三步**，继续分析：

包含 `envent` 的 `<a> </a>` 标签在分别存放在两个类下：

```html
<div class="hexo-douban-tabs"> ... </div>
<div class="hexo-douban-pagination"> ... </div>
```

所以，在 `~/hexo-site/themes/next/source/js/pjax.js` 中添加：

```js
if(document.getElementsByTagName("hexo-douban-tabs")){
    //动态加载 CSS 文件
    dynamicLoading.css("/css/douban.css");
    dynamicLoading.js("/js/douban.js");
}
if(document.getElementsByTagName("hexo-douban-pagination")){
    //动态加载 CSS 文件
    dynamicLoading.css("/css/douban.css");
    dynamicLoading.js("/js/douban.js");
}
```

> __因为没学过前端的 HTML、JS、CSS 这些，如有错误，希望不吝赐教__


## 参考

> [1] FHB科学院，樊浩柏，[PJAX原理和使用](https://www.fanhaobai.com/2017/07/pjax.html)
>
> [2] 米米的博客，张书樵，[NexT 适配 PJAX 的方案](https://zhangshuqiao.org/2020-06/NexT适配PJAX的方案/)
>
> [3] 程序员甜品店，Jefsky，[解决pjax加载页面导致js插件失效](https://www.jefsky.com/archives/234.html)
>
> [4] 木皆之森，Raoby，[pjax无刷新加载后百度统计失效解决方案](https://www.raobee.com/archives/254/)
>
> [5] 小乐的博客，XiaoLe，[解决next主题开启pjax时使用hexo-blog-encrypt无效](https://www.xiaole88.com/post/55609.html)

