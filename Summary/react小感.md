react是一个前端框架，通过使用这个框架，真正实现了浏览器和手机可以只需要改一次ui，就可以使用，而且react速度快捷，有着可重复使用的文件，最早是由facebook发展出来的

-----
* JSX语法,是js语法的一个延伸
 
指直接将js代码写入html页面
```
var h1=<h1>hello</h1>
var div=(
<div>
<h1>ly</h1>
</div>
);
```

```
var React = require('react');
var ReactDOM = require('react-dom');

//ReactDOM是一个js库，里面包含了一些react方法
//render创建了一个dom节点树，使jsx呈现在我们面前
//<h1>1+2</h1> 代表输出1+2,执行html语句
//<h1>{1+2}</h1> 执行js语句，输出为3
ReactDOM.render(<h1>Hello world</h1>, document.getElementById('app'));
```

```
if (coinToss() == 'heads') {  //if..else 语句
  var img = <img src={pics.kitty} />;
} else {
  var img = <img src={pics.doggy} />;
}

ReactDOM.render(
  img,  //执行的行为
  document.getElementById('app')
);
