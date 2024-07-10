---
title: A Doxygen生成C工程文档
comments: true
---

## 壹丨Doxygen简介

Doxygen是一个程序的文档产生工具，可以将程序中的注释转换成说明文档或者说是API参考手册，从而减少程序员整理文档的时间。当然这里程序中的注释需要遵循一定的规则书写，才能让Doxygen识别和转化。

目前Doxygen可处理的程序语言包含C/C++、Java、Objective-C、IDL等，可产生出来的文档格式有HTML、XML、LaTeX、RTF等，此外还可衍生出不少其它格式，如HTML可以打包成CHM格式，而LaTeX可以通过一些工具产生出PS或是PDF文档等。

## 贰丨Doxygen安装

Doxygen：[下载地址](https://www.doxygen.nl/download.html){:target="_blank"}

Graphviz：一种用于渲染图表的工具，[下载地址](https://graphviz.org/download/){:target="_blank"}

## 叁丨Doxygen设置



## 肆丨Doxygen注释语法

### 4.1 注释格式

块注释语法：

```
/**
...
*/
```

=== "CLion"

    在函数上方输入`/**`，回车，即可自动标准化相关变量

=== "Visual Studio"

	安装插件`Doxygen Comments`。
	
	在函数上方输入`/**`，回车，即可自动标准化相关变量



### 4.2 注释语法[^1]

```
@exception <exception-object> {exception description} 对一个异常对象进行注释。

@warning {warning message } 一些需要注意的事情

@todo { things to be done } 对将要做的事情进行注释，链接到所有TODO 汇总的TODO 列表

@bug 缺陷，链接到所有缺陷汇总的缺陷列表

@see {comment with reference to other items } 一段包含其他部分引用的注释，中间包含对其他代码项的名称，自动产生对其的引用链接。

@relates <name> 通常用做把非成员函数的注释文档包含在类的说明文档中。

@since {text} 通常用来说明从什么版本、时间写此部分代码。

@deprecated

@pre { description of the precondition } 用来说明代码项的前提条件。

@post { description of the postcondition } 用来说明代码项之后的使用条件。

@code 在注释中开始说明一段代码，直到@endcode命令。

@endcode 注释中代码段的结束。

@code .. @endcode 包含一段代码

@addtogroup 添加到一个组。

@brief  概要信息

@deprecated 已废弃函数

@details  详细描述

@note  开始一个段落，用来描述一些注意事项

@par  开始一个段落，段落名称描述由你自己指定

@param  标记一个参数的意义

@fn  函数说明

@ingroup 加入到一个组

@return  描述返回意义

@retval  描述返回值意义

@include 包含文件

@var、@enum、@struct、@class 对变量、美剧、结构体、类等进行标注
```



## 伍丨示例









[^1]: 博客园，@silencehuan，[代码注释规范之Doxygen](https://www.cnblogs.com/silencehuan/p/11169084.html)