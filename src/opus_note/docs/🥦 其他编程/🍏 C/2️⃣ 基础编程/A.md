---
title: 💖 基础编程
comments: true
---

### 1. `strcpy()` —— 字符串复制函数

`strcpy` 是一个 C 语言标准库函数，用于将一个字符串（以 null 字符 `\0` 结尾）复制到另一个字符串数组中。

```c
char *strcpy(char *dest, const char *src);
```
`strcpy` 函数接受两个参数，`dest` 和 `src`，分别表示目标字符串和源字符串。函数将源字符串的内容复制到目标字符串中，包括 null 字符 `\0`，并返回指向目标字符串的指针。
需要注意的是，目标字符串必须具有足够的空间来容纳源字符串的内容，否则可能导致缓冲区溢出的问题。此外，使用 `strcpy` 时需要确保源字符串以 null 字符结尾，否则可能会导致不可预测的行为。
```c
#include <stdio.h>
#include <string.h>
int main() {
    char source[] = "Hello, World!";
    char destination[20];
    strcpy(destination, source);
    printf("Source string: %s\n", source);
    printf("Copied string: %s\n", destination);
    return 0;
}
```

输出结果为：

```
Source string: Hello, World!
Copied string: Hello, World!
```

### 2. `strcat()` —— 字符串拼接函数

`strcat` 是一个 C 语言标准库函数，用于将一个字符串（以 null 字符 `\0` 结尾）追加到另一个字符串的末尾。

```c
char *strcat(char *dest, const char *src);
```
`strcat` 函数接受两个参数，`dest` 和 `src`，分别表示目标字符串和源字符串。函数将源字符串的内容追加到目标字符串的末尾，并返回指向目标字符串的指针。
需要注意的是，目标字符串必须具有足够的空间来容纳源字符串的内容，否则可能导致缓冲区溢出的问题。此外，使用 `strcat` 时需要确保目标字符串已经以 null 字符结尾，否则可能会导致不可预测的行为。
```c
#include <stdio.h>
#include <string.h>
int main() {
    char destination[20] = "Hello, ";
    char source[] = "World!";
    strcat(destination, source);
    printf("Concatenated string: %s\n", destination);
    return 0;
}
```

输出结果为：

```
Concatenated string: Hello, World!
```

### 3. `sprintf()` —— 字符串写入函数

`sprintf` 是一个 C 语言标准库函数，用于将格式化的数据写入一个字符串中。

```c
int sprintf(char *str, const char *format, ...);
```
`sprintf` 函数接受多个参数，其中 `str` 是指向目标字符串的指针，`format` 是格式化字符串，后面的参数是根据格式化字符串中的格式符，用于替换相应的值。
`sprintf` 函数按照指定的格式将数据转换为字符串，并将结果写入目标字符串 `str` 中。它的返回值是写入到目标字符串中的字符数（不包括终止的 null 字符 `\0`）。
格式化字符串 `format` 可以包含普通字符和格式控制符，例如 `%d` 表示将整数转换为字符串，`%f` 表示将浮点数转换为字符串，`%s` 表示将字符串复制到结果中等等。通过在格式化字符串中插入格式控制符，并在后面的参数中提供相应的值，可以将这些值转换为字符串并插入到目标字符串中。
```c
#include <stdio.h>
int main() {
    char str[50];
    int age = 30;
    float height = 1.75;
    sprintf(str, "I am %d years old and %.2f meters tall.", age, height);
    printf("Formatted string: %s\n", str);
    return 0;
}
```

输出结果为：

```
Formatted string: I am 30 years old and 1.75 meters tall.
```

> 有点像Python里的f-string