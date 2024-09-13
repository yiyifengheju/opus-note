---
title: 📪 修复4K分辨率下指针过小
date: 2021-06-01
comments: true
---

4K屏下，鼠标指针小的可怜，经常补兵找不到指针、打团找不到指针、商店购物钱不够

__第一步__，修改`英雄联盟/Game/Config/game.cfg`：

```ini
[General]
+ CursorOverride=0
+ CursorScale=3.0000
```

> `CursorScale`控制放大倍数，`3.0000`表示放大到`300%`

__第二步__，修改`英雄联盟/Game/Config/PersistedSettings.json`：

```json
{
    "name": "CursorOverride",
    "value": "0"
},
{
    "name": "CursorScale",
    "value": "3.0000"
},
```

__第三步__，设置`英雄联盟/Game/Config/PersistedSettings.json`为__只读__

