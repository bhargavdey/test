employee_file = open("employees.txt", "r")

print(employee_file.readable())
#print(employee_file.read())
#print(employee_file.readline())#this reads a line.
#print(employee_file.readline())#this reads the next line and so on
#print(employee_file.readlines())#this function puts the data of the file in an array/list
print(employee_file.readlines()[1])

employee_file.close()

#all reaading functions do not work together. thus some lines are commented above