'''27.
a = input("Enter a string: ")
b = input("Enter a substring: ")
occurence=0
for b in a:
    occurence+=1
print(occurence)
'''

'''28.
n = input("Enter a no: ")
if (int(n[0])**3 + int(n[1])**3 + int(n[2])**3)==int(n):
    print("Armstrong no")
else:
    print("Not armstrong no")
'''

num=1
for x in range(1,5):
    for y in range(1,x+1):
        print(str(num)+ " ", end="")
        num+=1
    print()