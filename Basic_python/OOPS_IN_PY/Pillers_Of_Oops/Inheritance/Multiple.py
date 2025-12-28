class Employee:

    start_time="9 AM"
    end_time="5 PM"

class Teacher(Employee):
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
class AdminStaff(Employee):
    def __init__(self,name,department):
        self.name=name
        self.department=department
t1=Teacher("Roshan Chandola","Python")
print(t1.name)
print(t1.subject)
print(t1.start_time)
print(t1.end_time)
A1=AdminStaff("Amit Sharma","HR")
print(A1.name+" from "+A1.department+" department")
print("start time"+A1.start_time+" and end time is "+A1.end_time)    
