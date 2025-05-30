---
title: C中设计Array
date: 2025.04.12
---

### 1. `Array1`设计

```C
typedef struct
{
    f64*  data;
    usize length;
} Array1;
```

>`.data`是一个指向数组的指针

使用时：
```C
f64    mem_f64[20];   // 先申请内存
Array1 arr;
arr.data = mem_f64;   // 将数组赋值给arr1
```

数据遍历：
```C
void fuck_Array1(Array1 arr)
{
    printf("Array1::\n");
    printf("  .length: %zu\n", arr.length);
    printf("  .data: ");

    for (usize i = 0; i < arr.length; i++) {
        printf("%.4f ", arr.data[i]);
    }
    printf("\n");
}
```

### 2. Array2设计

```C
typedef struct
{
    f64** view;   // 指向指针数组的指针
    usize length;
    usize ndim;
} Array2D_View;   // Array2只有视图，指向保存指针的数组
```

> `.view`: 指向二维数组
>
> `.length`: 行数
>
> `.ndim`: 列数

使用静态声明：必须要创建一个指向有效数据的指针数组，再传递给`.view`
```C
f64  mem_f64[40];    // 有效数据数组
f64* mem_f64p[20];   // 指向每行首元素的指针数组

for (usize i = 0; i < 20; i++) {
    for (usize j = 0; j < 2; j++) {
        mem_f64[i * 2 + j] = xxx;   // 有效数组赋值
    }
    mem_f64p[i] = &mem_f64[i * 2];   // 指针数组赋值，指向行首元素
}

Array2D_View arr2 = {0};
arr2.view         = mem_f64p;   // 指向指针数组
arr2.length       = arr1_20_1.length;
arr2.ndim         = 2;
```

> 使用动态声明内存会简单很多

遍历：

```C
void fuck_Array2(Array2D_View arr)
{
    printf("Array2::\n");
    printf("  .length: %zu\n", arr.length);
    printf("  .ndim: %zu\n", arr.ndim);
    printf("  .view: \n");

    for (int i = 0; i < arr.length; i++) {
        for (int j = 0; j < arr.ndim; j++) {
            printf("[%d,%d]=", i,j);
            printf("%f ", arr.view[i][j]);
        }
        printf("\n");
    }
}
```


### 3. 悬空引用

```C
usize  superb_len = (data->length < data->ndim ? data->length : data->ndim) + 1;
f64    mem_f64[superb_len];

Array1 superb   = {0};
superb.data     = mem_f64;
```

！！！这里的`superb`不能设置为`static`。

* mem_f64是一个局部变量，因为需要计算`superb_len`，所以肯定不能设置为`static`
* 当局部变量`mem_f64`赋值给静态变量时，如果生命周期结束，内存被释放，`superb.data`仍然持有对`mem_f64`的引用，就导致了__悬空引用__（dangling reference）