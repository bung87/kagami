# kagami
## Installation
`pip install git+https://github.com/bung87/kagami`
##Kagami是什么?

一个简单粗暴的工具

解决各种软件包管理安装源无法正常访问或者访问慢的问题

##Kagami支持哪些软件包管理工具？

* android sdk manager
* maven
* pypi
* gem
* bundle
* npm

##Kagami如何解决这些问题的？

* android sdk manager：简单粗暴地在hosts文件里增加一行使dl-ssl.google.com解析到国内镜像
* maven：maven配置文件里增加oschina镜像配置
* pypi：pypi配置文件里index-url设置为<https://pypi.tuna.tsinghua.edu.cn/simple>
* gem：使用<https://ruby.taobao.org/>源
* bundle：bundle配置文件里增加<https://ruby.taobao.org/>镜像
* npm:设置别名cnpm 安装源和发布地址均使用淘宝提供的地址

##如何使用？

一次解决android sdk manager,maven的问题  

`kagami forward android maven`

指定bundle配置文件绝对路径或者让程序在当前目录查找或用户目录下查找  

`kagami forward bundle -f /yourbundlelocation/.bundle/config`

指定pypi配置文件绝对路径或者让程序在当前虚拟环境下查找或用户目录下查找  
 
`kagami forward pypi -f /yourpypilocation/pip.conf`

##有问题反馈

在使用中有任何问题，欢迎反馈给我

