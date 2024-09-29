#except line can be used to do something if the original thing does not happen
#we can specify an except line as printing something according ot the error in the try portion
try:
    value = 10/0#try commenting this line
    number = int(input("Enter a number: "))#try entering anything except integer
    print(number)
except ZeroDivisionError as err:#ZeroDivisionError prints division by zero by default
    print(err)
except ValueError:
    print("Invalid input!")