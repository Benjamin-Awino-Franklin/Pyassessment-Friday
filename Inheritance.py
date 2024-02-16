class Staff():
    def __init__(self, name, position, age, salary):
        self.Name = name
        self.Position = position
        self.Age = age
        self.Salary = salary
    def display(self):
        print('My name is', self.Name,'I am a',self.Position,'I am', self.Age,'years old and my salary sums upto', self.Salary)
S1 = Staff('Newton Andrews,','Teacher',34,45000)

S1.display()

class Teacher(Staff):
    def __init__(self, name, position, age, salary,lessons_per_day):
        super().__init__(name, position, age, salary)
        self.lessons_per_day = lessons_per_day

    def display(self):
        print('My name is',self.Name,'I am a', self.Position, 'I am', self.Age,'years old and my salary sums upto', self.Salary,'I teach',self.lessons_per_day,'five lessons each day.')

T1 = Teacher('Newton Andrews,','Teacher',34,45000,5)
T2 = Teacher('Ben Carson,','Teacher',30,75000,3)

T1.display()
T2.display()


