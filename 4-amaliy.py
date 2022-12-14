n = int(input("n>>>"))
s=1
c=1
for n in range(n):
    s+=0.1
    c *= s
print(c)