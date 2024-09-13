---
title: 🐬 Hexo配置记录
date: 2021-06-26
comments: true
---

## 壹丨安装Hexo

第一步，安装NodeJS，参考：

<div class="grid cards" markdown>

-   :simple-nodedotjs:{ .lg .middle }  __安装NodeJS__

    ---


    [:octicons-arrow-right-24: Getting started](../1️⃣ 环境配置/B.md)

</div>

第二步，安装`Hexo`

```bash
sudo npm install -g hexo-cli
```

第三步，（可选）安装`deployer`

```bash
sudo npm install hexo-deployer-git --save
```

## 贰丨新建博客

### 第一步，博客初始化

```bash
mkdir hexo-site
```

```bash
cd hexo-site
```

```bash
hexo init
```

> __配置文件介绍__
>
> `~/hexo-site/_config.yml`，博客网站配置文件
> `~/hexo-site/themes/next/_config.yml`，主题配置文件
>
> Tips：将主题配置文件复制到博客目录下并改名为：`~/hexo-site/_config.next.yml`，这样每次升级主题时只需要覆盖主题文件夹

### 第二步，使用[NexT主题](https://theme-next.js.org)

> 官方提供了git方法和npm方法，其中，npm方法安装的主题文件位于`~/hexo-site/node_modules/next`下，本文推荐git方法。

安装主题：

```bash
cd hexo-site
```

```bash
git clone https://github.com/next-theme/hexo-theme-next themes/next
```

> __升级主题__
>
> ```bash
> cd hexo-site
> ```
>
> ```bash
> cd themes/next
> ```
>
> ```bash
> git pull origin master
> ```

### 第三步，启用NexT主题

博客配置文件`~/hexo-site/_config.yml`

```bash ~/hexo-site/_config.yml
+ theme: next
```

### 第四步，本地预览

```bash
# 清除缓存
hexo clean
# 生成静态网页
hexo g
# 本地预览
hexo s
```

打开默认端口http://localhost:4000即可本地预览

## 叁丨部署

>网页托管服务很多，如 Github Pages、Gitee Pages、Coding 持续集成、Cloudflare Pages 、Vercel等……

> Coding、Gitee 为国内服务提供商，需要实名认证，其中 Coding 和鹅云联系密切，需要 **超大量** 的认证工作，没个三五天搞不完。Cloudflare Pages、Github Pages、Vercel 为国外服务提供商，相对而言访问速度较慢。

| 服务             | 优点                                            | 缺点                                                         |
| ---------------- | ----------------------------------------------- | ------------------------------------------------------------ |
| Coding           | 速度快<br/>可被百度爬取                         | 需要认证的太多<br/>构建过程漫长<br>(部署过程繁琐，需要配置鹅云权限、各种实名认证) |
| Github Pages     | 部署简单<br/>构建速度快                         | 访问速度慢<br/>不能被百度收录                                |
| Cloudflare Pages | 部署简单<br/>部署&自定义域名一条龙<br/>速度还行 | 不能百度收录                                                 |
| Gitee Pages      | 速度快                                          | 上传后需要手动部署<br/>不能避免审查<br>__现已下线__          |
| Vercel           | 部署简单<br/>自带域名解析                       | 不能百度收录                                                 |

> Vercel部署方法最简单，这里不再赘述

!!! note "Github部署方法"

    第一步，新建仓库，命名为：
    
    ```bash
    用户名.github.io
    ```
    
    第二步，修改配置文件
    
    修改`~/hexo-site/_config.yml`：
    
    ```bash ~/hexo-site/_config.yml
    + deploy:
    +   type: git
    +   repo: git@github.com:用户名/用户名.github.io.git
    +   branch: master
    ```
    
    第三步，部署博客
    
    ```bash
    hexo deploy
    # 或
    hexo d
    ```
    
    打开Git仓库，Settings——Pages——自行配置。打开`http://用户名.github.io`即可看到博客。

## 肆丨设置个人域名

> Vercel的设置方法比较简单，不再赘述

!!! note "以阿里云为例"

    __第一步，添加解析__：阿里云控制台——域名——解析——添加A记录：
    
    ```c
    // 解析线路：默认
    // 记录类型：A
    
    // 主机记录：@
    // 记录值：下述任选一即可
    ```
    
    ***使用 [IPAddress.com](https://www.ipaddress.com/) 查找 `github.io` 的地址：***
    
    ```bash
    185.199.108.153
    185.199.109.153
    185.199.110.153
    185.199.111.153
    ```
    
    添加CNAME记录：
    
    ```C
    // 解析线路，默认
    // 记录类型，CNAME
    // 主机记录，www
    // 记录值，用户名.github.io
    ```
    
    __第二步，本地配置__
    
    ```bash
    cd ~/hexo-site/source
    touch CNAME
    nano CNAME
    # 写入域名并保存
    ```
    
    > 或者执行下一步会自动添加CNAME文件
    
    __第三步，GitHub 配置__
    
    仓库——setting——Custom domain——添加域名——填入域名


!!! note "Cloudflare实现HTTPS"

    第一步，Cloudflare注册：www.cloudflare.com；
    
    第二步，获取DNS服务器地址：Add Site——添加域名——扫描DNS记录——分配两个DNS——盛出备用；
    
    第三步，替换阿里云默认DNS服务器：阿里云——域名控制台——域名——管理——基本信息——修改DNS——添加分配的两个DNS地址——保存

## 伍丨写作软件推荐

| 软件   | 平台                                                       | 推荐度                         | 网站                           |
| ------ | ---------------------------------------------------------- | ------------------------------ | ------------------------------ |
| MWeb   | :simple-macos:                                             | :star::star::star::star:       | https://zh.mweb.im/            |
| Typora | :simple-macos: :fontawesome-brands-windows: :simple-linux: | :star::star::star::star::star: | https://typora.io/             |
| VSCode | :simple-macos: :fontawesome-brands-windows: :simple-linux: | :star::star::star:             | https://code.visualstudio.com/ |
| 妙言   | :simple-macos:                                             | :star::star:                   | https://miaoyan.app/           |

## 参考

> [1] CSDN，@HongtaiWolf，[Mac下使用Homebrew安装nginx报错](https://blog.csdn.net/D516701881/article/details/107421940)
>
> [2] 知乎，@seay，[手把手教从零开始在GitHub上使用Hexo搭建博客教程(一)-附GitHub注册及配置](https://zhuanlan.zhihu.com/p/22405775)
>
> [3] CSDN，@yucicheung，[为GitHub Page绑定自定义域名并实现HTTPS访问 ](https://blog.csdn.net/yucicheung/article/details/79560027)
>
> [4] 知乎，@Momo，[MWeb配合Hexo高效管理博客](https://zhuanlan.zhihu.com/p/30513914)

