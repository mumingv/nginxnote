# 配置示例

## 基于ODP生成的默认配置进行业务配置

### 默认配置

###### 

```
server {
    listen              8080;
    server_name         xxx.baidu.com;
    more_set_headers    'Server: Apache';
    set $php_upstream 'unix:/home/users/yinjie05/baidu/work/dumi-speaker/odp_oss/var/php-cgi.sock';
    #set $php_upstream 'unix:/home/users/yinjie05/baidu/work/dumi-speaker/odp_oss/var/hhvm.sock';

#########域名适配模块配置###############
    dna off;
    dna_adapt_path "/home/users/yinjie05/baidu/work/dumi-speaker/odp_oss/webserver/conf/adaption";
    dna_url_adaption "device";
    dna_cookie_adaption "device";

#########OMP支持#######################
    #设置产品线
    set $product odp;
    #设置子系统
    set $subsys newapp;
    if ($http_x_bd_product) {
        #从接入层获取产品线
        set $product $http_x_bd_product;
    }
    if ($http_x_bd_subsys) {
        #从接入层获取子系统
        set $subsys $http_x_bd_subsys;
    }

#   统一配置全局的rewrite规则请打开如下配置项，并配置当前目录下的rewrite文件
#   include             vhost/rewrite;

    underscores_in_headers on;
    logid_name x_bd_logid;

#   防盗链
    if ($host !~ "^((.*\.)?(baidu\.(com|com\.cn|cn)|91\.com)|localhost|\d{1,3}(\.\d{1,3}){3})(:\d+)?$") {
        return 403;
    }

    location ~* /(\.svn|CVS|Entries){
        deny all;
    }

    location ~* /((.*)\.(.*)\/(.*)\.php){
        deny all;
    }

    location ~* /\.(sql|bak|inc|old)$ {
        deny all;
    }

    location ~ ^/(favicon.ico|static) {
        root            /home/users/yinjie05/baidu/work/dumi-speaker/odp_oss/webroot;
    }

    location ~ \.php$ {
        root            /home/users/yinjie05/baidu/work/dumi-speaker/odp_oss/webroot;
        fastcgi_pass    $php_upstream;
        fastcgi_index   index.php;
        include         fastcgi.conf;
    }

    location / {
        root /home/users/yinjie05/baidu/work/dumi-speaker/odp_oss/webroot;
        index index.php;
        fastcgi_pass    $php_upstream;
        include         fastcgi.conf;
        rewrite ^/([^/.]*)(/[^\?]*)?((\?.*)?)$ /$1/index.php$2$3 break;
    }
}
```


### 运营前端资源转发配置

###### 

```
    location ~ /oss/index.html {
        root            /home/users/yinjie05/baidu/work/dumi-speaker/odp_oss/html;
    }

    location = / {
        rewrite ^(.*)$ /oss/index.html;
    }

    location ~ \.(js|css|gif|jpeg|png|woff|woff2|ttf) {
        root            /home/users/yinjie05/baidu/work/dumi-speaker/odp_oss/static/oss;
    }
```


### 支持rest风格

```
    location / {
        root /home/users/yinjie05/baidu/work/dumi-speaker/odp_oss/webroot;
        index index.php;
        fastcgi_pass    $php_upstream;
        include         fastcgi.conf;
        rewrite ^(/[^\?]*)?((\?.*)?)$ /oss/index.php/main$1$2 break;
    }
```










