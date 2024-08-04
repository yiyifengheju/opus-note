---
title: 🍃 MinIO搭建本地图床
comments: true
---

## 壹丨为什么要搭建本地图床？

由于公司保密要求高，网盘、云笔记类软件一概不得使用，多番尝试过后，决定使用搭建一套本地博客系统的方法用于归档多源数据。

然而，当我在多种博客框架间反复横跳时，发现不同主题对Markdown本地图片的管理方式不一致，有些主题只需要在配置文件中设置：

```yaml
post_asset_folder: true
```

然后将图片放入文档的同名文件夹中即可正常显示，但此方法并不通用且管理起来很不灵活。**常规的解决办法是使用图床**，如腾讯云/阿里云的对象存储、Github/Gitee的仓库……

显然，公司是绝不允许这样做的。因此，建立一套本地图床+自动上传的操作流是有必要的。

## 贰丨MinIO搭建本地图床[^1]

**下载MinIO：**

打开[官方网站](https://min.io/download#/windows)，选择`MINIO SERVER`，下载。

**启动服务：**

在`minio.exe`所在目录下，打开命令提示符，设置用户名密码：

```bash
setx MINIO_ROOT_USER admin
setx MINIO_ROOT_PASSWORD password
```

>**Tips：**如果忘记登录密码，可以尝试删除`~\Bucket\.minio.sys`文件夹，重新配置用户名密码即可。

启动服务：

```bash
.\minio.exe server E:\Bucket
```

<img src="https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/image-20221003131842618.webp" alt="" width='90%' />



**新建存储桶：**

打开http://127.0.0.1:9000

输入用户名：`mastermao`，密码`bugaosuni`（如上图`RootUser`、`RootPass`所示）

<img src="https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/image-20221003125708185.webp" alt="" width='90%' />

按照指示，点击`Create a Bucket`，输入存储桶名称并新建即可。

<img src="https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/image-20221003130035100.webp" alt="" width='90%' />

点击`Manage`，在`Access Rules`中点击`Add Access Rule`，新增一个`readwrite`规则

<img src="https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/image-20221003130224354.webp" alt="" width='90%' />

至此，存储桶新建完成。

## 叁丨PicGo连接MinIO[^2]

### 3.1 安装`picgo-plugin-minio`插件

【自动安装】

直接在PicGo插件设置中搜索并安装`minio`。但这种方式支持的文件格式仅包括`.gif`、`.jpg`、`.jpeg`、`.png`、`.bmp`、`.ico`、`.webp`。因此，推荐手动安装。

<img src="https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/image-20221003132455287.webp" alt="" width='90%' />

【手动安装】[^3][^4]

下载插件源码[picgo-plugin-minio](https://github.com/Herbertzz/picgo-plugin-minio)，手动修改文件`.\picgo-plugin-minio-master\src\helper.js`：

```js
const imageMime = {
  gif: 'image/gif',
  jpg: 'image/jpeg',
  jpeg: 'image/jpeg',
  png: 'image/png',
  bmp: 'image/bmp',
  ico: 'image/x-icon',
  webp: 'image/webp',
  // ADD
  svg: 'image/svg+xml'
}
```

> **Tips：**目前只测试过svg格式，理论上其他媒体格式同样适用：
>
> ```js
> avi: 'video/avi'
> mp3: 'audio/mp3'
> mp4: 'video/mp4'
> ```

然后，点击PicGo插件设置-导入本地插件，定位到`picgo-plugin-minio-master`文件夹安装。

<img src="https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/image-20221003135918000.webp" alt="" width='90%' />

### 3.2 图床配置

安装插件后，配置如下：

<img src="https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/Snipaste_2022-10-04_00-21-31.webp" alt="" width='90%' />

> **Tips：**endPoint，本地计算机的IP地址。
>
> 测试发现，使用`local host(127.0.0.1)`可以成功上传图片，但是在Typora中无法显示，推荐配置路由器的IP地址与MAC绑定，然后使用计算机在局域网的地址。（同理，可以使用闲置电脑在局域网内搭建图床，可自行探索）

然后点击`确定`、`设为默认图床`

最后，在PicGo-上传区测试图片上传

## 肆丨Typora图片自动上传

Typora-偏好设置-图像，配置如图所示

<img src="https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/image-20221003141240569.webp" alt="" width='90%' />



[^1]: CSDN，@旭东怪，[Windows MinIO使用教程（启动，登录，修改密码）](https://blog.csdn.net/qq_38974638/article/details/115678147)
[^2]: CSDN，@云海梦尘，[PicGo安装minio插件，Typora设置PicGo](https://blog.csdn.net/qq2523208472/article/details/121968162)
[^3]: CSDN，@plia，[minio上传svg图片后无法使用，图直接碎了](https://blog.csdn.net/ligaoming_123/article/details/126650862)
[^4]: lanol.cn，@Lan小站，[处理minio文件不能在线查看的问题 文件后缀转content_type](https://www.lanol.cn/post/599.html)
