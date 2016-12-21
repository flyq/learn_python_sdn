import itertools as itr
words = "1234"
r = itr.product(words, repeat=3)
dic = open("pass.txt","a")
for i in r:
    dic.write("".join(i))

dic.close()
