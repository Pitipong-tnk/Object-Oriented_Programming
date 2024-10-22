print("โปรแกรมหาพื้นที่สามเหลี่ยม")
base = int(input("ใส่ค่าฐาน: "))
height = int(input("ใสค่าสูง: "))
equal = 0.5 * base * height
print(f"ค่าพื้นที่ของสามเหลี่ยม = {equal}")

print("\nโปรแกรมหาพื้นที่สี่เหลี่ยม")
side = int(input("ใส่ค่าด้าน: "))
equal = side * side
print(f"ค่าพื้นที่ของสี่เหลี่ยม = {equal}")

print("\nโปรแกรมหาพื้นที่สี่เหลี่ยมผืนผ้า")
wide = int(input("ใส่ค่ากว้าง: "))
long = int(input("ใสค่ายาว: "))
equal = wide * long
print(f"ค่าพื้นที่ของสี่เหลี่ยมผืนผ้า = {equal}")

print("\nโปรแกรมหาพื้นวงกลม")
radius = int(input("ใส่ค่ารัศมี: "))
equal = 3.14 * radius * radius
print(f"ค่าพื้นที่ของวงกลม = {equal}")