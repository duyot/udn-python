def add(a, b):
    return a + b


def greeting(name="world"):
    print (f"Hello {name.title()}!")


def greeting_user(user):
    print (f"Hello {user.name.title()}!")


def greeting_m(users):
    for user in users:
        greeting(user)

def greeting_m2(*users):
    for user in users:
        greeting(user)

def greeting_m3(**users):
    for user in users:
        greeting(user)

# print(add(1, 2))
users = ["duy", "hien", "hiếu"]
# greeting_m(users)
# greeting_m2("duy", "hien", "hiếu", "messi")

user1 = {"name": "duy"}
user2 = {"name": "hien"}
user3 = {"name": "hiếu"}
user4 = {"name": "messi"}

# greeting_m3(user1=user1, user2=user2, user3=user3, user4=user4)

# function that return values
def get_user():
    return "duy", 40

name, age = get_user()
print(name, age)



