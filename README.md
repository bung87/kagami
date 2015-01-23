# kagami

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
* pypi：pypi配置文件里index-url设置为<http://pypi.douban.com/simple/>
* gem：使用<https://ruby.taobao.org/>源
* bundle：bundle配置文件里增加<https://ruby.taobao.org/>镜像
* npm:设置别名cnpm 安装源和发布地址均使用淘宝提供的地址

##有问题反馈
在使用中有任何问题，欢迎反馈给我

