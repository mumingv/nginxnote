# 环境FAQ

## Nginx日志显示收到请求，但是PHP没有业务处理日志也没有错误日志。如何排查？

**问题描述**

Nginx收到的请求日志如下：

```
172.24.185.249 - - [12/Apr/2018:16:24:39 +0800] "GET /oss/device_type HTTP/1.1" 200 31 "-" "ENRICHUID=M19nd2Vqb2pybzMyNXBvcmdwd3A%3D; 
```

**问题原因**

location中没有指定SCRIPT_FILENAME参数。

```
location ~ ^/oss/ {
	...
	fastcgi_param  SCRIPT_FILENAME    $document_root$fastcgi_script_name;
	...
}
```

**排查方法**

需要确定是否走到了预期的分支。

1.增加对应不同的日志格式

```
http {

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" "$http_cookie" "$http_user_agent" '
                      '$request_time $logid $remote_addr $server_addr $upstream_addr $host '
                      '"$http_x_forwarded_for" $product $subsys $tracecode $msec';

    log_format  hit  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" "$http_cookie" "$http_user_agent" '
                      '$request_time $logid $remote_addr $server_addr $upstream_addr $host '
                      '"$http_x_forwarded_for" $product $subsys $tracecode';

    log_format  other  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" "$http_cookie" "$http_user_agent" '
                      '$request_time $logid $remote_addr $server_addr $upstream_addr $host '
                      '"$http_x_forwarded_for" $product $subsys';
}
```

2.在不同的分支中打印日志

```
   location ^~ /oss/ {
        access_log  "/home/users/yinjie05/baidu/work/dumi-speaker/odp_oss/log/webserver/access_log"  hit;
        access_log  "/home/users/yinjie05/baidu/work/dumi-speaker/odp_oss/log/webserver/access_log"  main;
        root /home/users/yinjie05/baidu/work/dumi-speaker/odp_oss/webroot;
        index index.php;
        fastcgi_pass    $php_upstream;
        include         fastcgi_params;
        rewrite ^/([^/.]*)(/[^\?]*)?((\?.*)?)$ /$1/index.php$2$3 break;
    }
    location / {
        access_log  "/home/users/yinjie05/baidu/work/dumi-speaker/odp_oss/log/webserver/access_log"  other;
        access_log  "/home/users/yinjie05/baidu/work/dumi-speaker/odp_oss/log/webserver/access_log"  main;
        root /home/users/yinjie05/baidu/work/dumi-speaker/odp_oss/webroot;
        index index.php;
        fastcgi_pass    $php_upstream;
        include         fastcgi.conf;
        #rewrite ^/([^/.]*)(/[^\?]*)?((\?.*)?)$ /$1/index.php$2$3 break;
        rewrite ^(/[^\?]*)?((\?.*)?)$ /oss/index.php/main$1$2 break;
    }
```

3.发送请求并通过日志格式来判定是否走到了相应的分支。

