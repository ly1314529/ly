## docker 
不知道什么时候就发展起来的一个容器，他有什么作用呢？纯粹是为了节省空间，运行速度快，部署项目只需一个命令搞定，迁移方便快捷，一个镜像里面可以有多个容器，
他们之间独立运作，相互不影响


* 如果你的电脑有一个hyper-v,就可以直接在下面新建一个centos
* uname -r   //Docker 要求 CentOS 系统的内核版本高于 3.10,使用该命令可以查看当前内核版本
* sudo yum install docker   //sudo 是为了不是root用户提供的权限，

* docker search nginx   //查看nginx的版本号（hub.docker.com）
* docker pull nginx：    //适合你自己的版本号，从docker上面拉取下来，
* docker images         //查看已有的镜像
* docker create --name  nginx01  -p 3094:9094  -v ~/nginx/www:/usr/share/nginx/html \
-v ~/nginx/conf/nginx.conf:/etc/nginx/nginx.conf \
-v ~/nginx/logs:/var/log/nginx nginx
 
 //创建nginx容器名字是nginx01，从宿主机映射到容器目录，映射本机的3094端口到docker的9094端口
 
 
 * 
 
 
  

