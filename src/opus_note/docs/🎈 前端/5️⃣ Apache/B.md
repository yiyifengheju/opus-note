---
title: 🎄 使用Apache2使用多个端口添加网站
comments: true
---

第一步，修改端口配置文件

```bash title="/etc/apache2/ports.conf"
Listen 80
Listen 8888
```

第二步，更新虚拟主机文件，为每个端口更新虚拟主机配置

```bash title="/etc/apache2/sites-enabled/000-default.conf"
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /path/to/site

        <Directory /path/to/site/>
        Allow from ip1 ip2
        Deny from all
        </Directory>
        ErrorLog ${APACHE_LOG_DIR}/error_80.log
        CustomLog ${APACHE_LOG_DIR}/access_80.log combined
</VirtualHost>

<VirtualHost *:8888>
        ServerAdmin webmaster@localhost
        DocumentRoot /path/to/site

        <Directory /path/to/site/>
        Allow from ip1 ip2
        Deny from all
        </Directory>
        ErrorLog ${APACHE_LOG_DIR}/error_8888.log
        CustomLog ${APACHE_LOG_DIR}/access_8888.log combined
</VirtualHost>
```

第三步，添加文件夹权限

```bash title="/etc/apache2/apache2.conf"
<Directory /path/to/site1/>
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
</Directory>
<Directory /path/to/site2/>
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
</Directory>
```

第四步，重新运行Apache服务

```bash
sudo service apache2 restart
```