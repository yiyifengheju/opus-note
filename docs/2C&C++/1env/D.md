---
title: 🧁 C工程添加开源库（以FFTW为例）
comments: true
---

!!! note "FFTW"

    官网：[FFTW](http://www.fftw.org/index.html)
    
    Windows安装说明：[FFTW/install/windows](http://www.fftw.org/install/windows.html)
    
    FFTW是一个 C 子程序库，用于计算一维或多维、任意输入大小、实数和复数数据（以及偶数/奇数数据，即离散余弦/正弦变换或 DCT/DST）的离散傅里叶变换 (DFT)

!!! note "环境信息"

    操作系统：Windows 10 专业版 21H1
    
    工具链：MSYS2 + MinGW64
    
    MinGW：11.0 w64
    
    CMake：3.30.5

### 壹丨下载&安装

第一步，下载及解压缩FFTW库文件，[这里](http://www.fftw.org/install/windows.html)

第二步，基于`dlltool`工具编译`.lib`：

```bash
# 在fftw解压目录下
dlltool -d .\libfftw3-3.def -l .\libfftw3-3.lib
dlltool -d .\libfftw3l-3.def -l .\libfftw3l-3.lib
dlltool -d .\libfftw3f-3.def -l .\libfftw3f-3.lib
# -d指定.def文件，-l指定生成的.lib文件

# 输出：
# libfftw3-3.lib
# libfftw3l-3.lib
# libfftw3f-3.lib
```

第三步，将FFTW目录添加到环境变量（实测还是出现找不到动态链接库的错误，解决方法见下文）

## 贰丨CMakeLists配置

根目录`CMakeLists.txt`

```cmake
cmake_minimum_required(VERSION 3.30)
project(CPulse C)

# 设置C标准
set(CMAKE_C_STANDARD 11)

# 设置FFTW文件路径
set(FFTW_DIR "D:/Clib/fftw")

# 添加子目录
add_subdirectory(c_ndarray)
add_subdirectory(signal_processing) # 包含fft.c、fft.h

# 添加可执行文件
add_executable(${PROJECT_NAME} main.c)

# 链接库
target_link_directories(${PROJECT_NAME} PUBLIC "${FFTW_DIR}")
target_link_libraries(${PROJECT_NAME} signal_processing c_ndarray fftw3-3 fftw3f-3 fftw3l-3)

# 指定头文件搜索路径
target_include_directories(${PROJECT_NAME} PUBLIC signal_processing "${FFTW_DIR}")
signal_processing`目录下`CMakeLists.txt
add_library(signal_processing fft.c fft.h)
target_include_directories(signal_processing PUBLIC ${CMAKE_CURRENT_SOURCE_DIR} ${FFTW_DIR})
```

## 叁丨测试用例

```
#include <fftw3.h>
#include "../c_ndarray/c_ndarray.h"

Array1_Complex rfft(const Array1 *in_signal) {
    usize N = in_signal->length;
    f64 in[N];
    fftw_complex out[N];

    for (i32 i = 0; i < N; i++) {
        in[i] = in_signal->data[i];
    }

    fftw_plan p = fftw_plan_dft_r2c_1d((i32)N, in, out, FFTW_ESTIMATE);
    fftw_execute(p);

    Array1_Complex res = {0};
    for (usize i = 0; i < N; i++) {
        res.data[i].real = out[i][0];
        res.data[i].imag = out[i][1];
    }
    res.length = N / 2 + 1;
    return res;
}
```

## 叁丨错误及解决

### 1. 运行报错：`进程已结束，退出代码为 -1073741515 (0xC0000135)`

【原因】表明没有找到所需的DLL文件

【解决方法1】将`libfftw3-3.dll`、`libfftw3f-3.dll`、`libfftw3l-3.dll`文件复制到`.exe`同级目录，如：CLion工程目录的`cmake-build-debug`文件夹下

【解决方法2】将`libfftw3-3.dll`、`libfftw3f-3.dll`、`libfftw3l-3.dll`文件复制到MinGW64的bin目录下，如：`C:\mingw64\bin`

【无效方法】将上述DLL所在目录添加到环境变量（可能是我没重启IDE）

### 2. 在`#include <fftw3.h>`显示找不到文件

【原因】没有在子模块的`CMakeLists`添加FFTW路径

【解决方法】见<贰>