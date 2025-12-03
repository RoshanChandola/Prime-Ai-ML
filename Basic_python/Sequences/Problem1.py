"""problem statement
Given a list of tuples with infor(name ,subject)
list all unique subjects
list students enrolled in english subject
create dictionary (student ,set of subjects )"""
data = [("Alice", "Math"),
        ("Bob", "English"),
        ("Alice", "English"), 
        ("David", "Science"), 
        ("Bob", "Math")]
# list all unique subjects
unique_subjects = set()
for name, subject in data:
    unique_subjects.add(subject)    
print("Unique subjects:", unique_subjects)
print("-------------------")
# list students enrolled in english subject
for name, subject in data:
    if subject=="English":
        print(name)
print("-------------------")
# creating a dictionary (student ,set of subjects )
dict = {}
for name, subject in data:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(subject)
    else:
        dict[name].add(subject)
print(dict)
