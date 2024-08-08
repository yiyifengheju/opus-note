---
title: 🐛 MinIO的Python交互
comments: true
date: 2024.03.03
---

背景：想做一个Python对MinIO存储桶上传下载的脚本

```python
import subprocess

from minio import Minio


def download_package():
    # 创建MinIO客户端对象
    minio_client = Minio(
        "192.168.0.108:9000",
        access_key="uvxxxxx",
        secret_key="4axxxx",
        secure=False  # 如果没有启用SSL，请将其设置为False
    )

    # 指定MinIO存储桶和对象名称
    bucket_name = "xxxx"
    object_name = "xxxx-0.0.1.tar.gz"

    try:
        # 下载文件
        minio_client.fget_object(bucket_name, object_name, object_name)
        return object_name
    except:
        print('error')


def execute_cmd(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.returncode


if __name__ == '__main__':
    package = download_package()
    cmd = f'pip install {package}'
    res = execute_cmd(cmd)
    print(res)
```



