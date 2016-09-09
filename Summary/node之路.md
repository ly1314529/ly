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

* 

