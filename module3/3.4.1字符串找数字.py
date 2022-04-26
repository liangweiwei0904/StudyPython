# string = 'My moral standing  is: 0.98765'
# 将其中的数字字符串转换成浮点数并输出。
# （提示：可以使用find()方法和字符串切片或split()方法，提取出字符串中冒号后面的部分，然后使用float函数，将提取出来的字符串转换为浮点数）
string = 'My moral standing  is: 0.98765'
pos = string.find(":")
print(pos)
print(string[pos+1:])
f = float(string[pos+1:])
print(type(f))
