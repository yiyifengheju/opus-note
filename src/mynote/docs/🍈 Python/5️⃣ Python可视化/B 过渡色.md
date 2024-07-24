---
title: B 过渡色
comments: true
---



为matplotlib设置过渡颜色

```python
import matplotlib.pyplot as plt
import matplotlib.colors as colors


def get_color(value):
    cmap = colors.LinearSegmentedColormap.from_list('blue_to_red', ['blue', 'red'])
    norm = colors.Normalize(vmin=0, vmax=1)
    return cmap(norm(value))


if __name__ == '__main__':
    # 测试代码
    values = [0, 0.25, 0.5, 0.75, 1]
    for value in values:
        color = get_color(value)
        print(f"Value: {value}, Color: {color}")
```