---
title: C 标签
comments: true
---

示例标签：

```python
url = 'https://img.shields.io/badge/swift-F54A2A?style=for-the-badge&logo=swift&logoColor=white'
```

使用：

```html
<img src="https://img.shields.io/badge/swift-F54A2A?style=for-the-badge&logo=swift&logoColor=white">
```

<img src="https://img.shields.io/badge/swift-F54A2A?style=for-the-badge&logo=swift&logoColor=white">

快速新建标签：

```python
def make_label(message,color1,logo,color2):
    url=f'https://img.shields.io/badge/{message}-{color1}?style=for-the-badge&logo={logo}&logoColor={color2}'
    print(url)

make_label('swift','F54A2A','swift','white')
```



