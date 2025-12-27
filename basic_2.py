import module1 as m
class student:
    def __init__(self,rno,name):
        self.rno=rno
        self.name=name

class test(student):
    def __init__(self,rno,name,m1,m2,m3):
        student.__init__(self,rno,name)
        self.m1=m1
        self.m2=m2
        self.m3=m3
class result(test):
    def __init__(self, rno, name, m1, m2, m3):
        super().__init__(rno, name, m1, m2, m3)
        self.total=0.0
        self.percentage=0.0
        self.grade=""
    def calculate(self):
        self.total=self.m1+self.m2+self.m3
        self.percentage=self.total/3
        if self.percentage>=75:
            self.grade= "A"
        elif self.percentage>=55:
            self.grade= "B"
        elif self.percentage>= 45:
            self.grade= "C"
        else:
            self.grade= "F"
    
    def dispaly(self):
        print(f'Rollno :- {self.rno}')
        print(f'Name of student is :- {self.name}')
        print(f'mark1 = {self.m1}\nmarks2 = {self.m2}\nmark3 = {self.m3}')
        print(f'total marks is = {self.total}')
        print(f'percentage occurs in the test :- {self.percentage}')
        print(f'Grade occur in exam :- {self.grade}')

s1=result(21,'Aniket Ambuskar',85,87,90)
m.printline('*')
print('\tSTUDENT INFO')
m.printline('*')
s1.calculate()
s1.dispaly()



# ANIKET SANDIP AMBUSKAR
# aniket23july@gamil.com, ambuskaraniket100@gamil.com
# 8010519461