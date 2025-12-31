x = float(input("Enter first no :"))
y = float(input("Enter second no :"))

op = input("Enter any opereater in which (+,-,/,*) :")



if op=="+":
    print("Your select + your answer is = ", x+y)
elif op=="-":
    print("Your select - your answer is = ", x-y)
elif op=="*":
    print("Your select * your answer is = ", x*y)
elif op=="/":
    print("Your select / your answer is = ", x/y)
else:
    print("Please select the correct opertaer.")


