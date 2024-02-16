from datetime import date


class Person():
    def __init__(self, name, country, date_0f_birth):
        self.name = name
        self.country = country
        self.date_0f_birth = date_0f_birth
    def display(self):
        print('My name is ',self.name,'and I am from', self.country,'I was born on', self.date_0f_birth)
    def age(self):
        self.date_0f_birth = int(2024) - int(self.date_0f_birth)
        print(self.date_0f_birth)

p1= Person('Alferd williams','USA',2006)
p2= Person('Benjamin Franklin','Kenya',2005)

p1.age()