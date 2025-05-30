---
title: C工程化经验总结
date: 2025.04.12
---



4. 静态变量一定要初始化。静态变量在使用前没有清空原来的数据，导致第一次运行影响第二次运行结果
2. 多个函数使用的数据，一定要在入参时设置为`const`指针
3. 差分与原始数据长度不一致，如：

对acc处理：python原始输入60s，截断为10s；C中直接输入10s

```Python
acc_mean = np.mean(self.acc_mag[ss : ee])
acc_dmean = np.mean(self.acc_dmag[ss : ee])
```

```C
np_mean(&self.acc_mag, &RES->ACC_MEAN);
np_mean(&self.acc_dmag, &RES->ACC_dMEAN);
```

Python中处理的`self.acc_dmag`长度为`10 * sample_rate`，而C中处理的长度为`10 * sample_rate - 1`

4. 基础数组的设计

```C
typedef struct
{
    f64*  data;
    usize length;
} Array1;
```

更灵活、更省空间

```C
typedef struct
{
    f64   data[MAX_LENGTH];
    usize length;
} Array1;
```
更不容易出错，空间效率不高


5. 数据过大过小，怎样归一化？
TODO：未解决

6. 调试时，先前已经调试过的函数，在其他位置运行时可能会结果不一致导致最终结果不一致
如：已经调试了PCA算法，但在MWPTT特征提取中发现PCA结果不一致

TODO：创建一个模拟数据接入函数，在片段中插入模拟值，以定位问题发生位置

7. 要时刻关注数据函数是否会修改入参
8. 最大的问题还是基础函数的结果一致性问题
9. usize类型的一些问题

usize类型不可以做>=0判断，下述会出现死循环

```C
for (usize idx = 10; idx >= 0; idx--) {
    printf("%zu, ", idx);
}
```

10. 工程化前尽可能将输入输出确定，如：输入信号（信号源、采样率等），确定算法流程



## 一些想法

### 1. 怎样构建内存池？

第一种，声明一长段数据，指针指向第一个元素，根据需要的size申请内存，不需要时指针重置

第二种，类似第一种，设计一个结构体，分别是内存和flag，然后链接到实例

第三种，每个数组相互独立，手动管理是否在用

第四种，（不可用）数组最后一位配置为首元素指针（指针数组和数组是不一样的，没法写在一个数组里面）

第五种，数组最后一位设为特定的数据，比如前3个数据按位与，作为在用的标记