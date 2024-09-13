---
title: 🦚 Cloudflare配置
comments: true
---

[Cloudflare](https://www.cloudflare.com)提供CDN、优化工具、安全、分析以及应用等服务，可以使用其提供的免费加速服务和网站保护服务。

## 壹丨Cloudflare配置DNS解析

与各种云服务域名解析功能类似，在Cloudflare中可以设置`使用Cloudflare代理流量`或`仅限DNS解析`

> 记录类型介绍：
>
> * CNAME记录：别名记录，将域名解析到另外一个域名；
> * A记录：指定主机名（或域名）对应的IP地址，即当访问此域名的时候，直接指向IP地址的主机；
> * TXT记录：为某个主机名或域名设置说明，可以用来验证对域名的管理权；
> * MX记录：邮件交换记录，一般用于将某个域名的电子邮件指向对应邮件服务器。

## 贰丨启用Cloudflare Pages

__（2022.3更新：已经弃用Cloudflare Pages服务，改用vercel）__

[Cloudflare Pages](https://pages.cloudflare.com)为前端开发人员提供协作和部署服务，支持Hugo、JekyII、React、Vue、Gatsby等框架。

以Hexo博客部署为例，流程如下：

第一步，项目创建：Cloudflare Pages中，创建项目——登录Github——选择对应的git仓库

第二步，构建与部署：

1. 构建参数设置为空

> 在Hexo创建博客时：
>
> `hexo g`命令，将`~/hexo-site/source/`文件夹下`.md`、`.html`、`.js`等文件渲染并放入`~/hexo-site/public/`文件夹下
>
> `hexo deploy`命令，将`~/hexo-site/public/`文件夹下的内容推到git仓库（静态网页的全部内容就在这里）

2. 构建配置：

> * 框架预设：None
> * 构建命令：空
> * 构建输出目录：空
> * 根目录（高级）：空

配置完后将自动部署

第三步，自定义域名：

1. 项目——自定义域——设置自定义域；

2. Cloudflare中：DNS——添加记录——设置CNAME记录。

第四步，开启HTTPS。使用Cloudflare代理可以直接开启强制HTTPS，在Cloudflare Pages中是默认配置的。

## 参考

> [1] 知乎，@江湖人士，[cloudflare使用入门教程，国外最好免费CDN](https://zhuanlan.zhihu.com/p/82909515)
>
> [2] 知乎，@随风，[Hexo博客提交百度收录SEO](https://zhuanlan.zhihu.com/p/128033054)