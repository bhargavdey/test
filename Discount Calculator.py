a = float(input("Enter purchase amount: "))
if a < 4000:
    print("Payable amount is " + str(a))
elif a >=4000 and a <8000:
    print("Payable amount is " + str(a - 0.05*a))
else:
    print("Payable amount is " + str(a - 0.1*a))