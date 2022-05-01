# 自定义函数move_substr(s, flag, n)，
# 将传入的字符串s按照flag（1代表循环左移，2代表循环右移）的要求左移或右移n位（例如对于字符串abcde12345，
# 循环左移两位后的结果为cde12345ab，循环右移两位后的结果为45abcde123），结果返回移动后的字符串，
# 若n超过字符串长度则结果返回-1。__main__模块中从键盘输入字符串、左移和右移标记以及移动的位数，
# 调用move_substr()函数若移动位数合理则将移动后的字符串输出，否则输出“the n is too large”。
def move_substr(s,flag,n):
    if n > len(s):
        print("移动长度不合法！the n is too large")
        return -1
    if flag == 1:
        print("循环左移",n,"位")
        s = s[n:]+s[:n]
        print(s)
    if flag == 2:
        print("循环右移",n,"位")
        s = s[-n:]+s[:-n]
        print(s)
s,flag,n=input("请输入字符串s，标志flag，距离n，以空格隔开").split(" ")
move_substr(s,int(flag),int(n))



# def moveSubstr(s, flag, n):
#     if n > len(s):
#         return -1
#     else:
#         if flag == 1:
#             return s[n:] + s[:n]
#         else:
#             return s[-n:] + s[:-n]
#
#
# if __name__ == "__main__":
#     s, flag, n = input("enter the 'string,flag,n': ").split(',')
#     result = moveSubstr(s, int(flag), int(n))
#     if result != -1:
#         print(result)
#     else:
#         print('the n is too large')