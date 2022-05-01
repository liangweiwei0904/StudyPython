with open("article.txt",mode="r+") as f:
    article = f.read()
print(article)
a = [",","?",".","...","!"]
article = article.replace("\n"," ")
for i in a:
    article = article.replace(i,"")
lst = article.split(" ")
print(lst)
clist = ""
count = 0
for item in lst:
    # clist.append(len(item))
    if len(item) > count:
        count = len(item)
        clist = item

print(clist)
#print(article[max(clist)])

