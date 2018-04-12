# 功能FAQ

## 默认配置文件解析？

以MAC brew安装的nginx为例（/usr/local/etc/nginx/nginx.conf），默认配置文件（[链接](http://localhost/mnote/backup/nginx/nginx.conf.default)）如下：

```
worker_processes  1;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    sendfile        on;

    keepalive_timeout  65;

    server {
        listen       8080;
        server_name  localhost;

        location / {
            root   html;
            index  index.html index.htm;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }

    include servers/*;
}
```

mime.types的默认内容：[链接](http://localhost/mnote/backup/nginx/mime.types.default)。

### 参数含义

######  

|参数名称			|参数含义						|
|---------------|---------------------------|
|worker_processes|工作进程数量，默认值：1	|
|worker_connections|单个工作进程能够处理的连接数|
|include		|包含其他配置文件|
|default_type	|文件扩展名到MIME类型的映射|
|sendfile		|系统调用sendfile()的开关|
|keepalive_timeout|与客户端的连接超时时间|
|listen			|服务器监听地址	|
|server_name	|服务器主机名称	|
|root			|请求的根目录|
|index			|定义网站入口文件|
|error_page		|定义错误页面文件|


## 如何配置PHP文件解析？

在server配置里增加如下location配置：

```
location ~ \.php$ {
    root           /Users/muming/Sites/fe/books/Head-First-Ajax/origin/HeadFirstAjax_Ch01_Final;
    fastcgi_pass   127.0.0.1:9000;
    fastcgi_index  index.php;
    fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
    include        fastcgi_params;
}
location / {
    root   /Users/muming/Sites/fe/books/Head-First-Ajax/origin/HeadFirstAjax_Ch01_Final;
    index  index.html index.htm;
}
```

fastcgi_params的默认内容：[链接](http://localhost/mnote/backup/nginx/fastcgi_params.default)。

### 参数含义

######  

|参数名称			|参数含义						|
|---------------|---------------------------|
|fastcgi_pass	|指定FastCGI服务器，对于PHP则是PHP-FPM的域名、IP地址端口或者UNIX套接字|
|fastcgi_index	|PHP处理的默认入口文件|
|fastcgi_param  |传給php-fpm的参数|














