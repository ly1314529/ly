## docker 
不知道什么时候就发展起来的一个容器，他有什么作用呢？纯粹是为了节省空间，运行速度快，部署项目只需一个命令搞定，迁移方便快捷，一个镜像里面可以有多个容器，
他们之间独立运作，相互不影响


* 如果你的电脑有一个hyper-v,就可以直接在下面新建一个centos
* uname -r   //Docker 要求 CentOS 系统的内核版本高于 3.10,使用该命令可以查看当前内核版本
* sudo yum install -y yum-utils \

  device-mapper-persistent-data \

  lvm2

