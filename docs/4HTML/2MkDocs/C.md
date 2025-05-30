---
title: 😍 MkDocs部署
comments: true
---

## 壹丨基于Python的Mkdocs部署[^1]（不推荐）

!!! warning "Python部署的HTTP服务器不稳定，多个用户访问会发生阻塞"

```python
import http.server
import socketserver
from http import HTTPStatus
from loguru import logger
import time

PORT = 8848

t_tmp = time.strftime('%Y%m%d%H')
LOG_PATH = f'~/Log/{t_tmp}.txt'

ACCESS_DICT = {}


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def handle_one_request(self):
        if self.client_address[0] in ACCESS_DICT.values():
            logger.info(f'{self.client_address[0]} Accessed!')
            return http.server.SimpleHTTPRequestHandler.handle_one_request(self)
        else:
            logger.warning(f'{self.client_address[0]} Denied!')
            return 'IP Block!!'


if __name__ == '__main__':
    trace = logger.add(LOG_PATH, encoding='utf-8')
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        logger.info(f'Server Running at Port: {PORT}')
        # Get请求
        # logger.info(httpd.get_request())
        httpd.serve_forever()
```



## 贰丨基于Npm搭建简单的Web服务器

!!! warning "较适合本地开发测试。如果要在生产环境中托管项目，建议使用Nginx或Apache等服务器"

安装`http-server`服务器工具

```bash
npm install -g http-server
```

进入项目目录，执行：

```bash
http-server
```

然后在`http://localhost:8000`展示项目

!!! tip "或者使用live-server"

    一个支持热重载的开发服务器，在保存文件时自动重新加载页面
    
    ```bash
    npm install -g live-server
    ```
    
    进入项目目录，执行：
    
    ```bash
    live-server
    ```
    
    然后在`http://localhost:8080`展示项目


## 叁丨基于Apache部署在WSL/Ubuntu

第一步，安装Apache[^2]

```bash
sudo apt update
```

```bash
sudo apt-get install apache2
```

第二步，修改配置文件

```bash
sudo nano /etc/apache2/apache2.conf
```

添加访问权限：

```xml
+ <Directory /mnt/c/Users/USER_NAME/mynote/site/>
+         Options Indexes FollowSymLinks
+         AllowOverride None
+         Require all granted
+ </Directory>
```

!!! tip "添加IP白名单策略[^3][^4]"

    ```bash
    sudo nano /etc/apache2/sites-enabled/000-default.conf
    ```
    
    修改
    
    ```xml
    - DocumentRoot /var/www/html
    + DocumentRoot /mnt/c/Users/USER_NAME/mynote/site
    ```

第三步，启动Apache Web Server

```bash
sudo service apache2 start
```

打开`127.0.0.1`或`192.168.x.x`预览



[^1]: coder.work，[python - 如何从 SimpleHTTPServer 获取客户端 IP](https://www.coder.work/article/1775625)
[^2]: DigitalOcean，[How To Install the Apache Web Server on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-22-04)
[^3]: CSDN，@网络不安全，[Apache访问控制策略](https://blog.csdn.net/qq_44484541/article/details/130098775)
[^4]: 博客园，@不会代码的小强，[apache 站点 只允许某IP 或是某IP段访问](https://www.cnblogs.com/Mr-zhangwenqiang/p/17325025.html)
