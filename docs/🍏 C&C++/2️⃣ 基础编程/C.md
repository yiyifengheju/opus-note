---
title: 🧰 errno常见错误类型
comments: true
---

1. **`EPERM` (1)** : 操作不允许。通常表示没有权限执行某个操作。
2. **`ENOENT` (2)** : 没有这样的文件或目录。表示尝试访问的文件或目录不存在。
3. **`ESRCH` (3)** : 没有这样的进程。表示尝试访问的进程不存在。
4. **`EINTR` (4)** : 被信号中断。表示系统调用被信号中断。
5. **`EIO` (5)** : 输入/输出错误。表示发生了输入/输出错误。
6. **`ENXIO` (6)** : 设备或地址不存在。表示设备不存在或没有可用的地址。
7. **`E2BIG` (7)** : 参数列表太长。表示传递给程序的参数列表过长。
8. **`ENOEXEC` (8)** : 可执行文件格式错误。表示尝试执行的文件不是有效的可执行文件。
9. **`EBADF` (9)** : 坏文件描述符。表示文件描述符无效。
10. **`ECHILD` (10)** : 当前进程没有子进程。表示尝试等待的子进程不存在。
11. **`EAGAIN` (11)** : 资源暂时不可用。表示资源暂时不可用，通常用于非阻塞操作。
12. **`ENOMEM` (12)** : 内存不足。表示无法分配足够的内存。
13. **`EACCES` (13)** : 权限被拒绝。表示没有权限访问文件或目录。
14. **`EFAULT` (14)** : 错误的地址。表示传递给函数的指针无效。
15. **`EBUSY` (16)** : 设备或资源忙。表示设备或资源正在使用中。
16. **`EEXIST` (17)** : 文件已存在。表示尝试创建已存在的文件。
17. **`EXDEV` (18)** : 跨设备链接。表示尝试在不同设备之间创建链接。
18. **`ENODEV` (19)** : 没有这样的设备。表示设备不存在。
19. **`ENOTDIR` (20)** : 不是目录。表示尝试访问的路径不是目录。
20. **`EISDIR` (21)** : 是目录。表示尝试对目录执行不允许的操作。
21. **`EINVAL` (22)** : 无效参数。表示传递给函数的参数无效。
22. **`ENFILE` (23)** : 文件表溢出。表示系统打开的文件数量超过限制。
23. **`EMFILE` (24)** : 进程打开的文件数超过限制。表示当前进程打开的文件数量超过限制。
24. **`ENOTTY` (25)** : 不是终端设备。表示尝试对非终端设备执行终端操作。
25. **`ETXTBSY` (26)** : 文本文件忙。表示尝试执行正在被其他进程使用的文本文件。
26. **`EFBIG` (27)** : 文件太大。表示尝试写入的文件超过了系统限制。
27. **`ENOSPC` (28)** : 设备上没有空间。表示设备没有足够的空间来完成操作。
28. **`ESPIPE` (29)** : 非法的寻址。表示尝试在不支持的文件描述符上执行操作。
29. **`EROFS` (30)** : 只读文件系统。表示尝试在只读文件系统上写入。
30. **`EMLINK` (31)** : 链接数量过多。表示尝试创建的链接数量超过限制。
31. **`EPIPE` (32)** : 管道破裂。表示尝试写入已关闭的管道。
32. **`EDOM` (33)** : 数学参数超出范围。表示传递给数学函数的参数超出范围。
33. **`ERANGE` (34)** : 数学结果超出范围。表示数学运算的结果超出范围。