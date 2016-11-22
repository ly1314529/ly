# cucumber自动化测试
## 安装vagrant搭建一个Linux开发环境：

  * VirtualBox安装,[下载地址](https://www.virtualbox.org/wiki/Downloads)
  * Vagrant安装[下载地址](https://www.vagrantup.com/downloads.html)
  * 安装git,[官网](https://git-scm.com/download/)
  

## 安装好git后打开git bash,环境下输入命令

    $ mkdir ubuntu14.04
    $ cd ubuntu14.04
    $ vagrant init ubuntu/trusty64(ubuntu指的是虚拟机的名字，可以自行设置，trusty64是vagrant所需要的box,输入这个就可以在虚拟机上自行安装)

## linux上映射到windows的设置
 * 打开ubuntu下的自动生成的vagrantfile文件，修改
 *  config.vm.synced_folder "../data", "/vagrant_data" （去掉前面的#号，然后在windows下建立data文件，data也可以自定义改名，vagrantfile中也要改变data）


## 关于在Linux终端运行cucumber的步骤

       $ vagrant up 
       $vagrant ssh
      
## 安装java

    $ sudo apt-add-repository ppa:webupd8team/java
    $ sudo apt-get update
    $ sudo apt-get install oracle-java7-installer
    $ export JAVA_HOME=/usr/lib/jvm/java-7-oracle # append to your ~/.profile file
## 安装nodejs

    $ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.25.2/install.sh | bash //首先装个nodejs版本管理器，方便管理
    $ nvm #nodejs版本管理器 看是否有输出，有就安装成功了
    $ nvm install 0.12 #可去官网查看最新版本 
  

## cucumber运行起来需要打开三个终端
* 第一个终端是运行终端
* 第二个是服务器终端
* 第三个是本地服务器终端

### 首先是npm的安装，npm是包管理器，nvm是版本管理器

    $ sudo apt-get install -g npm(安装npm)
    $ npm use 0.12(调出npm使用)
    $ nvm alias default 0.12(npm 全局设定，下次可以直接使用npm)

### 还需要安装cucumber

    $ sudo apt-get install cucumber(cucumber的安装命令)

### 在首次执行运行时，需要安装依赖库

    $ npm install(方便运行时调用依赖库)

### 第一个终端需要进入到测试文件目录下

     $ ./test/run.js
    
 如果是运行git上面的文件，需要git clone “url地址”
### 第二个终端需要安装浏览器

    $ npm install -g phantomjs(安装时需要进入测试目录下，在安装完成后需要将浏览器改成phantomjs)
### 然后运行服务器终端

    $ npm run-script local-webserver
    
### 运行第三个终端

    $ xvfb-run --server-args="-screen 0, 1366x768x24" selenium-standalone start，在以后使用的时候可以输入：selenium-standalone start
  第一个终端是最后运行的
  
##然后等待终端跑起来吧！


### 关于linux的映射问题
就是说使ubuntu下的文件内容在windows上也可以看见，需要在ubuntu的文件下的vgrantfile改了，#config.vm.synced_folder "d:/ubuntu14.04/data", "/vagrant_data"注释掉#(是在开启ubuntu下的时候再注释掉)

