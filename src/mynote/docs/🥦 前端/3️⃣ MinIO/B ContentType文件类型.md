---
title: B ContentType文件类型
comments: true
---

Content-Type即内容类型，用于定义网络文件的类型和网页的编码，决定文件接收方将以什么形式、什么编码读取这个文件。

ContentType属性指定响应的 HTTP内容类型，如果未指定，默认为TEXT/HTML。

!!! note "常见的Content-Type[^1]"

    ```
    text/html  ：HTML格式
    text/plain ：纯文本格式      
    text/xml   ：XML格式
    
    image/gif  ：gif图片格式    
    image/jpeg ：jpg图片格式 
    image/png  ：png图片格式
    
    application/xml     ： XML数据格式
    application/json    ： JSON数据格式
    application/pdf     ： pdf格式  
    application/msword  ： Word文档格式
    application/octet-stream ： 二进制流数据（如文件下载）
    
    application/x-www-form-urlencoded ： 
    
    <form encType="">中默认的encType，
    form表单数据被编码为key/value格式发送到服务器（表单默认的提交数据的格式）。
    服务器收到的raw body会是，name=aaa&key=bbb。
    
    multipart/form-data ： 表单上传文件
    
    ```

??? note "更多Content-Type"

    ```
    .doc
    
    application/msword
    
    .dot
    
    application/msword
    
    .docx
    
    application/vnd.openxmlformats-officedocument.wordprocessingml.document
    
    .dotx
    
    application/vnd.openxmlformats-officedocument.wordprocessingml.template
    
    .docm
    
    application/vnd.ms-word.document.macroEnabled.12
    
    .dotm
    
    application/vnd.ms-word.template.macroEnabled.12
    
    .xls
    
    application/vnd.ms-excel
    
    .xlt
    
    application/vnd.ms-excel
    
    .xla
    
    application/vnd.ms-excel
    
    .xlsx
    
    application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
    
    .xltx
    
    application/vnd.openxmlformats-officedocument.spreadsheetml.template
    
    .xlsm
    
    application/vnd.ms-excel.sheet.macroEnabled.12
    
    .xltm
    
    application/vnd.ms-excel.template.macroEnabled.12
    
    .xlam
    
    application/vnd.ms-excel.addin.macroEnabled.12
    
    .xlsb
    
    application/vnd.ms-excel.sheet.binary.macroEnabled.12
    
    .ppt
    
    application/vnd.ms-powerpoint
    
    .pot
    
    application/vnd.ms-powerpoint
    
    .pps
    
    application/vnd.ms-powerpoint
    
    .ppa
    
    application/vnd.ms-powerpoint
    
    .pptx
    
    application/vnd.openxmlformats-officedocument.presentationml.presentation
    
    .potx
    
    application/vnd.openxmlformats-officedocument.presentationml.template
    
    .ppsx
    
    application/vnd.openxmlformats-officedocument.presentationml.slideshow
    
    .ppam
    
    application/vnd.ms-powerpoint.addin.macroEnabled.12
    
    .pptm
    
    application/vnd.ms-powerpoint.presentation.macroEnabled.12
    
    .potm
    
    application/vnd.ms-powerpoint.template.macroEnabled.12
    
    .ppsm
    
    application/vnd.ms-powerpoint.slideshow.macroEnabled.12
    
    ```



[^1]: CSDN，@way_more，[各种文件对应的ContentType，拿来即用](https://blog.csdn.net/qq_36551991/article/details/109499487)

