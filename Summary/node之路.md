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



