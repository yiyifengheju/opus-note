---
title: PyTorch
date: 2025.03.10
---

### 1. RuntimeError: use_libuv was requested but PyTorch was build without libuv support

解决方法：将`use_libuv`禁用：在`.env`中添加环境变量：

```toml
USE_LIBUV="0"
```

> 参考：https://github.com/RVC-Boss/GPT-SoVITS/issues/1357

### 2. TypeError: Descriptors cannot not be created directly. - protobuf version bug

问题分析：问题根源来自于`protobuf`库在`4.21.0`版本发生更改。

解决方法：将`protobuf`降级

```bash
rye add protobuf==3.21.1
```

参考：

https://github.com/RVC-Boss/GPT-SoVITS/issues/1357