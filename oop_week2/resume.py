name = input("โปรดกรอกชื่อ\n")
age = input("โปรดกรออกอายุ\n")
id = input("โปรดกรอกรหัสประจำตัวนักศึกษา\n")
yesr = input("โปรดกรอกชั้นปี\n")
nickname = input("โปรดกรอกชื่อเล่น\n")
height = float(input("โปรดกรอกส่วนสูง\n"))
weight = float(input("โปรดกรอกน้ำหนัก\n"))
sum = height + weight

print(" ชื่อ: " + name + " อายุ: " + age + " ปี ")
print(" รหัสประจำตัวนักศึกษา: " + id + " ระดับชั้น: " + yesr)
print(" ชื่อเล่น: " + nickname)
print(" ส่วนสูง: " + str(height) + " น้ำหนัก: " + str(weight))
print(" ส่วนสูง + น้ำหนัก = " + str(sum))