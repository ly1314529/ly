第一次接触express，就了解到是一个关于node.js的框架，深受大众喜爱

以前老是把http和express混合想到一起，后来才知道http只是一个模块

而express是一个框架，需要var app=express();

对！就是如此

------


* 创建一个文件夹
```
mkdir express-test && cd express-test
```

* 安装express框架，(我习惯全局安装)
```
npm install -g express  //这个时候在目录下会看到一个node_modules文件夹
```

* 创建app.js
```
vi app.js
```
```javascript
var express=require('express'); //引用框架
var app=express(); //生成函数，方便调用
app.get('/',function (req,res) {   //get是从服务器获取数据，后面接url地址
//req是request，指的获取到的http的头或者body，就是得到的一些数据
//res是response，指的是在得到‘/’这个地址后，服务器将要发送给浏览器的字符串

  res.send('hello');  //send发送
  });
app.get('/about',function (req,res) {   //‘/about’指的是另一个路由地址
   res.send('about us');
   });
app.listen(8000,function (req,res) {  //监听端口8000
    console.log('the port is 8000');  //在监听成功发送的信息
    });
```
