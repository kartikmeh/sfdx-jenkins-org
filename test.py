txt = "I/like/bananas"

x = txt.replace("/", "\\")
print(x)
index=x.rindex("\\")
substring=x[0:index]
print(substring)