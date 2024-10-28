---
title: 🏝️ 串口通信
comments: true
---
第一步，安装Serial包和安装串口驱动

```bash
pip install serial
```

```bash
pip install pyserial
```

[ch340g-ch34g-ch34x-mac-os-x-driver](https://github.com/adrianmihalko/ch340g-ch34g-ch34x-mac-os-x-driver)，下载安装驱动程序

第二步，查看串口

```bash
ls /dev/tty.*
```

第三步，常见用法

```python
# 打开第一个串口
my_serial = serial.Serial(0)
# 设置串口地址、波特率
my_serial = serial.Serial(‘COM1’, 115200)

# 查看串口标识
print(my_serial.portstr) 

# 串口是否打开
my_serial.isOpen()
# 打开串口
my_serial.open() 
# 关闭串口
my_serial.close()

# 串口写数据
my_serial.write("hello")
# 串口读数据
data = my_serial.read() # 读一个字符
data = my_serial.read(20) # 读20个字符
data = my_serial.readline() # 读一行，读至/n
```

