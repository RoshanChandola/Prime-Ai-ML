# FUNCTION WITH MIXED ARGUMENTS:
def create_profile(name, age, **kwargs):
    profile = {
        "name": name,
        "age": age
    }
    for key, value in kwargs.items():
        profile[key] = value
    return profile
user_profile = create_profile("Bob", 25, city="Los Angeles", profession="Engineer")
print(user_profile)