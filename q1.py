import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob
    
    def age(self):
        dob = datetime.datetime.strptime(self.dob, "%d-%m-%Y")
        today = datetime.datetime.today()
        if today.month > dob.month or (today.month == dob.month and today.day >= dob.day):
            age = today.year - dob.year
        else:
            age = today.year - dob.year - 1
        return age

obj1 = Person("ABC", "India", "11-07-2003")
print("The age is", obj1.age())
