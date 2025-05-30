---
title: 🐠 Git自动提交(Windows)
comments: true
date: 2024.02.03
---

第一步，新建脚本：

```bat title="autogit.bat"
@echo off
cd /d path/to/folder
set datetime=%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%
git add .
git commit -m "upload - %datetime%"
git push http://{USER}:{PASSWD}@xxxxx.git
```

第二步，添加定时任务

搜索“任务计划程序” —— 右侧“创建基本任务” —— 按照指导添加上述计划

