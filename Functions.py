def say_hi():
    print("Hello User")

print("Top")
say_hi()
print("Bottom")

def say_hi2(name, age):#can put any number of parameters
    print("Hello " + name + ". You are " + str(age))

say_hi2("Mike", 15)
say_hi2("Anne", 17)