大学时期学过sql server,那nosql,又是什么东东

维基百科上如是说：不同于传统的关系数据库的数据库管理系统的统称。其中最重要的是NoSQL不使用SQL作为查询语言。其数据存储可以不需要固定的表格模式

在这个时候，mongoDB作为一个nosql数据库就华丽丽的现身了，他是一个开源的数据库，反应更加的敏捷，增加了数据库的可靠性，灵活性

-----

* 下载mongoDB，[官网](https://www.mongodb.com/cn)
* 选择自定义安装
```
cd /f
mkdir mongodb && cd mongodb  //mongodb就安装在这个文件夹下
mkdir data && cd data
mkdir db  
```
* 打开cmd
```
cd /f/mongodb/bin
mongod.exe --dbpath f:\mongodb\data\db  //此时在打开另一个终端
```
```
cd /f/mongodb/bin
mongo
```

* 编辑语言
```
show dbs //展示表
use test //select the db called test
show collections //展示集合
db.cats.find()   //查询cats集合下的所有数据
db.cats.remove({"age":2})  //删除cats集合下的age:2的所有数据
```
* 如何连接数据库
 * 安装依赖
```
npm install -g mongoose 
```
  * 源码
```
vi app.js
```
```javascript
var mongoose=require('mongoose'); //调用包
mongoose.connect('mongodb://localhost/test'); //连接一个叫test的表，不用担心没有，因为mongodb会自己创建一个test的表
var People=mongoose.model('People', {
name:String,
job:String,
age:Number
});  //创建一个表 的各项标签，包括姓名，工作，年龄
var one=new People({name:"ly",age:18,job:"tester"});  //创建一个实例，并且加入相应的数据
one.save(function (err) {
 if (err) 
 console.log('err');   //将这个数据储存在表中
 
 });
 ```
 * 运行
  
  在mongodb启动的情况下
  ```
  node app.js
  ```
你将会看到你所创建的数据库test




