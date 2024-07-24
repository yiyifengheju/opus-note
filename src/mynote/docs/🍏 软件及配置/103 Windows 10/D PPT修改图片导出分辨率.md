---
title: D 修改PPT图片导出分辨率
comments: true
---

默认情况下，要另存为图片的 PowerPoint 幻灯片的导出分辨率为每英寸 96 点 (dpi)。 若要更改导出分辨率，请执行以下步骤：

第一步，退出所有 Windows 程序。

第二步，右键单击“开始”，然后选择“运行”。 

第三步，在“打开”框中，键入“regedit”，然后选择“确定”。

第四步，根据你使用的 PowerPoint 版本，找到以下注册表子项之一：

PowerPoint 2016、PowerPoint 2019、Microsoft 365 专属 PowerPoint

```
HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\PowerPoint\Options
```

??? note "其他版本"

    PowerPoint 2013
    
    **HKEY_CURRENT_USER\Software\Microsoft\Office\15.0\PowerPoint\Options**
    
    PowerPoint 2010
    
    **HKEY_CURRENT_USER\Software\Microsoft\Office\14.0\PowerPoint\Options**
    
    PowerPoint 2007
    
    **HKEY_CURRENT_USER\Software\Microsoft\Office\12.0\PowerPoint\Options**
    
    PowerPoint 2003
    
    **HKEY_CURRENT_USER\Software\Microsoft\Office\11.0\PowerPoint\Options**

第五步，单击“选项”子项，指向“编辑”菜单上的“新建”，然后选择“DWORD (32 位)值”。

第六步，输入“ExportBitmapResolution”，然后按 Enter 键。

第七步，确保选中“ExportBitmapResolution”，然后选择“编辑”菜单上的“修改”。

第八步，在“编辑 DWORD 值”对话框中选择“十进制”。

第九步，在“数值数据”框中，输入分辨率“300”。 或使用下表中的参数。

??? note "分辨率参数"

    | 十进制值     | 全屏像素（水平 × 垂直） | 宽屏像素（水平 + 垂直） | 每英寸点数（水平和垂直） |
    | :----------- | :---------------------- | :---------------------- | :----------------------- |
    | 50           | 500 × 375               | 667 × 375               | 50 dpi                   |
    | 96（默认值） | 960 × 720               | 1280 × 720              | 96 dpi                   |
    | 100          | 1000 × 750              | 1333 × 750              | 100 dpi                  |
    | 150          | 1500 × 1125             | 2000 × 1125             | 150 dpi                  |
    | 200          | 2000 × 1500             | 2667 × 1500             | 200 dpi                  |
    | 250          | 2500 × 1875             | 3333 × 1875             | 250 dpi                  |
    | 300          | 3000 × 2250             | 4000 × 2250             | 300 dpi                  |

最后，确定并退出注册表编辑器