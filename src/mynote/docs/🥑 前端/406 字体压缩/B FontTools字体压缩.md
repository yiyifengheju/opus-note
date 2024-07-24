---
title: B FontTools字体压缩
comments: true
---

> 使用Python库压缩字体

第一步，安装`fonttools`包[^1]

```bash
pip install fonttools
```

第二步，下载[`sc_unicode.txt`](https://gist.githubusercontent.com/imaegoo/d64e5088b723c2e02c40985f55ff12db/raw/5ebd2ce49418c73459a9dfe050483409306a6c1d/sc_unicode.txt)

第三步，`NotoSerifSC.otf`、`sc_unicode.txt`放在同级目录下，执行压缩命令：

```bash
pyftsubset NotoSerifSC.otf --unicodes-file=sc_unicode.txt
```

生成`NotoSerifSC.subset.otf`字体（亲测可用）

| 字体            | 压缩前 | 压缩后 | 压缩比 |
| --------------- | ------ | ------ | ------ |
| NotoSerifSC.otf | 10.6MB | 2.33MB | 21.98% |



[^1]: CSDN，@littleduo，[有效的压缩字体方法](https://blog.csdn.net/littleduo/article/details/124563106)
