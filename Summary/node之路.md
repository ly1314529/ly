node.js是一个非常强大的语言库,他基于js,有属于他自己的npm和nvm,可以用于后台

* node的使用
[api手册](http://wiki.jikexueyuan.com/project/nodejs/)

* 从创建一个json文件开始
```
npm init //初始化包，然后按照提示一步步填写
ls //将会看到一个json文件
```
1.需要安装依赖库，在json文件中添加
```
"dependencies": {
    "express": "^4.14.0",
    "utility": "^1.8.0"
  }
```
2.直接在命令行里输入 npm install express --save,save的作用是将这个依赖库也添加到json文件中

* 创建一个简单应用
```
vi app.js
```
```javascript
var express=require('express'); //use the express frame 
var app=express(); //create a instance for express
//这是app调用的是get的方法，为‘/’这个路径指定了一个handler函数
//req,res分别代表request(请求)和response(回应)，这个也是函数所接受的参数
//req代表的是返回的数据，包括body,query这些
//res代表的是需要浏览器所输出的东西，send这个方法代表向浏览器输出这个字符串
app.get('/',function (req,res) { 
res.send('hello');
});
app.listen(3000,function (req,res) { //listen the 3000 port，第二个函数是回调函数
console.log('app port is 3000'); //在监听成功后，会输出的东西
}); 
```
* 更多的东西

在看参考资料是，发现了一个叫utility的包，是一个有用的工具集合，主要是依靠md5这个命令生成一些编码，保证数据的安全性


* 网络爬虫
  * 第一次接触这个词是在9个月前了，当时很疑惑，请教了别人，但别人也没讲董，事后也没有再认真研究，最近学node.js又遇到了，还是想逃避，足足一周没有去搞node，但今天又提起了，还是探索一番吧
  * 网络爬虫指的就是以一定的规律抓取某一网页上的数据
  * 在抓取页面的时候，需要用到
    * [superagent](https://cnodejs.org/topic/5378720ed6e2d16149fa16bd)
      * 一个非常方便的客户端请求代理模块，可以处理get,post,put,delete,head 
    * [cheerio](https://cnodejs.org/topic/5203a71844e76d216a727d2e)
      * 一个类似于jquery的api，将html告诉服务器，res是服务器将要返回的内容
  * 源码
    ```javascript
    var express=require('express');
    var superagent=require('superagent');
    var cheerio=require('cheerio');  //依赖库调用
    var app=express(); //创建express函数，方便调用express方法
    app.get('/',function (req,res,file) {  //file是获取的内容
    superagent.get('url');  //在url网页上抓取html
    .end(function (err,sres) {   //sres是获取到的html
    if (err) {   //报错的情况
    return file(err) 
     }
    var $=cheerio.load(sres.text);  // sres.text 里面存储着网页的 html 内容，将它传给 cheerio.load 之后
      //就可以得到一个实现了 jquery 接口的变量
    var items=[];  //创建一个数组
    $('需要查找的id,class').each(function (idx,element) {  //遍历id or class的元素
    var $element=$(element);   //得到html中的元素
    items.push({json格式}   //res将要展现的json, title : $element('href');
    ); 
    });
    });
    res.send(items);  //服务器响应将items发送到浏览器
    });
    });
    app.end(3000,function (res,req) {
    console.log('the port is 3000'); //监听端口3000
    });
    
    
    })
    ```

* 回调函数（callback)

说到回调函数，第一个想到的就是callback，指的是函数1作为参数在函数2中被调用，在函数2执行完之后，才去执行函数1，最近看了一本关于node.js入门的书（由于本人太菜，只能看入门），是一位伟大的计算机家所著，于是想起了前1个月的jquery,想想还是漫游道理的

jquery的样式如下：
```javascript
$('p').hide('slow',function () {
 alert('hide');  //这个function就是回调函数
});
```

* node闲话
 * 看了node入门那么久了，我琢磨了一些小经验
     * 一来就要找一个包，依赖他，或者找个框架也可以，大致形式是 var fs=require('fs');
     * 调用这个方法，在fs这个官网上查找这个包都有什么方法，什么get啊，on 啊，都用起来
     * 如果不出意外，可以增加一个err，如果请求错误，返回响应的错误回应，可以用console.log
 * 关于http的头
     * 以前就一直好奇，为嘛要在http返回时加上一个writeHead,而且界面也并没有返回，现在知道了，原来那是http的头部文件，在浏览器上不会显示
     * 于是在google的扩展程序上安装了http headers就可以看到你所发送的信息了
     * 关于http的使用结构
        * 调用http就不说了
        * 创建web服务器，createServer
        * 最后一个end()
        * 然后监听服务器的端口号

* 同步和异步，阻塞和非阻塞
  *  同步和阻塞概念差不多，指的是前一个函数没有执行完成，后面的函数就无法执行，在后面等待，一个一个的执行
  *  异步和非阻塞也是同一个意思，指的是在第一个函数没有执行前，后面的函数也可以执行，不必等待，这也是node的一个亮点
  *  代码理解
  
  ```javascript
  var fs=require('fs');  //读取系统文件
  var data=fs.readFileSync('ly.txt');  //读取完毕之后才能打印
  console.log('sync'+data.toString());
  
  fs.readFile('ly.txt',function (err,data) {
  if (err) throw err;
  console.log('async'+data.toString());
  })
   
