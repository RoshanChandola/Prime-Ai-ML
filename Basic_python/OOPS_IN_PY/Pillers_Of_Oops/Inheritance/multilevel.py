class Employee:
    start_time="9 AM"
    end_time="5 PM"
class AdminStaff(Employee):
    def __init__(self,role):
        self.role=role
class Accountant(AdminStaff):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary=salary
A1=Accountant(50000,"Finance")
print(A1.salary)
print(A1.role)
print(A1.start_time)
print(A1.end_time)
