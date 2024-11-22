import random

class Student:
    def __init__(self,ชื่อ,นามสกุล,ชื่อเล่น,):
        self.fristname = ชื่อ
        self.lastname = นามสกุล
        self.nickname = ชื่อเล่น
        self.score = random.randint(1,10)
        self.fixscore = random.randint(1,10)
    def checkScore(self):
        if self.score >= 5:
            print(f"{self.fristname} {self.lastname} \nชื่อเล่น {self.nickname} \nสอบได้ {self.score} คะแนน สอบผ่าน\n")
        else:
            print(f"{self.fristname} {self.lastname} \nชื่อเล่น {self.nickname} \nสอบได้ {self.score} คะแนน สอบไม่ผ่าน")
            print("----สอบแก้----")
            if self.fixscore >= 5:
                print(f"{self.fristname} {self.lastname} สอบแก้ได้ {self.fixscore} คะแนน \nคุณแก้สอบผ่าน\n")
            else:
                print(f"{self.fristname} {self.lastname} สอบแก้ได้ {self.fixscore} คะแนน \nคุณแก้สอบไม่ผ่าน\n")

student1 = Student("ปิติพงศ์","ภูมิพงค์","ปอน")
student2 = Student("เตชินท์","ศรีพุฒ","ไปรท์โหด")
student3 = Student("ชิติพัทธ์","โสขะรัตน์","ไนซ์")
student4 = Student("กมลศักธิ์","จิรังพันธ์","ออฟ")
student5 = Student("โยธินั้นท์","แป้นสุข","ก้อง")

student1.checkScore()
student2.checkScore()
student3.checkScore()
student4.checkScore()
student5.checkScore()