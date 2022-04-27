# Apeclass的Python大课
# 第0章 前言 Python简介与安装
## 1. Python环境的安装
登陆网站：https://www.python.org/ ，选择最新版本Python进行安装，这里安装的是Win的3.10.1版本
> 注意进入安装界面，选择Python3.10到环境变量中
> 选择自定义安装

安装完毕后，进入运行cmd，键入`python`，将显示如下：

<img src="D:\Github\Python\PythonNotes\pic\python.png" alt="Python"  />

## 2. Pycharm的安装
登陆网站：https://www.jetbrains.com/pycharm/ ，这里选择下载，选择社区版（免费版）。
> 由于Pycharm的专业版为收费版，因此这里下载社区版。
> 安装过程中，记得选中关联.py
> 安装专业版时，需要注册账号，社区版本不需要。

新建工程：

Pycharm进行新建工程过程中，需要进行一些配置。

1. 工程的位置
2. 选择解释器，如下图所示，选择系统自带的python3（就是上一个环节安装的软件）

![pycharmNewProject](D:\Github\Python\PythonNotes\pic\pycharmNewProject.png)

![pycharmNewProject1](D:\Github\Python\PythonNotes\pic\pycharmNewProject1.png)

## 3. Python简介
Python由荷兰数学和计算机科学研究学会的Guido van Rossum 于1990 年代初设计，作为一门叫做ABC语言的替代品。
python之父：吉多·范罗苏姆（Guido van Rossum） ，是一名荷兰计算机程序员，他作为 Python 程序设计语言的作者而为人们熟知。别称：龟叔
python特点：语言简洁，对初学者友好。拥有强大的第三方库，使得程序员在开发时得心应手。
python信仰：人生苦短，我用python
从业方向：Python全栈工程师、爬虫、自动化运维、数据分析、人工智能

## 4. Python版本
Python版本：Python2.x：官方2020年停止更新、源码不规范、重复较多
Python3.x：功能更加强大且修复了很多bug、源码清晰简单

## 5. 编译型与解释型语言的区别
编译型：开发完成，一次性把所有代码编译成机器能识别的二进制码
> 代表语言：C、C++
> 优点：执行速度开，缺点：开发速度慢，调试周期长

解释型：代码从上到下一行一行解释并运行
> 代表语言：python、php
> 优点：开发效率快、调试周期短；缺点：执行速度相对慢

## 6. Python的解释器
1、Cpython(官方推荐)：把Python代码转化为C语言能识别的二进制码
2、JPython：把Python代码转化为java语言能识别的二进制码
3、PyPy：将所有代码一次性编译成二进制码，加快执行效率（模仿编译型语言的一款Python解释器）
4、其他语言解释器：把Python代码转化为其他语言能识别的二进制码

# 第1章 变量与数据类型
## 1. 变量与赋值
什么是变量？
变量实际上是实体的指代，可变化的
> Python中无常量这个数据类型，一般以大小写（人为规定）区分常量（大写）与变量
> 可重新赋值。即x = 2与x = 5这两个x的地址实际上不一样的

```python
# 查看变量的内存地址
x = 2
print(id(x)) # 返回的是十进制的，注意
```
对变量进行赋值：
1、通过=进行赋值
2、被重新赋值之前的值被系统回收了，而且其内存地址也不一样

## 2. Python的六大基本数据类型
> 注意：强调的是基本，数据类型和数据结构指向的范围更加广泛，不要产生错误的认知，形成思维定式

```python
# 查看变量的数据类型
type(x)
```
1、`int`(整数):python中无具体范围
2、`float`(浮点数):因为计算机只认识0与1，则通过浮点的方式来表达小数

```python
# 通过int/float可以进行数据的转换
int('1')
float('1.0')
# 可以通过float来表达无限INF
float("INF")
```
3、`string`(字符串、字符序列)：在有些语言中，单个字符也是一个基本的数据类型(char)

```python
str(2)
# '2'
```

> string是有序的
> 表示方法：'1'、"1"、"""1"""或```1```(可以进行换行)；两种模式都可以表示，
```python
# 使用三引号进行换行
x = """
...dsa"""
# 结果为：'\ndsa',可以表达换行
```
> 转义字符：告诉当前解释器，表示的是一个字符或一个特殊字符
> 通过\来转义：如\n	\"
```python
s = "2\n3"
print(s)
# 2
# 3
```

4、`boolean`(布尔值)：用来表示`True`与`Flase`
```python
bool(2)
bool(0)
```
> `True`等价于1
> `Flase`等价于0

5、`bytes`(二进制序列)：

```python
bytes("Hello World".encode("UTF-8"))
# b'Hello World'
```

6、`None`(空)
因为`False`与`0`也代表一种结果，而`None`可以表示无结果

## 3. Python的四大基本数据结构
1、`list`(列表)：用来转载*不同数据类型*的数据集结构。
特点：1）有序的；2）可以装载任意数据类型；3）*可以更改的*

```python
# 如何表示list
# 1）通过list()建立一个列表
list("Hello World")
# 2）通过[]声明一个列表
a = [1, 2, 3]
```

2、`tuple`(元组)：可以简单地认为元组就是不可修改的列表，常用来记录
特点：1）有序的；2）可以装载任意数据类型；3）*不可更改*
```python
# 如何表示tuple
# 1）通过tuple()建立一个元组
tuple("Hello World")
# 2）通过()声明一个列表
a = (1, 2, 3)
# 注意，将一个元素声明为元组时，用(,)
b = (1, )
```

3、`dict`(字典)：字典也叫hashtable（散列表），通过hash（散列）函数将传入的`key`值生成地址来查找`value`
`key` -> `hash`函数 -> 返回了`value`的地址 -> 通过地址返回了`value`值
特点：1）*无序的*；`python3.6`是有序的，之后就更改回无序的
2）字典中key必须是可hash的（需要不可更改，唯一的），如key不能使list数据结构
3）可以更改的，其内容是可更改的
4）`key`值与`value`值可以包括*任何数据类型*

```python
# 如何表示dict
# 1）通过dict()建立一个字典
dict(a = 2)
# 2）通过{}来声明一个字典
a = {"a" : 2}
```

4、`set`(集合)：其实是没有`value`的字典,*注意*不是没有重复的列表
特点：1）*无序的*；`python3.6`是有序的，之后就更改回无序的
2）集合中的`key`必须是可`hash`的；
3）可以更改的
4）元素（即key）是唯一的，如set(1, 2, 2)，结果为{1,2}
> set中元素是唯一的，会自动去除重复元素，注意`1`与`1.0`认为是重复的
```python
# 如何表示set
# 1）通过set()建立一个集合
set(1, 2, 2)
# 最后机器默认为{1, 2}：自动删除了重复的，因为key是唯一的
# 2）通过{}来声明一个集合
a = {1， 2， 3}
```

## 4. 课后作业
1、四大基本的数据结构中，哪些可变/不可变；哪些有序/无序
`list`：可变，有序
`tuple`：不可变，有序
`dict`：可变，无序
`set`：可变，无序
2、创建`list`,`tuple`,`dict`,`set`实例，每个数据结构的实例需要包括六大基本类型
```python
# 创建list实例，包括int、float、string、boolean、bytes、None
list1 = [int(1), float(1.0), str('a'), bool(0), bytes(1), None]
type(list1)
# 结果：[1, 1.0, 'a', False, b'\x00', None]

# 创建tuple实例，包括int、float、string、boolean、bytes、None
tuple1 = (int(1), float(1.0), str('a'), bool(0), bytes(1), None)
type(tuple1)
# 结果：[1, 1.0, 'a', False, b'\x00', None]

# 创建dict实例，key值包括int、float、string、boolean、bytes、None
dict1 = {1:None, 1.0:None, '1':None, False:None, bytes(1):None, None:None}
type(dict1)
# 结果：{1: None, '1': None, False: None, b'\x00': None, None: None}

# 创建dict实例，value值包括int、float、string、boolean、bytes、None
dict2 = {1:1, 2:1.0, 3:'1', 4:True, 5:bytes(1), 6:None}
# 结果：{1: 1, 2: 1.0, 3: '1', 4: True, 5: b'\x00', 6: None}

# 创建set实例，值包括int、float、string、boolean、bytes、None
set1 = {1, 2.0, '1', False, bytes(1), None}
type(set1)
# 结果：{False, 1, 2.0, b'\x00', '1', None}
```
总结：
1）字符串表示用`str`,而不是`string`
2）字典中无论`key`值还是`value`值都可以用*任何数据类型*
3）set中元素是唯一的，会自动去除重复元素，注意`1`与`1.0`认为是重复的

# 第2章 Python函数运算符与数据类型的常用方法
## 1. Python的函数的基本介绍
函数：一段可以直接被另一段程序或代码引用的程序或代码，也叫做子程序，*方法*
特点：1）可重复使用；2）可互相调用
目的：为了代码段的复用

**如何定义一个函数**
函数组成：参数列表 + 函数体 + 返回值
*参数列表*：
1）若有必须参数，必须按顺序传入

```python
def foo(arg, arg_2):
	return arg + arg_2
# 必须参数传参
result = foo('1','2') 
```
2）关键字参数：根据关键字参数传参可以无视顺序

```python
def foo(arg = None, arg_2 = None):
	return arg + arg_2
# 关键字参数传参，用于不知道函数参数的顺序
result = foo(arg_2 = '1',arg = '2')
```
3）默认参数：提前对形参赋值
```python
def foo(arg = 'gcm', arg_2 = None):
	return arg + arg_2
# 默认参数传参，对于赋值的参数，采用默认值
result = foo(arg_2 = '1')
```
4）不定长参数：可以接收任意长度（数量）的参数，在装饰器中大量应用，不需要关心传的是什么
这里不定长参数主要有两种形式：`*`(接收参数元组tuple)，`**`(接收参数字典dict)

```python
def foo(*args):
	print(args)
	return None
# 不定长参数传参，参数元组
result = foo("Hello", "World")
# 结果：("Hello", "World"),这里参数是一个元组
# None
```
```python
def foo(*args, **kwargs):
	print(args)
	print(kwargs)
	return None
# 不定长参数传参，参数元组
result = foo("Hello", "World", _class1 = '1', _class2 = '2')
# 结果：("Hello", "World"),这里参数是一个元组
# {'_class' = '1', '_class2' = '2'},这里参数是一个字典
# None
```
> `*`：代表了省略，省略了参数`tuple`(元组)
> `**`：省略了参数`dict`

*函数体*
*返回值*：若不指定return，默认返回None


def 函数名(参数列表):
	函数体
	return 返回值
> 注意要有`:`

```python
def foo(arg):
	return "Hello " + str(arg)
result = foo(gcm)
print(result)
# 结果：Hello gcm
```

## 2. Python的运算符
1、**算术运算**
`+`、`-`、`*`(乘法)
`/`(除法)、`//`(整除)
`%`(取余)
`**`(x的y次幂)
```python
x ** y
```
`开方` : 没有提供直接的运算符
```python
4 ** (1/2)
```
`abs()`(绝对值,abs(-1))
2、**赋值运算**
通过`=`赋值
3、**比较运算**
比较的是两个对象的字面值，字面值可以暂时理解为*输出值*
`<`、`>`、`<=`、`>=`、`==`、`!=`
比较数字：按照数字大小
比较字符串：按照字母所在位置上依次进行对比，一旦有比较出来的，就停止比较

> 比较不同数据类型，无法进行比较。因为Python是一个强类型语言
```python
a = 'abc'
b = 'abz'
c = 'abcd'
# a < b  b > c
```
4、**标识号比较运算**
比较的是两个变量的内存地址，
`is`：等于
`is not`：不等于

> 赋值类型为`str`、`int`时，要考虑`Python`的`常量池`
> ```python
a = 'abc'
b = 'abc'
a == b # True
a is b # True：因为Python中有一个常量池，字符串在常量池，地址一样
c = '你好'
d = '你好'
c is d # False：中文不在常量池中
>```

5、**成员检测运算**
判断元素是否在当前序列中
`in`：在
`not in`：不在
```python
a = [1, 2, 3]
1 in a # True
b = [1, 2]
b in a # False
a = [[1,2], 3]
b in a # True
```

6、**布尔运算**
判断当前语句的结果是`True`还是`False`
`and`：与运算，只有两边为`True`才`True`
`or`：或运算，只有两边表达式为`False`才为`False`

> `or`有短路逻辑，从左往右，只要出现一个`True`则为`True`，就不向右执行
>
> ```python
> True or print("statement B") # True
> print("statement B") or True # "statement B" True
> ```
> `print`返回的是无数据类型，NoneType，即None

`not`：取反

```python
not print("statement B") or print("statement A") # "statement B" True(对print返回的None取反为True，则不向右执行)，not优先级大于or
```

7、 **位运算**
二进制运算
`~`、`^`、`>>`、`<<`、`&`、`|`

## 3. Python的运算符优先级

自上而下是优先级提升

|               运算符               |                  描述                  |
| :--------------------------------: | :------------------------------------: |
|                 or                 |               布尔运算或               |
|                and                 |               布尔运算与               |
|                not                 |                逻辑取反                |
| in、not in、is、is not、<、!=、... | 成员检测运算、标识号检测运算、比较运算 |
|               +、-、               |               加法和减法               |
|            *、/、//、%             |         乘法，除法，整除，取余         |
|               +x、-x               |                 正负数                 |
|                 **                 |                   幂                   |

> 自定义优先级：通过`()`。
> 若不确定优先级，出于可读性和避免位置的Bug，我们都应该用`()`来自定义优先级
> ```python
> (not b and c) or (d and e)
> ```

## 4. 课后作业
用函数实现一个具有加减乘除，整除，取余，开方的计算器
```python
my_calculator.py
def add(arg1, arg2):
	return arg1 + arg2
def sub(arg1, arg2):
	return arg1 - arg2
def mult(arg1, arg2):
	return arg1 * arg2
def div(arg1, arg2):
	return arg1 / arg2
def divi(arg1, arg2):
	return arg1 // arg2
def rema(arg1, arg2):
	return arg1 % arg2
def power(arg1, arg2):
	return arg1 ** arg2
print(add(1, 2))
print(sub(1, 2))
print(mult(1, 2))
print(div(1, 2))
print(divi(1, 2))
print(rema(4, 3))
print(power(4, 1/2))
```
在交互模式中练习Python运算符

# 第3章 字符串的使用
## 1. 字符串(字符序列)和字节序列
**字符**：由于历史原因，将字符定义为`unicode`字符还不够准确，但是未来字符的定义一定是`unicode`字符
**字节**：就是字符的二进制表现形式
**码位**：我们计算机存储显示的实际上是码位，不过`python3`自动将码位进行了转换，显示出我们明白的东西。注意码位和字符是两个不同的东西
> 在`UNICODE`标准中以4-6个十六进制数字表示
> 注意码位和字符是两个不同的东西

```python
# 显示'你好'的码位
'你好'.encode("unicode_escape").decode()
# 结果：'\\u4f60\\u597d',但这并不是真正的码位
'\u4f60\u597d'
# 结果：'你好'
len('\u4f60\u597d')
# 结果：2
```

**编码**：
1）字符序列(string)->字节序列(bytes) *编码(encode)*

```python
"你好".encode("utf-8") # 由于历史原因，编码方式有很多种，我们只使用utf-8
# 结果：b'\xe4\xbd\xa0\xe5\xa5\xbd'
```

2）字节序列(bytes)->字符序列(string)	*解码(decode)*

```python
b = "你好".encode("utf-8") # 由于历史原因，编码方式有很多种，我们只使用utf-8
# 结果：b'\xe4\xbd\xa0\xe5\xa5\xbd'
b.decode("utf-8")
# 结果：'你好'
```

**编码错误**：
1）*乱码*和*混合编码(两种不同编码方式混合)*
2）如何解决：
方法一：*检查编码*：由于没有办法通过字节序列来得出编码格式，都是通过`统计学来预估`当前的编码
> 使用第三方库：chardet(未安装的需要安装，输入命令行：pip install chardet)
> ```python
> b = '你'.encode("utf-8") + '好'.encode("gbk")
> b.encode("utf-8") #将报错
> import chardet
> chardet.detect(b) 
> # {'encoding': 'ISO-8859-1', 'confidence': 0.73, 'language': ''} ，可信度0.73，实际上不准确的
> chardet.detect("你好".encode("utf-8")) 
> # {'encoding': 'utf-8', 'confidence': 0.7525, 'language': ''},结果就准确了，实际上使用统计学来预估的
> ```

方法二：舍小取大
*忽略错误编码*

```python
b_2 = "你好".encode("utf-8") + "啊".encode("gbk")
b_2.decode("utf-8", errors = 'ignore')
# '你好'，忽略了gbk编码的字节
```
*利用鬼符来替换*
```python
b_2 = "你好".encode("utf-8") + "啊".encode("gbk")
b_2.decode("utf-8", errors = 'replace')
# ''你好��''，用鬼符来替代gbk编码
```

## 2. 字符串的CRUD操作
**CRUD**:增删改查

*creat*(创建)
`+`、`+=`
```python
a = "a"
id(a)
# 2481711312432
a += "b" # "ab"
id(a)
# 2481755127536
```

*retrieve*(检索)
1、`根据索引获取字符`：在计算机语言中，索引值是从0开始数的

```python
a = "Hello World"
a[1] #'e'
```

2、`find`与`index`：获取目标字符的索引值

```python
a = "Hello World"
a.find("e") # 1
a.index("e") # 1
```

> `find`与`index`区别，`find`找不到值，返回-1；`index`找不到值，会报错

3、`startswith`和`endswith`：判断字符串是否为特定内容开头或结尾

```python
f = "2022-04-19-xxxx"
f.startswith("2022-04-19")
# 结果：True
e = "xxx.jpg"
e.endswith(".jpg")
# 结果：True
```
> 通过`dir`可以查看该数据下有那些方法和参数，dir("2022-04-19-xxxx")

*UPDATE*更新
1、`replace`:替换，x.replace("目标值", "替换值")，返回替换后的字符串x
```python
a = "Hello werld, Hello Werld"
a.replace('wer', 'wor')
# 结果："Hello world, Hello World"
```
2、`split`：分割，返回的是分割后的列表
```python
a = "<<python>>, <<java>>, <<c>>"
a.split(",")
# 结果：["<<python>>","<<java>>","<<c>>"]
```
3、`join`:拼接,`'y'.join(list1)`通过y将list中字符串拼接起来

```python
a = "<<python>>, <<java>>, <<c>>"
b = a.split(",")
",".join(b)
# 结果："<<python>>, <<java>>, <<c>>"
```
> `split`与`join`很有用
> `join`

*DELETE*删除
1、`strip`：去皮，str1.strip("x")，将字符串str1两边存在的x均去除
```python
a = "    hello, world      "
a.strip(" ")
# "hello, world"
```
2、`rstrip`与`lstrip`：将右或左的特定字符去掉

> 字符串的方法还有很多，可以通过查找文档来使用

## 3. 字符串的输出和输入
**保存到文件**
```python
# open函数打开一个文件，若无则会新建，但是路径不对会报错
# open("文件名", "w/r", "编码方式"),返回文件的句柄
output = open("output.txt", "w", encoding = "utf-8")
content = "Hello World"
# 正式写入文件
output.write(content)
# 关闭文件句柄
output.close()
```
> 注意：`w`是重新输入，无论原先文件内有什么内容，均重新填入

**读取文件**
```python
input = open("output.txt", "w", encoding = "utf-8")
# 获取文件中内容
content = input.read()
print(content)
# 第二次并不会读取出来，因此content2为空。暂时理解为只能读取一遍
content2 = input.read()
print(content2)
```

**追加文件**：
```python
output = open("output.txt", "a", encoding = "utf-8")
content = "\nHello python"
output.write(content)
output.close()
```
> 注意：在原有文件基础上再加入内容

## 4. 字符串的格式化输出
**format**:按照指定要求将字符串输出
1、*按传入参数默认顺序*
```python
a = "ping"
b = "pong"
print("play pingpong: {}, {}".format(a, b))
# "play pingpong: ping, pong"
```
2、*按指定参数索引*
```python
a = "ping"
b = "pong"
print("play pingpong: {0}, {1}, {0}, {1}".format(a, b))
# "play pingpong: ping, pong, ping, pong"
```
3、*按关键词参数*
```python
print("play pingpong: {a}, {b}, {a}, {b}".format(a='ping', b='pong'))
# "play pingpong: ping, pong, ping, pong"
```
4、*按变量*
```python
a = "ping"
b = "pong"
print(f"play pingpong: {a}, {b}")
# "play pingpong: ping, pong"
```
> 缺点：只有Python3.6以上才能使用

5、*小数的表示*
```python
print("{:.2f}".format(3.14159))
# "3.14"
```

**%方法**：与`format`方法没有本质区别
```python
a = "ping"
b = "pong"
print("plaing %s %s" % (a,b))
# "plaing ping, pong"
```
> `%`是一种老式做法

## 5. 课后作业
1、练习字符串的编码和解码
2、练习字符串的CRUD
3、练习字符串的格式化
4、将练习内容保存到本地文件
```python
# 练习字符串的编码和解码
content = '你好啊' #字符串
eContent = content.encode("utf-8")
print(eContent)
dContent = eContent.decode("utf-8")
print(dContent)
# 练习字符串的CRUD
cont = 'hello'
cont += ' world'
print(cont)
print(cont[1])
print(cont.find('e'))
print(cont.index('e'))
print(cont.startswith("he"))
print(cont.endswith("ld"))
contList = cont.split(" ")
print(contList)
print(",".join(contList))
print(cont.replace("e","o"))
cont1 = "    hello world     "
print(cont1.strip(" "))
print(cont1.rstrip(" "))
print(cont1.lstrip(" "))
# 练习字符串的格式化
print("playing {}, {}".format("a", "b"))
print("playing {3}, {2}, {1}, {0}".format("a", "b", "c", "d"))
print("playing {a}, {b}, {c}, {d}".format(a="a", b="b", c="c", d="d"))
a="a"
b="b"
print(f"playing {a}, {b}")
# 将练习内容保存到本地文件
f = open("output.txt", "w", encoding="utf-8")
f.write("hello")
f.close()
f1 = open("output.txt",'r',encoding="utf-8")
print(f1.read())
f2 = open("output.txt","a",encoding="utf-8")
f2.write(" world")
f2.close()
```
# 第4章 变量与引用简介
## 1. 了解变量和引用
**变量**：简单点说，变量就是指向一个实体
```python
a = 1
# a指向是一个实体，一个内存地址
```

**引用**：变量指向一个变量

```python
a = 1
b = a
# a与b的内存地址一样
```

## 2. 基础数据结构的CRUD操作
### list的CRUD
**list**：列表，**list中存在的元素就是引用**
*create*增加：
1、`append`：末尾添加元素，并不改变list的内存地址

```python
l = []
id(l)
l.append("a")
id(l)
# l的内存地址不改变
```

2、`+`和`+=`
`+`：拼接两个列表，然后返回一个新的列表
```python
l1 = ['a']
id(l1)
l2 = ['b']
id(l2)
l3 = l1 + l2
id(l3)
# l1、l2、l3指向内存地址均不同
```
`+=`：在原有列表中加入元素，但返回是相同内存地址的列表
> 在字符串string中，`+=`会更改字符串的内存地址
> 但在list中，`+=`并不会改变字符串的内存地址

```python
l = ['a']
id(l)
l += 'b'
id(l)
# l = ['a', 'b']，内存地址不改变
```

`*`与`*=`：批量增加n个相同元素，但这些元素的内存地址均相同
```python
a = 'a'
id(a)
l = [a] * 5
id(l[0])
id(l[4])
# l = ['a', 'a', 'a', 'a', 'a']
# 列表l中每个元素的内存地址均相同
a = 'b'
# 但l中元素内容不变，因为这里的a是一个新的a（内存地址已经改变），而不是原来的了。
```
> 这是因为list**列表所存的元素实际上是引用**

3、`insert`：在指定位置添加元素，`list.insert(索引值, 元素)`
```python
l = ['a']
l.insert(0, 'b')
# l = ['b', 'a']
```
> 若添加一个超过现有列表的长度的话，自动添加到末尾
> ```python
> l = ['a']
> l.insert(10, 'b')
> # l = ['a', 'b']
> ```

*retrieve*检索
1、索引取值
> string，bytes，list，tuple均是有序的，可以进行索引取值
> dict与set是无序的，不支持索引取值
> l[-1]：取最后一个值

2、切片：`list[start:end:step]`
> 这里end是取不到的，只能取到start -> end - 1范围，取值范围`[start, end)`左闭右开
> step不取的话，就是1

```python
l = list(range(100)) # 获取内部含有0-99的列表
l[0:10:1] # 取前10个元素，
l[20:30] 
l[30:-1] # 取[30,最后一个值)，-1：代表最后一个值
```

3、`index`:`list.index(元素)`，返回的元素在list的索引值，若无则报错

```python
l = ['a', 'b', 'c']
l.index('a')
# 0, 返回的是索引值，就是该元素在列表什么位置
```

*update*更新
1、索引赋值，对内部元素进行更改时，但不改变list的内存地址。因此称list内容是可变的
```python
l = ['a', 'b', 'c']
l[0] = 'a_1'
# l = ['a_1', 'b', 'c']
```

2、切片赋值：将一整段元素进行赋值
```python
l = ['a_1', 'a_2', 'b', 'c']
l[0:2] = 'a'
# l = ['a', 'b', 'c']
```
> 切片赋值，是将一个序列（一段元素）赋值为新的序列，'a'字符串为一个序列，因此可以赋值
> 若l[0:2] = 1, 将会报错1不是序列

*delete*删除
1、`pop()`从末尾删除元素并返回删除的元素

```python
l = ['a', 'b', 'c']
l.pop()
# 'c'
# l = ['a', 'b']
```
2、`clear()`清除当前列表的元素，这里只是清除，但不会改变list的内存地址
```python
l = ['a', 'b', 'c']
l.clear()
# l = []
```

*sort*排序
1、`sort()`，将list中元素按正序排列，列表内存地址不变

> 列表本身带的函数`list.sort()`，因此可以用`.`进行调用

```python
l = [1,3,2,4,6]
l.sort()
# l = [1,2,3,4,6]
```
2、`sorted`，返回一个新的列表（元素已经排好序）
> 不是列表本身带的函数，只能用`sorted(list)`调用

```python
l = [1,3,2,4,6]
l1 = sorted(l)
# l内元素依然无序，l1内元素已经排好序
# l与l1内存地址不同
```
3、 `reverse`倒序，对元素逆序排列。`list.reverse()`
> 特点与sort一样，返回原先的列表

4、`reversed`倒序
> 不是列表本身带的函数，只能用`reversed(list)`调用
> 返回的是迭代器对象

```python
l = [1,3,2,4,6]
l1 = list(reversed(l))
# l1 = [6,4,3,2,1]
```
### tuple的CRUD
*create*：无，因tuple不可更改
*retrieve*：索引取值、index（无该元素，返回None）、切片
*update*：无
*delete*：无

### dict的CRUD
*create*
1、键对值赋值，key->value，并不会改变dict的id
```python
d = {}
d['a'] = 1
```
2、`update`：`dict.update(dict1)`,提供合并字典的功能，并不会改变dict的id
```python
d = {'a':1}
d1 = {'b':2, 'c':3}
d.update(d1)
# d = {'a':1, 'b':2, 'c':3}
```
3、`setdefault`:`dict.setdefault(key, 0)`
> 若这里key为dict中已有元素，则dict内不会更改，返回key对应的value
> 若这里key不是dict中元素，则dict则会添加，返回的设置的默认值0

```python
d = {'a':1, 'b':2, 'c':3}
d.setdefault('a', 0)
# 返回1，且d = {'a':1, 'b':2, 'c':3}不变
d.setdefault('d', 0)
# 返回0，且d = {'a':1, 'b':2, 'c':3, 'd':0}添加
```
*retrieve*
1、键对值访问
2、`get`：`dict.get(key)`，返回key对应的value
> 因键对值访问时，若dict中无该key，则会报错
> 而`get`则不会报错，返回值为None。
> 当然可以自定义默认值dict.get(key, 0)，若无key，则返回自定义值0

```python
d = {'a':1, 'b':2, 'c':3, 'd':0}
d.get('a') # 返回1
d.get('f') # 返回None
d.get('f', 0) # 返回自定义值0
```
3、`keys()`:`dict.keys()`,返回所有的key
> 但返回的是一个新的对象，需要进行对象转换

```python
d = {'a':1, 'b':2, 'c':3, 'd':0}
l = list(d.keys())
# l = ['a','b','c','d']
```
4、`values()`:`dict.values()`，返回所有的value
> 但返回的是一个新的对象，需要进行对象转换

5、`items()`:`dict.items()`, 返回所有的键对值
> 但返回的是一个新的对象，需要进行对象转换

*update*
1、键对值赋值
```python
d = {'a':1, 'b':2, 'c':3, 'd':0}
d['a'] = 0
# d = {'a':0, 'b':2, 'c':3, 'd':0}
```
2、`update`:`dict.update(dict1(需要修改的键对值))`,进行更新
```python
d = {'a':1, 'b':2, 'c':3, 'd':0}
d.update({'b':200, 'c':300})
# d = {'a':1, 'b':200, 'c':300, 'd':0}
```
*delete*
1、`pop()`:`dict.pop(key)`，返回value，同时dict进行删除元素
2、`popitem()`:`dict.popitem()`,对于人来说，相当于**随机**返回一个item（）
> dict要认为是一个**无序**的

3、`clear`:`dict.clear()`,清空dict内元素

### set的CRUD
*create*
1、`add`:`set.add(key)`，添加一个key
> `set`认为是只有key的字典

```python
s = set()
s.add('a')
s = {'a'}
```
*retrieve*
1、运算符`in`成员检测
```python
s = {'a', 'b', 'c'}
'a' in s
# True
```
*update*
1、`update`:`set.update(set1)`，相当于将set1元素添加到set中
```python
s = {'a', 'b', 'c'}
s.update({'d','e'})
# s = {'a', 'b', 'c', 'e', 'd'}
```
2、`union`:`set.union(set1)`，将set1元素添加到set中，并返回一个新的set
```python
s = {'a', 'b', 'c'}
set1 = s.union({'e', 'f'})
# set1 = {'a', 'b', 'c', 'e', 'f'}
```
*delete*
1、`remove`:`set.remove(key)`,删除对应的key
> 若key不存在，则会报错

```python
s = {'a', 'b', 'c'}
s.remove('a')
# s = {'b', 'c'}
```
2、`discard`:`set.discard(key)`,删除对应的key
> 若key不存在，则返回None
> 
```python
s = {'a', 'b', 'c'}
s.discard('f')
# s = {'a', 'b', 'c'}
```

3、`pop`:`set.pop()`，**随机**删除一个元素，返回元素
## 3. 课后作业
1、完成四大基础数据结构的CRUD操作
太长，这里就不进行展示，详见代码CRUD.py

# 第5章 流程控制、循环语句、异常处理
## 1. Python的逻辑控制语句
### 条件判断语句
`if`
`if else`

```python
a = 100
if a > 100:
	print("a超过阈值")
else:
	print("a小于阈值")
```
`if elif ... else`

```python
a = 50
if a > 100:
	print("a超过阈值")
elif a == 50
	print("a只有阈值的一半")
else:
	print("a小于阈值")
```
### 循环语句
`for`：去**遍历**一个可迭代的对象（暂时理解为list），会影响相同作用域当中的变量
```python
l = [1, 2, 3, 4, 5] # list是一个可迭代对象
for e in l:
	print(e)
```
> `for`有一个作用是获取索引值和值，利用`enumerate(list)`生成一个元组
> ```python
> l = [1, 2, 3, 4, 5]
> for i,e in enumerate(l):
>     print(f"index:{i}, value:{e}")
> ```

`while`:
> `while`一定要有退出机制，一定要有逻辑判断语句来退出`while`

`while 判断语句:`
		`表达式`

```python
counter = 0
while counter < 100:
	print(f"sim statement : {counter}")
	counter += 1
```

`while True:`
		`判断语句`
		`表达式`
```python
counter = 0
x = 84
while True:
	if counter == x:
		break
	print(f"sim statement : {counter}")
	counter += 1
```

`跳出循环`
1、`break`:停止当前循环
2、`continue`:跳过当前的执行逻辑，立即继续循环语句的执行
```python
l = [1, 2, 3, 4, 5]
for e in l:
	if e == 3
		continue
	else:
		print(f"search element:{e}")
```
3、`pass`:起到提示作用，跳过当前条件判断中的执行语句，后续语句继续执行
```python
l = [1, 2, 3, 4, 5]
for e in l:
	if e == 3
		pass
	else:
		print(f"search element:{e}")
	print("-----------------------")
```
## 2. Python的异常与处理
**异常**：程序遇到严重错误时，会终止程序的运行并抛出异常
```python
def my_sub(a, b):
	return a / b
if __name__ == '__main__': # 在当前脚本下执行下面表达式
	my_sub(1, 0)
# 这里就会报错，就是异常
```
**捕获异常**：
```python
try:
	表达式	# 将可能报错的语句放到这里
except [Exception] as e:	# 若上述语句报错，则会执行下面的语句
	表达式
finally:	# 无论是否有异常，最终都会执行
	表达式
```


```python
def my_sub(a, b):
	try:
		return a / b
	except ZeroDivisionError as e:
		print("分母不能为0")
		return None
	finally:
		print("function my_sub end")
if __name__ == '__main__': # 在当前脚本下执行下面表达式
	my_sub(1, 0)
# 结果：
# division by zero
# 分母不能为0
# function my_sub end
```

> *Exception*：所有异常的基类，所有的异常都是`Exception`的子类
> 尽量不要捕获基类Exception，尤其是数据处理的时候。因为Exception太宽了，无法正确处理异常
> 处理异常颗粒度要细一点

**常见的异常**：
1、`IndexError`：索引值超过了列表长度
```python
l = [1]
print(l[2])
```
2、`KeyError`：找不到key
```python
d = {"a":1}
print(d['b'])
```
3、`ValueError`：传入参数错误

```python
int('1')
int('a1')
```
4、`TypeError`：类型错误，常见于运算
```python
1 + '2'
```
5、`SyntaxError`：语法报错，检查自己的语法有没有写错
6、`IndentationError`：缩进错误（混用tab和space；缩进长度不对）

**如何处理异常**
1、处理：见上
2、抛出新异常：处理异常时，可以抛出新的异常`raise Exception("xxxx")`
```python
def my_sub(a, b):
	try:
		retrun a/b 
	except ZeroDivision as e:
		print("分母不能为0")
		raise Exception("params error")
	finally:
		print("function my_sub end")
```
3、重新抛出 `raise 异常`
```python
def my_sub(a, b):
	try:
		retrun a/b 
	except ZeroDivision:
		print("分母不能为0")
		raise ZeroDivision
	finally:
		print("function my_sub end")
```
4、忽略（不推荐）:`pass`用来指示当前处理语句没有正式写完，尽量不要忽略异常，否则代码的健壮度会很差，造成不可预知的bug
```python
def my_sub(a, b):
	try:
		retrun a/b 
	except ZeroDivision:
		pass
	finally:
		print("function my_sub end")
```
**自定义异常**
```python
class ParamsError(Exception): 
	pass
def my_sub(a, b):
	try:
		retrun a/b 
	except ZeroDivision:
		raise ParamsError("分母不可以为零")
	finally:
		print("function my_sub end")
```

## 3. 课后作业
1、用for循环和while循环来完成简单的计数
```python
def my_counter1(l):
    for i,e in enumerate(l):
        print(i+1)
def my_counter2(l):
    i = 1
    while i <= len(l):
        print(i)
        i += 1
def my_counter3(l):
    i = 1
    while True:
        if i > len(l):
            break
        print(i)
        i += 1   
if __name__ == '__main__':
    l = range(0,10)
    # my_counter1(l)
    # my_counter2(l)
    # my_counter3(l)
```
2、用for循环和while循环来实现斐波那契数列,，限制在100以内
斐波那契数列：第n项是n-1，n-2的和

```python
F(n) = F(n-1) + F(n-2)
[0,1,1,2,3,4,8,13,21...]
```
```python
def my_fn(n):
    l = []
    for i in range(0, n):
        if i == 0:
            l.append(0)
        elif i == 1:
            l.append(1)
        else:
            l.append(l[i-1] + l[i-2])
    return l

if __name__ == '__main__':
    l = my_fn(10)
    print(l)
```
3、在实现简单计算器的基础上，对参数进行检查，若报错则抛出自定义异常`ParamsError`
```python
class ParamsError(Exception):
    pass
def add(arg1, arg2):
    try:
        # return int(arg1) + int(arg2)
        return arg1 + arg2
    except ValueError:
        raise ParamsError("传入的参数错误")
    except TypeError:
        raise ParamsError("数据类型错误")
    finally:
        print("function add end")
if __name__ == '__main__':
    #print(add(1, 'a1'))
    print(add(1, '2'))
```
# 第6章 重学函数
## 1. 重新认识函数
**内置函数**：认识Python自带的，可全局调用的函数，避免我们命名冲突导致了函数性状发生改变
> 查看Python携带的内置函数
> ```python
> from pprint import pprint # 导入pprint库，可以格式化输出
> # 格式化输出的库
> pprint(dir(__builtins__))
>```

*常见的内置函数*
*六大基本数据类型转换*
1、`str`:`str(1.0)`,将数据类型转换为字符串格式
2、`int`:`int('1')`,将数据类型转换为整型格式
3、`float`:`float('1.0')`,将数据类型转换为浮点型格式
4、`bytes`:`bytes('a'.encode('utf-8'))`，将数据类型转换为二进制序列格式
5、`bool`:`bool('0')`(**True**)，`bool(0.0)`(False)
*四大基本数据结构转换*
1、`list`:只要是**序列**都可以转换成list，`list('qwe')`
2、`tuple`:只要是**序列**都可以转换成tuple（不可变的list），`tuple('qwe')`
3、`dict`:`dict(a=1)`，将其转换为dict
4、`set`:可以将序列化数据转换为set
```python
set('qweqwe') # {'q', 'w', 'e'}
set([1,2,2]) # {1, 2}
```
*其他*
1、`id`:查看内存地址
2、`dir`:查看当前对象下的所有方法和属性
> 在Python中一切皆为对象
> 查看Python的内置函数`dir(__builtins__)`

3、`max`:返回一个序列中的最大值，`max([1,3,5])`
4、`min`:返回一个序列中的最小值，`min([1,4,5])`
5、`range`:返回一组可迭代的数字对象
> ```python
> r = range(0, 100) # 获取[0, 100)（即[0,99]）的可迭代数字对象
> list(r) # 将其转换为列表
> for i in range(100) # 可以使用for来遍历可迭代对象 
> 	 print(i)
> ```
> `range`这个可迭代对象是可以索引的，**而**其他可迭代对象就不一定，`range(10)[0]`（只不过进行了优化）

> 在记忆时，记：*可迭代对象不可以索引*。这样避免不必要混淆。在此基础上，再考虑优化
> 如，python的常量池，还是记：*变量重新赋值后，内存地址将改变*

**函数的形参和实参**
*形参*:形式参数，简单地说，就是还没有接收到实际值的参数
```python
def my_power(a,b):	#a,b就是形参
	return a ** b
```
*实参*:实际传入的参数，函数调用时传入的值就是实参
```python
my_power(2,3) #2,3一旦被调用就是实参
```
**函数的返回值**
*返回值的类型*：在python中，类型可以是任意类型，包括函数本身
*如何接收返回值*：
> 1、接受单个值，`return a*b`
> 2、接受多个值，`retun a+b, a*b`，返回是一个`tuple`
> ```python
> def foo(a, b):
> 	retun a+b, a*b
> result = foo(2, 3) # result类型就是tuple
> # result = (5, 6)
> ```
> 3、多个变量按顺序接收，实现原理是**元组解包（unpack）**
> `a, b = foo(2, 3)`，相当于`a, b = (5, 6)`
> ```python
> a, b = foo(2, 3)
> # a = 5
> # b = 6
> ```
> 4、不定长变量接收，接收的是一个list
> ```python
> def foo()
> 	return 1,2,3,4,5,6
> a, *b, c = foo()
> # a = 1, c = 6
> # b = [2,3,4,5] 不定长参数是一个list
> ```

## 2. 匿名函数
顾名思义，匿名函数就是没有名字的函数，一般都是提供给高阶函数调用
1、通过`lambda`关键字来声明匿名函数
2、函数体是纯表达式
*1、不能有复杂的逻辑判断语句（如if等）*
> 唯一例外的例子:`lambda x: 返回值 if 纯表达式 else 返回值`
> ```python
> lambda x : True if x % 2 == 0 else False #判断是否为偶数
> ```

*2、不能有循环语句*
*3、不能有异常捕获*
*4、不能有赋值语句*
*5、不能有`return`关键字*

3、默认表达式运行的结果就是返回值
```python
lambda x: x**2 # 返回的是x^2，匿名函数对象
```

4、例子：嵌套list的特定元素排序
```python
l = [[1,2], [2,1], [6,4], [3,5]]
l.sort() #对于嵌套的list，sort默认第一个元素进行排序
#结果：l = [[1,2], [2,1],  [3,5], [6,4]]
l.sort(key = lambda x : x[1])	#令sort()第二个元素x[1]进行排序
#结果：l = [[2,1]， [1,2], [6,4], [3,5]]
```


## 3. 高阶函数






## 4. 递归函数






## 5. 课后作业