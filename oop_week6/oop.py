class Cat:
    def __init__(self,ชื่อ,อายุ,สี,ความหิว):
        self.name = ชื่อ
        self.age = อายุ
        self.color = สี
        self.hungry = ความหิว
    def eat(salf,อาหาร):
        salf.hungry += อาหาร

cat1 = Cat(ชื่อ="ศรีทอง", อายุ=10, สี="ส้ม", ความหิว=5)
cat2 = Cat("ศรีเงิน", 8, "ขาว", 1)