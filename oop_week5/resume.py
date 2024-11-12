num = int(input("จำนวนคนที่จะป้อน : "))
resume = {}
for i in range(1,num+1):
    print(f"กรุณากรอกคนที่ {i}")
    resume["name"] = str(input("กรุณากรอกชื่อ : "))
    resume["nickname"] = str(input("กรุณากรอกชื่อเล่น : "))
    resume["stdid"] = str(input("กรุณากรอกรหัสประจำตัวนักศึกษา : "))
    resume["hobby"] = str(input("กรุณากรอกงานอดิเรก : "))
    resume["color"] = str(input("กรุณากรอกสีที่ชอบ : "))
    print(resume)