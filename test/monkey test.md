#
* 手机连接电脑
* adb devices
 查看设备连接

* adb install 包名   
 进入到包目录，安装需要测试的包
* aapt dump xmltree ColaBox.apk AndroidManifest.xml   
 查看源码文件
* aapt dump badging ColaBox.apk |findstr "package"     
 找到package名
* adb shell monkey -p your.package.name 500          
 运行指定pack包 乱点500次  ，-p约束
* adb shell monkey -v -v -v -s 8888 --throttle 300 --pct-touch 30 --pct-motion 25 --pct-appswitch 25 --pct-majornav 5 --pct-nav 0 --pct-trackball 0 -p 包名 10000 

3个-v显示最详细的测试信息，指定种子值为8888，操作时间延迟300ms,指定触摸事件占30%、手势事件占25%、Activity跳转占25%、主导航占5%、方向导航0%、轨迹球0%，剩下的15%随机分配给其它未指定的事件，

