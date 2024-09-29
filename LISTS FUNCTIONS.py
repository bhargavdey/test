lucky_numbers = [42, 8, 15, 16, 23, 4]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
print(friends)
friends.append("Cooper")#adds element at end of list
print(friends)
friends.insert(1, "Kelly")
print(friends)
friends.remove("Kevin")
print(friends)
friends.pop()#removes last element
print(friends)

friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friends.index("Kevin"))
print(friends.count("Jim"))

friends.sort()#array sorted alphbetically
print(friends)

lucky_numbers.sort()#sorts arrays in ascending order
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

friends.clear()
print(friends)