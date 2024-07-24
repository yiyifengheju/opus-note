---
title: B Numpy
comments: true
---

### 1. 求离散序列的梯度[^1]

```python
res = np.gradient(data)
```

??? note "代码"

    ```python
    import matplotlib.pyplot as plt
    import numpy as np
    import scienceplots
    
    plt.style.use('mastermao-simtimes')


    def plot_fig(x1, x2, title):
        figure, ax = plt.subplots(2, 1, figsize=(7.05, 3), constrained_layout=True)
        ax[0].plot(x1, label='y')
        ax[0].legend(loc='upper right')
        ax[0].set(title='Sin(x) + Noise')
    
        ax[1].plot(x2, label='$\partial$y/$\partial$x')
        ax[1].legend(loc='upper right')
        ax[1].set(title='Gradient')
        plt.savefig(f'./{title}.webp')
        plt.show()


    if __name__ == '__main__':
        x = np.linspace(0, 10, 100)
        y = 5 * np.sin(x) + np.random.random(100)
        dy = np.gradient(y)
        plot_fig(y, dy, 'Partial')
    ```


![Partial](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/Partial.webp)

### 2. 替换nan

```python
res = np.nan_to_num(data, nan=0)
```

??? note "代码"

    ```python
    import numpy as np
    
    x = np.array([[1, 2], [2, 3], [np.nan, 3]])
    y = np.nan_to_num(x, nan=0)
    print(x)
    print(y)
    ```

```
array([[ 1.,  2.],
       [ 2.,  3.],
       [nan,  3.]])
array([[1., 2.],
       [2., 3.],
       [0., 3.]])
```

### 3. 合并数组

```python
res = np.concatenate((a,b), axis=0)
```

??? note "代码"

    ```
    import numpy as np
    
    a = np.ones((2,3,5))
    b = np.zeros((3,3,5))
    res = np.concatenate((a,b),axis=0)
    print(res)
    ```

```
array([[[1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.]],
       [[1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.]],
       [[0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.]],
       [[0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.]],
       [[0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.]]])
```



[^1]: CSDN，@June，[numpy的梯度函数np.gradient(f)](https://blog.csdn.net/MachineLearner/article/details/104403097)