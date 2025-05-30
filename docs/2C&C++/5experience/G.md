---
title: C工程化常见报错
date: 2025.04.12
---

### 1. 进程已结束，退出代码为 -1073741701 (0xC000007B)

【问题解析】进程退出代码 `-1073741701 (0xC000007B)` 通常表示 `STATUS_INVALID_IMAGE_FORMAT`，这意味着程序尝试加载一个无效的
DLL 文件。

【问题解决】

第一步，先把`.lib`、`.dll`复制到`.exe`同级目录下，运行是否报错（在这一步解决了）

第二步，想办法将动态链接库添加到环境变量

### 2. 进程已结束，退出代码为 -1073741819 (0xC0000005)

【问题解析】进程退出代码 `-1073741819 (0xC0000005)` 通常表示 `STATUS_ACCESS_VIOLATION`，这意味着程序尝试访问它没有权限访问的内存地址

【问题解决】字符串编程上的错误，导致内存出错

### 3. 进程已结束，退出代码为 -1073740791 (0xC0000409)

```C
const char *model_path = "D:/Projects/CLionProjects/test/model4.onnx";
OrtSession *session;
ORT_ABORT_ON_ERROR(
  g_ort->CreateSession(env, model_path, session_options, &session));
verify_input_output_count(session);
```

报错：

```bash
Load model from 悌勫€讲鏁懀饨充眱娼╁伄娼叉暘鐟ｂ匠鏁寸懗娲懐姹モ复婀‘ failed:Load model 悌勫€讲鏁懀饨充眱

娼╁伄娼叉暘鐟ｂ匠鏁寸懗娲懐姹モ复婀‘ failed. File doesn't exist
```

【问题解析】

1. 进程退出代码 `-1073740791 (0xC0000409)` 通常表示 `STATUS_STACK_BUFFER_OVERRUN`，这意味着程序检测到了堆栈缓冲区溢出
2. ONNX使用`ORTCHAR_T`类型表示模型路径，需要使用宽字符表示路径，尤其是在路径包含非ASCII字符时

【问题解决】

```
ORTCHAR_T *model_path = L"D:/Projects/CLionProjects/test/model4.onnx";
```

1. 使用`L`前缀将字符串转为宽字符字符串
2. 使用`ORTCHAR_T`类型表示模型路径

### 4. Output tensor is not float type.

```bash
Output tensor is not float type.
?[0;93m2025-03-13 11:04:10.1041634 [W:onnxruntime:, execution_frame.cc:876 onnxruntime::ExecutionFrame::VerifyOutputSize
s] Expected shape from model of {-1} does not match actual shape of {1,1} for output predictions?[m
```