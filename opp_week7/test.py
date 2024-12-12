class Salaried:
    def __init__(self,ชื่อ,อาชีพ,เงินเดือน):
        self.name = ชื่อ
        self.occupation = อาชีพ
        self.salary = เงินเดือน
    def salaryOfYear(salf):
        return salf.salary * 12 

salaried1 = Salaried("โซเฟีย","ครู",12000)
salaried2 = Salaried("ปีเตอร์","หมอ",45000)
salaried3 = Salaried("บ็อบ","โปรแกรมเมอร์",40000)

print(f"{salaried1.name} ประกอบอาชีพ {salaried1.occupation} มีเงินเดือนทั้งปี = {salaried1.salaryOfYear()}")
print(f"{salaried2.name} ประกอบอาชีพ {salaried2.occupation} มีเงินเดือนทั้งปี = {salaried2.salaryOfYear()}")
print(f"{salaried3.name} ประกอบอาชีพ {salaried3.occupation} มีเงินเดือนทั้งปี = {salaried3.salaryOfYear()}")