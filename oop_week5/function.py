def no3(a,b):
    for i in range(a,b+1):
        if i % 3 != 0 :
            print(i)

def num(a):
    sum = 0
    gum = 0
    while True:
        if a > 0:
            sum += a
            print(sum)
        elif a < 0:
            gum += a
            print(gum)
        else:
            break
    return f"ผลรวมเลขบวก {sum}\nผลรวมเลขลบ {gum}"

