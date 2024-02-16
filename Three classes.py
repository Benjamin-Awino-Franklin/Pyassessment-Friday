class Person():
    def __init__(self, name, age, year_of_birth, gender):
        self.name = name
        self.age = age
        self.year_of_birth = year_of_birth
        self.gender = gender

    def display(self):
        print(self.name, self.age, self.year_of_birth, self.gender)

p1= Person('John', 26, 1997, 'Male')

p1.display()

class Employee():
    def __init__(self, name,position, year_of_birth, gender):
        self.name = name
        self.position = position
        self.year_of_birth = year_of_birth
        self.gender = gender

    def display1(self):
        print(self.name, self.position, self.year_of_birth, self.gender)

e1 = Employee('William', 'Cook', 1997, 'Male')

e1.display1()

class Student():
    def __init__(self, name, age, year_of_birth, gender):
        self.name = name
        self.age = age
        self.year_of_birth = year_of_birth
        self.gender = gender

    def display2(self):
        print(self.name, self.age, self.year_of_birth, self.gender)

s1 = Student('Ben', 26, 2005, 'Male')

s1.display2()

class personalinfo(Employee,Student):
    def __init__(self, name, position, year_of_birth, gender):
        super().__init__(name, position, year_of_birth,gender)

    def display3(self):
        print('My name is',self.name,'my position here is a', self.position, 'I was born on', self.year_of_birth,'I am a', self.gender)

i1 = personalinfo('John', 'student,', '2001.','Male')
i2 = personalinfo('Paul', 'teacher,', '1990.','Male')
i1.display3()
i2.display3()
