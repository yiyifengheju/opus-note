---
title: 📪 Win10常见报错及修复
comments: true
---
### 1. win10开始菜单磁贴只有背景

解决方法：重启explorer

**方法一**：使用命令提示符：

```powershell
taskkill /f /im explorer.exe
```

```powershell
start explorer
```

**方法二**：`Ctrl`+`Alt`+`Del`打开任务管理器，选中`Windows 资源管理器`，结束任务（此方法同样适用于部分情况下的电脑卡死问题）

### 2. Word、PPT 等拖动闪退

解决方法：禁用硬件加速

**方法一**：GUI界面关闭硬件加速

文件——选项——高级——禁用硬件加速

**方法二**：修改注册表

第一步，Win+R——打开regedit

第二步，找到  HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Common

第三步，新建——项——命名 Graphics

第四步，Graphics——新建——DWORD值——DisableHardwareAcceleration

第五步，DisableHardwareAcceleration双击——0改为1

### 3. Chrome系浏览器打开全黑

解决方法：关闭硬件加速

属性——快捷方式——目标——添加“ --disable-gpu --disable-software-rasterize”

### 4. 软件开启高DPI

> 使用2K、4K屏时，一些软件如美图秀秀、央视影音等显示的非常小，原因是没有适配高DPI，可以手动设置下。

快捷方式——右键“属性”——兼容性——更改高DPI设置——高DPI缩放替代——勾选替代高DPI缩放行为——缩放执行选择“系统（增强）”



<img src="https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/image-20211217185849972.webp" width="60%" />





