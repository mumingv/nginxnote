# 精通Nginx（第一版）

## 安装Nginx及第三方模块


## 配置指南

### 基本配置格式


### Nginx的全局配置参数


### 使用include文件


### Http的server部分


### 虚拟server部分


### Locations - where、when、how

**location修饰符**

|修饰符			|处理方式									|
|---------------|---------------------------------------|
|= 				|使用精确匹配，并且终止搜索|
|~				|使用正则表达式匹配，区分大小写|
|~* 			|使用正则表达式匹配，不区分大小写|
|^~				|优先于正则表达式的匹配；如果匹配了该location，则不会再进行其他正则表达式形式的匹配。|

**location匹配顺序**

1. 将所有的location配置分为两组：非正则表达式匹配、正则表达式匹配。
2. 第一组，非正则表达式匹配：优先进行`=`和`^~`匹配，如果匹配上了，则不再进行其他正则表达式location的匹配。
3. 第二组，正则表达式匹配：按正则表达式配置的顺序进行匹配，首次匹配成功则结束。
4. 兜底匹配，没有指定修饰符的场景：`location / {}`。


### mail的server部分


### 完整的样本配置文件


## 使用mail模块

略。


## Nginx作为反向代理


## 反向代理高级话题


## Nginx Http服务器


## Nginx的开发


## 故障排除技巧

