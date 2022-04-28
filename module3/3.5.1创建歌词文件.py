my_str = '''How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they're forever banned
The answer my friend is blowing in the wind
The answer is blowing in the wind'''


with open("Blowing in the wind.txt", mode='w') as f:
    f.write(my_str)
with open("Blowing in the wind.txt",mode="r+") as f1:
    # 直接插入会覆盖 f1.write("Blowin' in the wind\n")
    old = f1.read()
    f1.seek(0, 0)

    f1.write("Blowin' in the wind")
    f1.write(" - Bob Dylan\n")
    f1.write(old)
    f1.seek(0,2)
    f1.write("\n1962 by Warner Bros. Inc.")
with open("Blowing in the wind.txt",mode="r") as f3:
    my_lines = f3.readlines()
str_lrc = "".join(my_lines)
#print(my_lines)
print(str_lrc)

def insert_line(lines):
 lines.insert(0, "Blowin' in the wind\n")
 lines.insert(1, "Bob Dylan\n")
 lines.append("1962 by Warner Bros. Inc.")
 return ''.join(lines)
with open('Blowing in the wind1.txt', 'r+') as f:
 lines = f.readlines()
 string = insert_line(lines)
 # print(string)
 f.seek(0)
 f.write(string)