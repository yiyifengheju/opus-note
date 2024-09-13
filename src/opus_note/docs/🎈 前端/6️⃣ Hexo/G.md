---
title: 🛌 Hexo制作个人画廊
date: 2021-07-12
comments: true
---

> 需求：在导航栏添加一个展示照片墙的“画廊”功能，要求:
>
> 1. 图片使用图床保存
> 2. 图片加载速度快
> 3. 图片体积小，非原图

> 本文使用腾讯云对象存储 COS 作为图床，使用 PicGo 软件上传，使用 Hexo 插件制作画廊，并使用 Python 脚本将原图批量压缩为 Webp 格式。

## 壹丨腾讯云 COS 图床

菜单 —— 产品 —— 存储 —— 对象存储 —— 立即使用

存储桶列表 —— 创建存储桶 —— 访问权限设置为：公有读私有写

## 贰丨使用图床

在存储桶列表 —— 选择存储桶 —— 概览中，可以看到存储桶名称和所属地域

在账户 —— 访问管理 —— 访问秘钥 —— API 秘钥管理 —— 新建秘钥，可以看到APPID、SecretId和SecretKey

### 【使用客户端】

下载客户端：https://console.cloud.tencent.com/cos5/cosbrowser

### 【PicGo】

下载客户端：https://github.com/Molunerfinn/PicGo/releases

## 叁丨Typora 图床设置

第一步，配置好 PicGo

第二步，Typora 中，文件——偏好设置——图像：

```yaml
插入图片时：上传图片
上传服务：PicGo(app)
设置 PicGo 路径
```

验证图片上传选项

## 肆丨Hexo 画廊展示

使用 Hexo 插件 `hexo-next-photos`

### 1. 安装插件

```bash
cd ~/hexo-site
```

```bash
npm install hexo-next-photos --save
```

### 2. 修改主题配置文件

第一步，将 `~/hexo-site/themes/next/_config.yml` 复制到 `~/hexo-site/`，重命名为 `_config.next.yml`

>  PS：关于这三个文件，测试发现它们的优先级：`~/hexo-site/themes/next/_config.yml` > `~/hexo-site/_config.next.yml`（用在新建导航栏调整顺序的时候）

第二步，新建文件夹 `~/hexo-site/source/_data`，新建文件 `body-end.njk`、`body-end.swig`、`styles.styl`

第三步，新建页 `hexo new page gallery`，修改 `/source/gallery/index.md`：

```html
---
title: gallery
type: photos
---
<div class="ImageGrid"></div>
```

第四步，修改 `~/hexo-site/_config.yml`，推荐使用图床模式，添加内容：

```yaml
# hexo-next-photos
hexo_next_photos:
  modes: figureBed 
  pictureUrl: 
  pictureDirPath: source/gallery/PhotoDir
```

第五步，修改 `~/hexo-site/themes/next/_config.next.yml`，如下：

```yaml
custom_file_path:
-  #bodyEnd: source/_data/body-end.swig
+  bodyEnd: source/_data/body-end.njk
-  #style: source/_data/styles.styl
+  style: source/_data/styles.styl

...

# ---------------------------------------------------------------
# Third Party Plugins & Services Settings
# See: https://theme-next.org/docs/third-party-services/
# You may need to install dependencies or set CDN URLs in `vendors`
# There are two different CDN providers by default:
#   - jsDelivr (cdn.jsdelivr.net), works everywhere even in China
#   - CDNJS (cdnjs.cloudflare.com), provided by cloudflare
# ---------------------------------------------------------------
- #fancybox: false
+ fancybox: true

...

- #lazyload: false
+ lazyload: true

...

vendors:
  # FancyBox
  # jquery: //cdn.jsdelivr.net/npm/jquery@3/dist/jquery.min.js
  # fancybox: //cdn.jsdelivr.net/gh/fancyapps/fancybox@3/dist/jquery.fancybox.min.js
  # fancybox_css: //cdn.jsdelivr.net/gh/fancyapps/fancybox@3/dist/jquery.fancybox.min.css
  jquery:
  fancybox:  # choose a faster CDN
  fancybox_css: # choose a faster CDN

  # Lazyload
  # lazyload: //cdn.jsdelivr.net/npm/lozad@1/dist/lozad.min.js
  # lazyload: //cdnjs.cloudflare.com/ajax/libs/lozad.js/1.9.0/lozad.min.js
  lazyload: # choose a faster CDN
```

增加菜单栏：

```yaml
menu:
+ gallery: /gallery/ || fa fa-camera
```

插件源程序存在错误，会导致第一张图片不显示，修改 `~/hexo-site/node_modules/hexo-next-photos/lib/figureBed.js`

```js
-  page: 1
+  page: 0
```

#### 3. 添加图片

将保存在图床的图片地址拷贝到 `source/gallery/PhotoDir/linkList.txt`，如下：

```bash
https://s1.ax1x.com/2020/05/21/YbueyT.jpg
https://s1.ax1x.com/2020/05/21/YbuZlV.jpg
https://s1.ax1x.com/2020/05/21/YbuVS0.jpg
```

## 参考

> hexo-next-photos作者博客：https://jygzyc.github.io/photos