---
title: 🤩️ 软件推荐
comments: true
---

<div class="grid cards index-info" markdown>

-   :simple-opensourceinitiative:{ .simple-opensourceinitiative .icon } &ensp;&ensp;__[开源软件](./0️⃣ 开源软件){ .icon_title }__
{ .cards }

	---

	开源软件是指源代码可以被公众访问、使用、修改和分发的软件。遵循开源许可证，如MIT、GPL等，允许用户自由地查看、修改代码。
{ .description }

	[:octicons-arrow-right-24: Getting started](./0️⃣ 开源软件)
{ .description }

-   :simple-ubuntu:{ .simple-ubuntu .icon } &ensp;&ensp;__[Linux(Ubuntu)](./1️⃣ Linux(Ubuntu)){ .icon_title }__
{ .cards }

	---

	Linux是一种开源的类UNIX操作系统，以其稳定性、安全性和灵活性闻名，广泛应用于服务器、桌面、移动设备和嵌入式系统。
{ .description }

	[:octicons-arrow-right-24: Getting started](./1️⃣ Linux(Ubuntu))
{ .description }

-   :simple-linux:{ .simple-linux .icon } &ensp;&ensp;__[WSL](./2️⃣ WSL){ .icon_title }__
{ .cards }

	---

	WSL（Windows Subsystem for Linux）是微软从Win10引入的功能，允许在Windows上运行Linux环境及其命令行工具和应用程序。
{ .description }

	[:octicons-arrow-right-24: Getting started](./2️⃣ WSL)
{ .description }

-   :fontawesome-brands-windows:{ .fontawesome-brands-windows .icon } &ensp;&ensp;__[Windows10](./3️⃣ Windows10){ .icon_title }__
{ .cards }

	---

	Windows 10是微软于2015年推出的操作系统，提供了全新的开始菜单、Cortana语音助手、Edge浏览器等功能，支持多设备无缝操作。
{ .description }

	[:octicons-arrow-right-24: Getting started](./3️⃣ Windows10)
{ .description }

-   :fontawesome-brands-windows:{ .fontawesome-brands-windows .icon } &ensp;&ensp;__[Windows11](./4️⃣ Windows11){ .icon_title }__
{ .cards }

	---

	Windows 11是微软于2021年推出的操作系统，提供了新版开始菜单，支持与时代相符的混合工作环境，并侧重于提高用户的工作效率。
{ .description }

	[:octicons-arrow-right-24: Getting started](./4️⃣ Windows11)
{ .description }

-   :simple-git:{ .simple-git .icon } &ensp;&ensp;__[Git](./5️⃣ Git){ .icon_title }__
{ .cards }

	---

	Git是一个开源的分布式版本控制系统，用于处理项目版本管理。由Linus Torvalds创建，用于软件开发中以协调代码变更和多人协作。
{ .description }

	[:octicons-arrow-right-24: Getting started](./5️⃣ Git)
{ .description }

-   :material-apple:{ .material-apple .icon } &ensp;&ensp;__[macOS](./6️⃣ macOS){ .icon_title }__
{ .cards }

	---

	macOS是苹果公司开发的桌面操作系统，专为Mac电脑设计。它以Unix为基础，提供直观的图形用户界面和强大的多任务能力。
{ .description }

	[:octicons-arrow-right-24: Getting started](./6️⃣ macOS)
{ .description }

-   :simple-leagueoflegends:{ .simple-leagueoflegends .icon } &ensp;&ensp;__[英雄联盟](./7️⃣ 英雄联盟){ .icon_title }__
{ .cards }

	---

	英雄联盟（League of Legends）是Riot Games开发的英雄对战网游，游戏以丰富的英雄角色、多样的游戏模式和团队竞技为特色。
{ .description }

	[:octicons-arrow-right-24: Getting started](./7️⃣ 英雄联盟)
{ .description }

</div>









<img src="https://raw.githubusercontent.com/nvbn/thefuck/master/example.gif">

功能：纠正输入错误的cmd命令

开源链接：https://github.com/nvbn/thefuck

!!! tip "安装（Ubuntu）"

    第一步，安装：
    
    ```bash
    sudo apt update
    sudo apt install python3-dev python3-pip python3-setuptools
    pip3 install thefuck --user
    ```
    
    第二步，添加环境变量：
    
    ```bash
    sudo nano ~/.bashrc
    ```
    
    添加：
    
    ```bash
    eval $(thefuck --alias)
    # You can use whatever you want as an alias, like for Mondays:
    eval $(thefuck --alias FUCK)
    ```
    
    第三步，激活环境：
    ```bash
    source ~/.bashrc
    ```



!!! note "升级"

    ```bash
    pip3 install thefuck --upgrade
    ```
