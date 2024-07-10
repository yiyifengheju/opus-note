---
title: Streamlit调用C
date: 2023.12.15
comments: true
---


### 1. 输入的路径参数不能用双斜杠

对C工程生成的`.exe`传入参数，不能使用双斜杠，在程序内部C工程会再加个斜杠变成三斜杠

### 2. 不能使用windows的powershell，而是要用cmd

调试过程中，使用powershell总是无法将参数传入，使用cmd就可以正常使用

```powershell
cmd
```

### 3. 路径不能太长（命令长度传入有限制）

最好不要把绝对路径直接作为参数通过cmd命令传入`.exe`程序，当绝对路径过长的时候，会导致传入字符被截断

### 4. vs调试中模拟传入参数测试

解决方案 —— 属性 —— 调试 —— 命令参数 —— 填入需要调试的参数，在VS中再次执行程序的时候会将调试参数自动添加

### 5. C语言获得当前路径

```C
#include <stdio.h>
#include <stdlib.h>

int main() {
    char path[1024];
    if (_getcwd(path, sizeof(path)) != NULL) {
        printf("当前执行路径：%s\n", path);
    } else {
        perror("获取当前执行路径失败");
        return -1;
    }
    return 0;
}
```

当在Python中使用cmd命令调用某路径下`.exe`获取路径时，会获得Python程序的执行路径。比如说：

```python
cmd = f"'./path/to/main.exe' {target} {theme}"
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
```

