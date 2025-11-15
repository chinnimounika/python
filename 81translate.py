#maketrans,translate
txt="abc def pdf def asdf"
mytable=txt.maketrans("def","1*2")
print(txt)
print(txt.translate(mytable))