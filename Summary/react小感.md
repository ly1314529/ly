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
```
* 组件
   * 一个视图的创建
```
var Button=React.createClass({  //创建组件
render: function () {  //render可以把他看成一个类，这里面可以增加很多个类，比如增加一个name:'ly';
return something; //函数返回的东西
}
});
Reactdom.render(
<Button />,  //调用的就是button这个创建的组件
document.getElementById('id'); //全文的id监听
); //现在是调用这个类，render
```
   * 在两个文件下共同完成一个视图
```
var React = require('react');
var ReactDOM = require('react-dom'); //导入文件
var NavBar=require('./NavBar');  //导入NavBar这个文件

var ProfilePage = React.createClass({  //创建一个叫ProfilePage这个组件
  render: function () {  //函数
    return (
      <div>
       <NavBar /> //从一个文件调到这里来的navbar
        <h1>All About Me!</h1>
        <p>I like movies and blah blah blah blah blah</p>
        <img src="https://s3.amazonaws.com/codecademy-content/courses/React/react_photo-monkeyselfie.jpg" />
      </div>
    );   //返回的是html的内容
  }
});
ReactDOM.render(  //打开接口
<ProfilePage />,  //调用这个组件
  document.getElementById('app')
);


var React = require('react'); //导入重要文件

var NavBar = React.createClass({  //创建navbar这个组件
  render: function () {  //组件将要展示的内容
    var pages = ['home', 'blog', 'pics', 'bio', 'art', 'shop', 'about', 'contact'];
    var navLinks = pages.map(function(page){  //map是遍历整个pages的内容
      return (
        <a href={'/' + page}>
          {page}
        </a>
      );
    });

    return <nav>{navLinks}</nav>;{}里面的是执行这个语句
  }
});
module.exports=NavBar; //代表如果require了,你将从navbar里得到什么，相当于打开接口，和node一样，需要require时候，都要先打开接口
```
   * 向组件传递信息
    * this.props //指的当前属性,传递的也是属性
    * 而函数需要用this.talk传递，如talk :function () {},(在同一个文件下的函数用this.talk，不同文件下用this.props.talk)

```
var React = require('react');
var ReactDOM = require('react-dom');

var Greeting = React.createClass({
  render: function () {
    return <h1>Hi there, {this.props.firstName}!</h1>; //this.props.属性
  }
});

// ReactDOM.render goes here:
ReactDOM.render(
  <Greeting firstName='ly' />, //返回的属性
  document.getElementById('app')
);
```
   * this.props.children，将会返回jsx里的所有标签
   * this.state.属性 
```
var React = require('react');
var ReactDOM = require('react-dom');

var green = '#39D1B4';
var yellow = '#FFD712';

var Toggle = React.createClass({
  getInitialState: function () {
    return { color: green }; color是内置的属性，所以用state
  },
  
  changeColor: function () {
    var color = this.state.color == green ? yellow : green;
    this.setState({ color: color });  //立即调用这个设置，这样将会陷入x无限loop
  },
  
  render: function () {
    return (
      <div style={{background: this.state.color}}> 
        <h1>
          Change my color
        </h1>
        <button onClick={this.changeColor}>
          Change color
        </button>
      </div>
    );
  }
});

ReactDOM.render(
  <Toggle />,
  document.getElementById('app')
);
```


