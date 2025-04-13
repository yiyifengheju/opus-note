---
title: 为C工程生成类似Rust的版本信息
date: 2025.04.12
---



要点：

1. 获取Git Commit信息

   ```bash
   git rev-parse --short HEAD
   ```

2. 获取依赖版本信息

   ```bash
   # 查找包
   pacman -Qs GSL
   
   # local/mingw-w64-clang-x86_64-gsl 2.8-1
   #     The GNU Scientific Library (GSL) is a modern numerical library for C and C++ programmers
   #     (mingw-w64)
   # local/mingw-w64-x86_64-gsl 2.8-1
   #     The GNU Scientific Library (GSL) is a modern numerical library for C and C++ programmers
   #     (mingw-w64)
   ```


## 壹丨操作方法

第一步，新建版本文件`~/VERSION`：

```
2025.2.0
```

第二步，新建脚本`~/auto_version.sh`：

```bash
#!/bin/bash

# 获取Commit Hash
COMMIT_HASH=$(git rev-parse --short HEAD)
# 获取分支名
BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)
# 获取Commit日期
COMMIT_DATE=$(git log -1 --format=%cd)
# 获取Git用户名、邮箱
GIT_USER_NAME=$(git config user.name)
GIT_USER_EMAIL=$(git config user.email)

# 获取版本号
VERSION=$(cat VERSION)

# 获取平台信息
PLATFORM=$(uname -s)
ARCH=$(uname -m)

# 依赖包版本
FFTW_VERSION=$(pacman -Qi mingw-w64-clang-x86_64-fftw | grep Version | awk '{print $3}')
GSL_VERSION=$(pacman -Qi mingw-w64-clang-x86_64-gsl | grep Version | awk '{print $3}')

# 生成version_info.h头文件
cat <<EOL > version_info.h
#ifndef CPULSE_VERSION_INFO_H
#define CPULSE_VERSION_INFO_H

#define GIT_COMMIT_HASH "$COMMIT_HASH"
#define GIT_BRANCH_NAME "$BRANCH_NAME"
#define GIT_COMMIT_DATE "$COMMIT_DATE"
#define GIT_USER_NAME "$GIT_USER_NAME"
#define GIT_USER_EMAIL "$GIT_USER_EMAIL"

#define PROJECT_VERSION "$VERSION"
#define BUILD_PLATFORM "$PLATFORM"
#define BUILD_ARCH "$ARCH"

#define FFTW_VERSION "$FFTW_VERSION"
#define GSL_VERSION "$GSL_VERSION"

#endif // CPULSE_VERSION_INFO_H
EOL

# 添加头文件
git add version_info.h
```

第三步，代码中包含头文件：

```C
#include "version_info.h"

void fuck_version()
{
    printf("CPulse %s\n", PROJECT_VERSION);
    printf("Author: %s (%s)\n", GIT_USER_NAME, GIT_USER_EMAIL);
    printf("Commit: %s (%s %s)\n", GIT_BRANCH_NAME, GIT_COMMIT_HASH, GIT_COMMIT_DATE);
    printf("Platform: %s (%s)\n", BUILD_PLATFORM, BUILD_ARCH);
    printf("FFTW3: %s\n", FFTW_VERSION);
    printf("GSL: %s\n", GSL_VERSION);
}
```

第四步，编译前运行脚本。可以在CMakeLists中添加规则：

```
TODO

```