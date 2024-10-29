sum = 0
while True:
    num = int(input("ใส่ค่า: "))
    if num != 0:
        sum += num
        print(f"ผลรวามตอนนี้ {sum}")
    else:
        print(f"ผลรวามตอนนี้ {sum}")
        print(f"ผลรวมทั้งหมด {sum}")
        break