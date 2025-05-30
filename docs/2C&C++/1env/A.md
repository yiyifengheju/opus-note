---
title: 🧁 CLion代码格式化
date: 2025.02.27
comments: true
---



!!! note "CLion支持的格式化工具"

    1. 内置代码格式化器：使用`Ctrl + Alt + L`格式化代码
    2. ClangFormat：CLion可以集成ClangFormat，并自定义配置`.clang-format`代码风格
    3. Astyle（Artistic Style）：一个外部工具，可以通过File Watcher调用

## 壹丨 Astyle配置

!!! warning "弃用"

```
通过实参传入的方式可调整的内容有限，且保存时触发不符合使用习惯
```

第一步，通过MSYS2安装astyle[^1]

```bash
# clang64为例：
pacman -S mingw-w64-clang-x86_64-astyle
```

第二步，CLion安装插件`File Watchers`（CLion不自带，需要额外安装）

第三步，CLion：工具——File Watcher，添加[^2]：

```yaml
名称: astyle
文件类型: C/C++
作用域: 项目文件
程序: D:\msys64\clang64\bin\astyle
实参: -i $FileName$ --style=allman --indent=spaces=4 --align-pointer=type --attach-closing-while --indent-col1-comments --pad-oper --pad-comma --pad-header --add-braces --mode=c
要刷新的输出路径: $FileName$
工作目录: $FileDir$
```

> 每次使用时会自动生成一个`.orig`备份，可以通过实参前加`-n`取消自动生成，如：
>
> ```bash
> -n -i $FileName$ ...
> ```
>
> 建议取消勾选`自动保存编辑的文件以触发观察程序`

## 贰丨 ClangFormat配置

第一步，项目目录下新建`.clang-format`，配置以下内容[^3]：

??? note ".clang-format"

    ```yaml
    # https://clang.llvm.org/docs/ClangFormatStyleOptions.html
    # https://www.bbsmax.com/A/VGzlMjexJb/
    
    # 语言: None, Cpp, Java, JavaScript, ObjC, Proto, TableGen, TextProto
    Language: Cpp
    
    BasedOnStyle: LLVM
    
    # 访问说明符(public、private等)的偏移
    AccessModifierOffset: -4
    
    # 左括号(左圆括号、左尖括号、左方括号)后的对齐: Align, DontAlign, AlwaysBreak(总是在左括号后换行)
    AlignAfterOpenBracket: AlwaysBreak
    
    # 连续赋值时，对齐所有等号
    AlignConsecutiveAssignments: true
    
    # 连续声明时，对齐所有声明的变量名
    AlignConsecutiveDeclarations: true
    
    # 对齐连续位域字段的风格
    # AlignConsecutiveBitFields: AcrossEmptyLinesAndComments
    
    # 对齐连续宏定义的风格
    # AlignConsecutiveMacros: Consecutive #clang-format 12
    AlignConsecutiveMacros: Consecutive
    
    # 用于在使用反斜杠换行中对齐反斜杠的选项
    AlignEscapedNewlines: Left
    
    # 水平对齐二元和三元表达式的操作数
    AlignOperands: Align
    
    # 对齐连续的尾随的注释
    AlignTrailingComments: true
    
    # 如果函数调用或带括号的初始化列表不适合全部在一行时
    # 允许将所有参数放到下一行，即使BinPackArguments为false
    AllowAllArgumentsOnNextLine: true
    
    # 允许构造函数的初始化参数放在下一行
    AllowAllConstructorInitializersOnNextLine: true
    
    # 允许函数声明的所有参数在放在下一行
    AllowAllParametersOfDeclarationOnNextLine: true


    # 允许短的块放在同一行(Always 总是将短块合并成一行，Empty 只合并空块)
    AllowShortBlocksOnASingleLine: Empty
    
    # 允许短的case标签放在同一行
    AllowShortCaseLabelsOnASingleLine: true
    
    # 允许短的函数放在同一行: None, InlineOnly(定义在类中), Empty(空函数), Inline(定义在类中，空函数), All
    AllowShortFunctionsOnASingleLine: Inline
    
    # 允许短的if语句保持在同一行
    AllowShortIfStatementsOnASingleLine: true
    
    # 允许短的循环保持在同一行
    AllowShortLoopsOnASingleLine: true
    
    # 总是在定义返回类型后换行(deprecated)
    AlwaysBreakAfterDefinitionReturnType: None
    
    # 总是在返回类型后换行: None, All, TopLevel(顶级函数，不包括在类中的函数), 
    #   AllDefinitions(所有的定义，不包括声明), TopLevelDefinitions(所有的顶级函数的定义)
    
    # 函数声明返回类型后是否换行(None 自动，All全部，TopLevel...)
    AlwaysBreakAfterReturnType: None
    
    # 总是在多行string字面量前换行
    AlwaysBreakBeforeMultilineStrings: false
    
    # 总是在template声明后换行
    BreakTemplateDeclarations: No
    
    # false表示函数实参要么都在同一行，要么都各自一行
    BinPackArguments: false
    
    # false表示所有形参要么都在同一行，要么都各自一行
    BinPackParameters: false
    
    # 大括号换行，只有当 BreakBeforeBraces 设置为Custom时才有效
    BraceWrapping:
      # case 语句后面
      AfterCaseLabel: true
      # class定义后面
      AfterClass: true
      # 控制语句后面
      AfterControlStatement: Never
      # enum定义后面
      AfterEnum: true
      # 函数定义后面
      AfterFunction: true
      # 命名空间定义后面
      AfterNamespace: false
      # ObjC定义后面
      AfterObjCDeclaration: false
      # struct定义后面
      AfterStruct: true
      # union定义后面
      AfterUnion: true
      # extern 导出块后面
      AfterExternBlock: false
      # catch之前
      BeforeCatch: true
      # else之前
      BeforeElse: true
      # 缩进大括号(整个大括号框起来的部分都缩进)
      IndentBraces: false
      # 空函数的大括号是否可以在一行
      SplitEmptyFunction: false
      # 空记录体(struct/class/union)的大括号是否可以在一行
      SplitEmptyRecord: false
      # 空名字空间的大括号是否可以在一行
      SplitEmptyNamespace: false
    
    # 在二元运算符前换行: None(在操作符后换行), NonAssignment(在非赋值的操作符前换行), All(在操作符前换行)
    BreakBeforeBinaryOperators: None
    
    # 在大括号前换行: Attach(始终将大括号附加到周围的上下文), Linux(除函数、命名空间和类定义，与Attach类似), 
    #   Mozilla(除枚举、函数、记录定义，与Attach类似), Stroustrup(除函数定义、catch、else，与Attach类似), 
    #   Allman(总是在大括号前换行), GNU(总是在大括号前换行，并对于控制语句的大括号增加额外的缩进), WebKit(在函数前换行), Custom
    #   注：这里认为语句块也属于函数
    
    # 大括号的换行规则
    BreakBeforeBraces: Custom
    
    # 三元运算操作符换行位置（?和: 在新行还是尾部）
    BreakBeforeTernaryOperators: true
    
    # 在构造函数的初始化列表的逗号前换行
    BreakConstructorInitializersBeforeComma: false
    
    # 要使用的构造函数初始化式样式
    BreakConstructorInitializers: BeforeComma
    
    # 每行字符的限制，0表示没有限制
    ColumnLimit: 150
    
    # 描述具有特殊意义的注释的正则表达式，它不应该被分割为多行或以其它方式改变
    # CommentPragmas: ''
    
    # 如果为true，则连续的名称空间声明将在同一行上。如果为false，则在新行上声明每个名称空间。
    CompactNamespaces: false
    
    # 构造函数的初始化列表要么都在同一行，要么都各自一行
    ConstructorInitializerAllOnOneLineOrOnePerLine: false
    
    # 构造函数的初始化列表的缩进宽度
    ConstructorInitializerIndentWidth:  4
    
    # 延续的行的缩进宽度
    ContinuationIndentWidth: 4
    
    # 去除C++11的列表初始化的大括号{后和}前的空格
    Cpp11BracedListStyle: true
    
    # 继承最常用的指针和引用的对齐方式
    DerivePointerAlignment: false
    
    # 关闭格式化
    DisableFormat: false
    
    # 自动检测函数的调用和定义是否被格式为每行一个参数(Experimental)
    ExperimentalAutoDetectBinPacking: false
    
    # 如果为true，则clang格式会为短名称空间添加缺少的名称空间结尾注释，并修复无效的现有名称结束注释
    FixNamespaceComments: true
    
    # 需要被解读为foreach循环而不是函数调用的宏
    ForEachMacros:  [ foreach, Q_FOREACH, BOOST_FOREACH ]
    
    # 对#include进行排序，匹配了某正则表达式的#include拥有对应的优先级，匹配不到的则默认优先级为INT_MAX(优先级越小排序越靠前)，
    #   可以定义负数优先级从而保证某些#include永远在最前面
    IncludeCategories:
      - Regex:  '^"(llvm|llvm-c|clang|clang-c)/'
        Priority:   2
      - Regex:  '^(<|"(gtest|isl|json)/)'
        Priority:   3
      - Regex:  '.*'
        Priority:   1
    
    # 缩进case标签
    IndentCaseLabels: false
    
    # 要使用的预处理器指令缩进样式
    IndentPPDirectives: AfterHash
    
    # 缩进宽度
    IndentWidth: 4
    
    # 函数返回类型换行时，缩进函数声明或函数定义的函数名
    IndentWrappedFunctionNames: false
    
    # 保留在块开始处的空行
    KeepEmptyLinesAtTheStartOfBlocks: true
    
    # 开始一个块的宏的正则表达式
    MacroBlockBegin: ''
    
    # 结束一个块的宏的正则表达式
    MacroBlockEnd: ''
    
    # 连续空行的最大数量
    MaxEmptyLinesToKeep: 10
    
    # 命名空间的缩进: None, Inner(缩进嵌套的命名空间中的内容), All
    # NamespaceIndentation: Inner
    
    # 使用ObjC块时缩进宽度
    ObjCBlockIndentWidth: 4
    
    # 在ObjC的@property后添加一个空格
    ObjCSpaceAfterProperty: false
    
    # 在ObjC的protocol列表前添加一个空格
    ObjCSpaceBeforeProtocolList: true
    
    # 在call(后对函数调用换行的penalty
    PenaltyBreakBeforeFirstCallParameter: 2
    
    # 在一个注释中引入换行的penalty
    PenaltyBreakComment: 300
    
    # 第一次在<<前换行的penalty
    PenaltyBreakFirstLessLess:  120
    
    # 在一个字符串字面量中引入换行的penalty
    PenaltyBreakString: 1000
    
    # 对于每个在行字符数限制之外的字符的penalty
    PenaltyExcessCharacter: 1000000
    
    # 对每一个空格缩进字符的penalty(相对于前导的非空格列计算)
    # PenaltyIndentedWhitespace: 0 
    
    # 将函数的返回类型放到它自己的行的penalty
    PenaltyReturnTypeOnItsOwnLine: 120
    
    # 指针和引用的对齐: Left, Right, Middle
    PointerAlignment: Left
    
    # 允许重新排版注释
    ReflowComments: true
    
    # 允许排序#include
    SortIncludes: CaseInsensitive
    
    #
    IncludeBlocks: Preserve
    
    # 允许排序 using 声明顺序
    SortUsingDeclarations: false
    
    # 在C风格类型转换后添加空格
    SpaceAfterCStyleCast: false
    
    # 在逻辑非操作符(!)之后插入一个空格
    SpaceAfterLogicalNot: false
    
    # 在 template 关键字后插入一个空格
    SpaceAfterTemplateKeyword: false
    
    # 定义在什么情况下在指针限定符之前或之后放置空格
    # SpaceAroundPointerQualifiers: Before
    
    # 在赋值运算符之前添加空格
    SpaceBeforeAssignmentOperators: true
    
    # 左圆括号之前添加一个空格: Never, ControlStatements, Always
    SpaceBeforeParens: ControlStatements
    
    # 空格将在基于范围的for循环冒号之前被删除
    SpaceBeforeRangeBasedForLoopColon: true
    
    # [ 前是否添加空格（数组名和[之间，Lambdas不会受到影响）
    # 连续多个 [ 只考虑第一个（嵌套数组，多维数组）
    SpaceBeforeSquareBrackets: false
    
    # 在空的圆括号中添加空格
    SpaceInEmptyParentheses: false
    
    # 在尾随的评论前添加的空格数(只适用于//)
    SpacesBeforeTrailingComments: 3
    
    # 在尖括号的<后和>前添加空格
    SpacesInAngles: false
    
    # 在容器(ObjC和JavaScript的数组和字典等)字面量中添加空格
    SpacesInContainerLiterals:  false
    
    # 在C风格类型转换的括号中添加空格
    SpacesInCStyleCastParentheses: false
    
    # 如果为true，将在If/for/switch/while条件括号前后插入空格。
    SpacesInConditionalStatement: false
    
    # 在圆括号的(后和)前添加空格
    SpacesInParentheses: false
    
    # 在方括号的[后和]前添加空格，lamda表达式和未指明大小的数组的声明不受影响
    SpacesInSquareBrackets: false
    
    # 标准: Cpp03, Cpp11, Auto
    Standard: c++11
    
    # tab宽度
    TabWidth: 4
    
    # 使用tab字符: Never, ForIndentation, ForContinuationAndIndentation, Always
    UseTab: Never
    ```

第二步，CLion中，编辑器——代码样式——勾选`启用ClangFormat`


[^1]: MSYS2 Packages，[mingw-w64-astyle](https://packages.msys2.org/base/mingw-w64-astyle) 
[^2]: cnblogs.com，@北极的大企鹅，[Clion代码自动格式化保存](https://www.cnblogs.com/liuyangfirst/p/17568754.html)
[^3]: cnblogs.com，[ymwh@foxmail.com](mailto:ymwh@foxmail.com)，[我使用的 clang-format 配置文件](https://www.cnblogs.com/oloroso/p/14699855.html)