import random
print("โปรแกรมเป่ายิงฉุบ: ")
while True:
    game = random.choice(["ค้อน","กรรไกร","กระดาษ"])
    select = input("เลือก ค้อน กรรไกร กระดาษ \n คุณเลือก: ")
    if select == game:
        print("ผลลัพท์คือ เสมอ")
        print("--------------------------")
    elif select == "ค้อน" and game == "กรรไกร":
        print("ผลลัพท์คือ ชนะ")
        print("--------------------------")
    elif select == "กรรไกร" and game == "กระดาษ":
        print("ผลลัพท์คือ ชนะ")
        print("--------------------------")
    elif select == "กระดาษ" and game == "ค้อน":
        print("ผลลัพท์คือ ชนะ")
        print("--------------------------")
    else:
        print("ผลลัพท์คือ แพ้")
        print("--------------------------")