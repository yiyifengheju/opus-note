---
title: A 搭建HTTP服务
comments: true
---

性能显然不如使用Apache、Nginx等方式，多个用户访问会发生阻塞


```python
import http.server
import socketserver
from http import HTTPStatus
from loguru import logger
import time

PORT = 8848

t_tmp = time.strftime('%Y%m%d%H')
LOG_PATH = f'~/Projects/notebook_log/{t_tmp}.txt'

ACCESS_LIST = ['192.168.1.102', '192.168.1.105']


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def handle_one_request(self):
        if self.client_address[0] in ACCESS_LIST:
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

上述使用`ACCESS_LIST`限制访问的IP地址
