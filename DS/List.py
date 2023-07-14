#LISTS
Friends = ["Kevin", "Mike",  "keren", "jim", "Anna", "Joseph", "Mike"] #LIST CREATION
print(Friends)
print(Friends[0])
print(Friends[-1])
print(Friends[1:])
Friends[1] = "Mike"
print(Friends)

#LIST FUNCTIONS
lucky_numbers = [4, 8, 15, 16, 23, 42]
Friends.append("Catherine")
Friends.insert(1, "Kelly")
Friends.remove("jim")
print("SORTED")
Friends.sort() #SORTING LIST
print(Friends)
lucky_numbers.sort()
print(lucky_numbers)
Friends.extend(lucky_numbers) #EXTENDING LIST
lucky_numbers.reverse()    #REVERSING LIST
print(lucky_numbers)
print(Friends)
Friends2 = Friends.copy()  #COPYING LIST
print(Friends2)
print(Friends.index("Anna"))
Friends.pop()
print(Friends)

print(Friends.count("Mike")) #COUNT OF A NAME IN THE LIST
Friends.clear()  #CLEAR A LST
print(Friends)

