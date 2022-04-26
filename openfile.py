import os
# path = 'C:Users\\22495\Desktop\StudyPython'
for fname in os.listdir():
    print(fname)
    if fname.endswith('.py'):
        # 统计多少行
        # filepath = os.path.join(path,fname)
        # with open(filepath) as f:
        #     data = f.readlines()
        #     lens = len(data)
        #     print(filepath,"有",lens,"行代码")
        with open(fname,encoding='utf-8') as f :
            data = f.readlines()
            lens = len(data)
            print(fname, "有", lens, "行代码")