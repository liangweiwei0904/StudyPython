# 编程找出列表中不包含元音字母（包括大小写）和数字的所有单词并按原始先后顺序输出。
#
#   【测试数据与输出结果】
#
#     假设给定的字符串为（在程序中直接赋值）：
#
#     ['HELLO', 'PH', 'Hi', 'read', 'tmp123', 'Our', 'vmr']
#
#     输出：
#
#     PH
#
#     vmr
a = ['HELLO', 'PH', 'Hi', 'read', 'tmp123', 'Our', 'vmr']
# excep = ['A','a','E','e','I','i','O','o','U','u','1','2','3']
exceptstr = 'AEIOUaeiou0123456789'
t = list(exceptstr)
print(t)
for item in a:
    for i in item:
        count = 0
        if i in t:
            # print(item,"有元音或数字")
            count += 1
            break
    if count==0:

        print(item)


words = ['HELLO', 'PH', 'Hi', 'read', 'tmp123', 'Our', 'vmr']
for item in words:
    item_temp = item.lower()
    for ch in item_temp:
        if ch in 'aeiou' or ch in '0123456789':
            break
    else:
        print(item)