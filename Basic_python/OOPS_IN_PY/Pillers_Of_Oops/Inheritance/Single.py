class Employee:

    start_time="9 AM"
    end_time="5 PM"

class Teacher(Employee):
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
t1=Teacher("Roshan Chandola","Python")
print(t1.name)
print(t1.subject)
print(t1.start_time)
print(t1.end_time)