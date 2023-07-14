def say_hi(name, age):
    print("Hello " + name + ", you are " + age)
say_hi("Mike","52")
say_hi("Steve","4")

#RETURN STATEMENT

def cube(num):
    return num*num*num

print(cube(3))
print(cube(4))
result = cube(5)
print(result)

def square(x):
    return x * x
for i in range(10):
    print(f"The square of {i} is {square(i)}")


