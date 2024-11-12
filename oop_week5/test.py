a = int(input("ให้ป้อนกี่ตัว: "))
b = []
for i in range(a):
    c = int(input("ใสตัวเลข: "))
    b.append(c)
d = (sum(b)) // len(b)
print(d)