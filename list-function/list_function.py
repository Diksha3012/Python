lucky_numbers = [12,14,16,18,20]
friends = ["sourabh","neha","neha","dipti","sheetal","raghav"]
friends2 = friends.copy()
print(friends2)

print(friends.count("neha"))
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

print(friends.index("sourabh"))
friends.pop()           # pop the last element from the friends list
friends.append("Anket")
friends.insert(1,"Diksha")
friends.remove("dipti")
friends.pop()
#friends.clear()    "clears the whole frinds list
print(friends.index("sourabh"))

print(friends)

friends.extend(lucky_numbers)

print(friends)