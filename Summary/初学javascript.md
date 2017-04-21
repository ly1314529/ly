#### 现在才知道人真的是在不断的学习，以为高中轰轰烈烈的读完了，结果还有大学，大学要是没有学好，工作都找不到，有些事，真的很现实，比如你上班，没有掌握最近技术依然会被淘汰，人总是要去不断进步的，借用星爷的一句话：努力！奋斗！
--------

##### javascript是一种类似面向对象编程的语言（OOP）,从最简单的了解
 * js基本数据类型 
``` 
Undefined(未定义)、Null、Boolean(布尔)、Number（数值）、String（字符串）
```
 
 * 函数：这是一个可以被用来反复调用的方法,函数最重要的一定就是体内有个return返回值
 
 ```javascript
 
 function 函数名(参数，注意参数书写规范) { 源代码}
 ```
     
函数中的参数有形参和实参之分，形参是没有赋值的变量，并不占有空间，实参又是变量，拥有确定的值，形参接受的是实参的值
   * 函数的声明和赋值
   
   ```javascript
   function check() { if(!foo) { var foo=2; }
   return foo; } 
   check();//2
   ```
   
   这个时候思考！foo什么意思，foo代表是赋了值的，而！foo代表的是没有赋值的（foo=0也算没有赋值），只有在！foo没有赋值才会执行,
   foo之前没有出现过函数中，怎么没有报未定义的错?
   
   然后了解一下js编译器的运行机制，原来js是先声明后赋值的，在进入函数的时候就相当于var foo; if(!foo);
   所以最后会执行这个步骤，打印出2
   
   * 最近看到几段对函数声明和变量解析很透彻的代码
   
   ```javascript
    function foo() { 
     function bar() { 
      return 3; 
      } 
      return bar(); 
     function bar() { 
      return 8;
     } 
    } 
    foo();//8,函数声明的时候第二个function是被提到return bar()前面了，临近原则，返回的是8
```

```javascript
  function foo() { 
   var bar=function() { 
    return 3; 
    }; 
    return bar(); 
    var bar=function() { 
    return 8; 
    }; 
   } 
   foo();//3,函数表达式在声明的时候，首先声明的是变量，var bar =undefined;var bar=undefined; bar =function() {return 3;}
  
  ```

```javascript
foo();
function foo() {
var bar=function() {
return 3; 
}; 
return bar(); 
var bar=function() { 
return 8; 
}; 
 } //3,第3个和第二个函数是一样的，只是会先解析函数foo,在返回值
```

```javascript
function foo() { 
return bar(); 
var bar=function() { 
return 3; 
}; 
var bar=function() { 
 return 8; 
 }; 
  } 
foo()//VM246:1 Uncaught TypeError: bar is not a function，这个return bar()提前了，var bar=undefined; var bar=undefined; return bar();
```
------

   ```javascript
   function check() { if(foo) { var foo=2; }
   return foo; } 
   check();//undefined,代表foo已经被声明了，但是并没有赋值，所以不会执行这个函数
   ```

##### 对象：对象其实就是一个属性的集合，方法只是属性的值以函数的形式
  
   * 方法:这是相当于一个隐式函数，隐藏的就是对象，在源代码中是用this来调用，this指向的是当前函数体的对象
  
 ```javascript
 function myfunction(对象被隐藏，name) { this.name }
 ```
   * 创建对象有三种1.工厂模式，2.构造函数3.原型
  
  ```javascript
  function factory(name) {//工厂模式
  var o=new Object();
  o.name=name;
  o.say=function () {
  alert(this.name);}
  return o;
  }
  function Create(name) { //构造函数首字母大写
  this.name=name;
  this.say=function () {
  alert(this.name);
  }; 
  }
  function proto(name) {  //原型模式
  proto.prototype.name=name;
  proto.prototype.say=function () {
  alert(this.name); }
  }
  var person=new proto('ly');
  person.say();
  ```

   * 类型
    
    * 原始值: 相当于传值string，number，boolean，null，undefined
 
 ```javascript
var foo = 1,
    bar = foo;

bar = 9;

console.log(foo, bar); // => 1, 9只是传值
```
   * 复杂类型: 相当于传引用 object，array， function

```javascript
var foo = [1, 2],
    bar = foo;

bar[0] = 9;

console.log(foo[0], bar[0]); // => 9, 9,foo也发生了变化
```
   * 属性检测
         * 对象属性的检测
    
    ```javascript
function hasProperty(aObj,aProperty) {
return aObj.hasOwnProperty(aProperty)
}
var obj={age:10};
hasProperty(obj,'age');//用in也可以检测
```

    
   * 对象自身属性的检测
    
    ```javascript
    function hasProperty(aObj,aProperty) {
    return aObj.hasOwnProperty(aProperty); }
    function obj() {this.a=1};
   obj.prototype.b=2;
   var test=new obj();//一定要创建实例，不然无法正确的检测属性
   hasProperty(test,'a');//true
   hasProperty(test,'b');//false,不是自身的属性，是原型上的
 ```
 

 
  
#####  _proto_ JavaScript在创建对象的时候，都会有一个proto的内置属性，用于指向创建它的函数对象的prototype。原型对象也有proto属性。因此在不断的指向中，形成了原型链。o._proto_->Object._proto_->null
   *  constructor 原型对象prototype上都有个预定义的constructor属性，用来引用它的函数对象。这是一种循环引用。
   * ![原型链](https://segmentfault.com/img/bVwFw5)
   
  
   * 构造函数模式 所谓"构造函数"，其实就是一个普通函数，但是内部使用了this变量。对构造函数使用new运算符，就能生成实例，并且this变量会绑定在实例对象上。
   * 实例对象，在创建实例对象后，实例对象会有一个constructor属性，指向他们的构造函数
   * 每一个构造函数都有一个prototype属性，指向另一个对象。这个对象的所有属性和方法，都会被构造函数的实例继承
   * 每个对象都有prototype原型属性，实例对象的_proto_是指向对象的prototype属性的，原型链最终都会指向Object.prototype->null

##### javascript包含六个基本的数据类型：String, Number, Boolean, Undefined, Null, Object
   * 局部变量和全局变量的区别
   * 全局变量是存在于整个页面的,在该页面的各个地方都可以被调用，而局部变量是存在某个函数中的,只能在这个函数体中被调用
   * var的使用，如果在函数体中，没有使用var就成了全局变量，否则就是局部变量
   * 有一段代码，可以加深理解
  
  ```javascript
  function variable() {
  var a=b=1; } =>var a,b=1;a是局部变量，b是全局变量，为避免不必要的错误，可以改成：var a,b; a=b=1;
  ```

##### js检测数据类型
   * typeof 基本数据类型type都能返回适当的类型字符串,但是对象类型的她就没戏了
  
  ```javascript
   typeof "jerry"; // "string"
    typeof 12;  // "number"
    typeof true;    // "boolean"
    typeof undefined;   // "undefined"
    typeof null;    // "object"
    typeof {name: "jerry"}; // "object"
    typeof function(){};  //function
   ```
   typeof可以判断除null之外的数据类型，null返回的是object，function返回的是function
   //最近在网上取经，发现有个东西可以通过对象的原型来检测属性的类型，比typeof好太多
   
   ```javascript
   var s=null;
   Object.prototype.toString.call(s);//检测出null。而typeof返回的是对象
   ```
   
   * .constructor,可以检查一个对象的类型
   
```javascript
[].constructor

function method(name) { this.name=name;} new method("ly").constructor===method; //true

function obj(name) { this.name=name;} new obj("ly").constructor===obj; //true
```

   * hasOwnproperty,可以检测对象的自身属性，但不能检测继承属性，继承的属性用in可以检测
   
   ```javascript
   obj.hasOwnProperty(name); name in obj
   ```
   
   * Object.getOwnPropertyNames(),返回的是可枚举和不可枚举的属性数组，原型链上的属性就无法检测
   * for...in返回可枚举的属性，原型链上的属性也能检测
   * Object.keys()返回的是可枚举的属性数组，无法检测原型链上的属性
 
##### 使用的方法  
   * call()方法在使用一个指定的this值和若干个指定的参数值的前提下调用某个函数或方法.还有继承和多重继承
   其实在js中只有函数，而方法只不过是在函数的内部代码使用了this的函数,调用的是call前面的方法，接的是字符串

   ```javascript
   function hasproperty(property) { 
   return (this.hasOwnProperty(property)); 
   } 
   var obj={age:20}; 
   hasproperty.call(obj,"age");//call(需要调用方法的对象名，属性)
   ```
   
   * apply()方法和call一样，但是接受的是数组
  
   ```javascript
function hasproperty(property) { 
return (this.hasOwnProperty(property)); 
} 
var obj={age:20}; 
hasproperty.apply(obj,['age']);
```
##### 数组
   * 操作符，所谓的方法都离不开对象
         * 栈方法,有pop()和push()方法，push是推进去，pop是取出来，最后进去的先出来，后进先出
  
```javascript
 var o=['a'];
 o.push('ly');//['a','ly']
 o.pop();//['a']
 ```
 
    * 队列方法,shift()也是取出，是先进来的先出去，先进先出
 
 ```javascript
 var o=['ly','a'];
 o.shift(); //['a']
 ```
 
   * concat()是一个能够讲两个或多个数组链接起来的操作符
 
 ```javascript
 var o=['a','b']
 o.concat('c');//['a','b','c']
 ```

   * slice()是一个能复制数组区间的数，被操作的数组不变

 ```javascript
 var o=['a','b','c'];
 var a=o.slice(0,1);//['a']复制0，1区间的数，但是o数组的值不会变
 ```
 
   * splice()是一个可以删除数组中的某个数,被操作的数组会发生变化
 ```javascript
 var o=['a','b','c'];
 var p=o.splice(0,1,'s');///['s','b','c']从第0项开始删除一项后又增加一个‘s'，o的值发生变化，p数组就是删掉的‘a'
 ```
 

#### 迭代：指的是按照某种顺序逐个访问列表中的每一项。比如，for语句。
 
   * filter():对数组中的每一项运行给定函数。返回该函数会返回 true 的项组成的数组。过滤的作用
 
```javascript
var x=[2,3,4];
x.filter(function(item) {
  return (item>2); }//在执行完每一项后，返回true的数[3,4]
)
```

   * forEach():对数组中每一项运行给定函数。该函数没有返回值。
 
```javascript
var x=[2,3,4];
x.forEach(function (item) {
return (item>2); }//执行每一项之后，没有返回值
)
```
    * map():对数组中每一项运行给定函数。返回每次函数调用的结果组成的函数。
 
```javascript
var x=[2,3,4];
x.map(function (item) {
 return (item*2); }//[4,6,8]每一项都进行了运算，返回运算的值
)
```

   * some():对数组中每一项运行给定函数。如果函数对 任一项返回 true，则返回 true
 
```javascript
var x=[2,3,4];
x.some=(function (item) {
return (item>2);  }//true,只要有一个值是对的，就返回true
)
x.every(function (item) {
return (item>2); }//false,只要有一个值是错的，就返回false
)
```

##### 遍历： 指的是按照一定的规则访问树形结构中的每个节点，而且每个节点都只访问一次

   * Object.getOwnPropertyNames() 该方法返回一个由指定对象的所有自身属性的属性名（包括不可枚举属性）组成的数组，不能检测原型链上的属性

```javascript
var arr=[1,2,3]; Object.getOwnPropertyNames(arr)//["0", "1", "2", "length"]
var obj={0:'a',1:'b'}; Object.getOwnPropertyNames(obj)//["0", "1"]

Object.getOwnPropertyNames(obj).forEach(function (i) { console.log(i+obj[i]); })
//0a
//1b,将属性和值全部列出来
var obj={}; Object.defineProperty(obj,"a",{enumerable:false,value:"ly" } );   Object.getOwnPropertyNames(obj)
//["a"]将不可枚举的属性也能列出来
function B() {this.b=2;}; B.prototype.a=1; var test=new B(); Object.getOwnPropertyNames(test)
//["b"]原型链上的属性就无法检测出来
```

   * for ...in 以任意序迭代一个对象的可枚举属性和原型链上的属性，每个不同的属性，语句都会被执行一次

```javascript
var obj={a:1,b:2,c:3}; for(var i in obj) { console.log(i); }//a,b,c

var obj={}; Object.defineProperty(obj,"a",{enumerable:false,value:"ly" } ); for(var i in obj) { console.log(i); }
//undefined,因为for  in无法检测不可枚举属性

function B() {this.b=2;}; B.prototype.a=1; var test=new B();  for(var i in test) {console.log(i); } //b a，原型链上的也能遍历
```

   * Object.keys() 方法会返回一个由给定对象的所有可枚举自身属性的属性名组成的数组，而且不能检测原型链上的属性

```javascript
var obj=["a","b"]; Object.keys(obj)//["0", "1"]数组形式

var obj={0:1,1:2}; Object.keys(obj)//["0", "1"]

var obj={}; Object.defineProperty(obj,"a",{enumerable:false,value:"ly" } );  Object.keys(obj)
//[]，无法检测不可枚举属性

function B() {this.b=2;}; B.prototype.a=1; var test=new B(); Object.keys(test)
//["b"]，无法检测原型链上的属性
```


##### 循环： 指的是在满足条件的情况下，重复执行同一段代码

   * while

```javascript
 var i=0;
 while(i<3)//执行条件
 {
 i++;//执行语句
 console.log(i);//1,2,3
 }
```
   * do...while

```javascript
var i=0;
do{
i++;//执行语句
console.log(i);//1,2,3
}while(i<3);//执行条件
```
   * for

```javascript
for(var i=0;i<3;i++)//执行条件，执行语句
{
console.log(i);//0,1,2
}
```

##### 递归：指的是一个函数不断调用自身的行为
##### 闭包:指的是function函数体内还要镶嵌一个函数，通常是用return返回的
   * 闭包的作用：1.为了能从外部访问局部变量2.让这些变量的值始终保持在内存中。

```javascript
function foo() {
var n=1;
function foo1() {
  alert(n);}
return foo1;
}
var test=new foo();
test();//1;在内部有个function，就可以创建实例，返回局部变量值
```
   * 在上述中，foo1就是闭包，闭包就是能够读取其他函数内部变量的函数

```javascript
function foo() {
 var n=1;
 add=function () {
 n+=1; //全局函数
}
 return function foo1() {
 alert(n);
  }
}
 var test=new foo();
 test();//1,直接返回闭包foo1
 test();//1,值不会变化
 add();//这是一个全局变量，只有调用时，才会影响函数体
 test();//2，已经调用了全局变量，所有d返回2
 add();//再次调用该函数
 test();//3
 ```
   * 在上述中，我们发现add在调用了一次之后，n的值还是存在的，值是始终保存在内存中的
   * 书上有一段函数，是用this调用的闭包，很值得思考
 
```javascript
var name='ly';
var obj={ name:'lyy', 
say:function () {  //在这个时候没有使用闭包
return function () {
  return this.name; };//注意看return这个函数，并没有返回任何对象的调用，返回的只是this.name。并没有指明他的对象
 }
  };
 alert(obj.say()());//'ly'obj.say()返回一个匿名函数,这个时候，say()虽然是来自obj,但是方法返回的是this.name;并没有调用任何对象，this默认是window
```

```javascript
var name='ly';
var obj={ name:'lyy', 
say:function () {
var that=this;//已经把that放在了闭包可以访问函数中了
return function () {//这里就是一个闭包，他执行的是闭包的东西，访问的是整个函数体的东西，除了闭包里的东西不能访问
  return that.name; };
 }
  };
 alert(obj.say()());//这是将this的变量保存在闭包可以访问的地方‘lyy'
 ```
综上所诉，闭包的运行机制就简单了，在一个环境下同时出现两个变量，为了避免冲突，可以使用闭包，这样就只能访问闭包里的东西，其他就不能访问
  
#####ASCII码值的转换
   * "A".charCodeAt(0)//A->65;(0)代表的是一个顺序，0，1，2 (类似数组中的每个值的顺序，是从0开始的)
   * String.fromCharCode(97);//97->a;
   * 发现一个问题，函数是否具有length属性，然后写了一段代码
  
  ```javascript
function has() { }; has.hasOwnProperty('length')
true //发现length属性是存在函数上的，然后属性length到底是根据什么来定义的
```
   * 参数个数和函数length属性是否相等
   * 实参
   
   ```javascript
   function argumentMethod() { 
 while (arguments.length<30) { 
		 arguments.length++;//代表的是实参
		 console.log('参数个数'+arguments.length+','+'函数length'+my.length);
	} 
}  
argumentMethod();//由此可见打印出来的结果并不相等
```
   * 形参
  
  ```javascript
  var s='a';//s是个字符串，代表的是形参
var count=1;//代表的是形参个数
for (var i = 98; i < 100; i++) {//使用的是阿斯克码值，97是a
  s+=','+String.fromCharCode(i);//s就是字符串,String.fromCharCode()是转换成字母
  count++;//形参个数也增加
eval('function parameter('+s+') {}');//eval里是一个函数，有引号的地方代表不变的
console.log('参数个数:'+conunt+my.length); 
} 
```

```javascript
function random() {
	var s='a';
	for (var i = 98; i < 100; i++) {
  s+=','+String.fromCharCode(i);}
  return s;
} 
random();//提取出来的函数，可以用来生成参数个数，中间用逗号隔开，生成小写字母
```

   * 随机写出一个字符串
   
```javascript
function random(len) { 
	var s='';//定义一个空字符串
	while(s.length<len&&len>0) { //为了生成的字符串长度为len
		var r=Math.random();//定义一个值在0到1之间随机数
		s+=String.fromCharCode(Math.floor(r*26)+97);//使用阿斯克码值的转换成小写字母，floor取得整值，97是a的阿斯克码值
	} 
	return s; //返回的是s
} 
random(3);//随机生成一个长度为3的字符串
```
   * 函数的length属性是根据形参个数来改变的，和实参个数无关
  


更多内容可以看https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Introduction_to_Object-Oriented_JavaScript
