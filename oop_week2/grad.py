grad = int(input("ป้อนคะแนน: "))
if grad < 0 or grad > 100:
    print("โปรดกรอกคะแนน 0-100 เท่านั้น")
else:
    if grad >= 80:
        print("คุณได้เกรด 4")
    elif grad >= 70:
        print("คุณได้เกรด 3")
    elif grad >= 60:
        print("คุณได้เกรด 2")
    elif grad >= 50:
        print("คุณได้เกรด 1")
    else:
        print("คุณได้เกรด 0")
        solve = int(input("คุณจะสอบแก้หรือไม่ แก้พิมพ์ 1 ไม่แก้พิมพ์ 2: "))
        if solve == 1:
            print(f"คุณเหลือคะแนนอีก {50 - grad}")
        elif solve == 2:
            print("คุณสอบตก")
        else:
            print("กรุณาเลือก 1 หรือ 2 เท่านั้น")