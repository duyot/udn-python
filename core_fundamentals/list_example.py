

users = ["user1", "user2", "user3"]
print (users)
users.append("user4")
print (users)

users.insert(4,"user5")
print (users)

del users[0]
print (users)
users.reverse()
print (users)

print (len(users))

for user in users:
    print (user)

for i in range (1, 5):
    print (i)


numbers = [1,2,3,4,5]
print (f"Max number is {max(numbers)}")
print (f"Min number is {min(numbers)}")

x2Numbers = [value * 2 for value in numbers]
print (x2Numbers)

#slide a list
slicedNumbers = numbers[1:3]
print (slicedNumbers)