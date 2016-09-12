my_variable=10
my-boolan=True  #布尔值首字母大写，后面不用打分号
print my_boolean


def spam():  #一个函数
    eggs = 12  #需要空4格
    return eggs # return 
        
print spam()  #返回12

"""
三个双引号就苏多行注释
"""
eight = 2 ** 3 # 2的3次方

'he'\s'#\代表

name='ly'[1]
print name #y
print len(name) #2
 print   name.lower() #ly
 print   name.upper() #LY
   print str(name) #'ly'
   name='ly12'
name.isalpha() #检查是否只含了字母
  """ 
   string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)  #用%替换后面的变量
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)
"""

"""
from datetime import datetime
now=datetime.now()
print now #获取当前时间
print now.day #now.month now.year
print '%s/%s/%s' % (now.year, now.month, now.day) #2016/9/10
"""

"""
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower() #提问
    if answer == "left" or answer == "l":  #判断语句
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again." #打印
        clinic()

clinic() #调用函数
"""

"""
from module import function # 导入方法，moudle,function
"""




