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
