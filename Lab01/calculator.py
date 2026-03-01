#calculator:
num1=float(input("Enter a number:"))
num2=float(input("Enter a number:"))
operator=input("Enter Operator: +,-,*,/: ")
if operator=='+':
    add=num1+num2
    print("Addition: ",add)
elif operator=='-':
    sub=num1-num2
    print("Subtration: ",sub)
elif operator=='*':
    mul=num1*num2
    print("Multiplication: ",mul)
elif operator=='/':
    if num2<=0:
        print("Division by zero is not allowed")
    else:
        div=num1/num2
        div=round(div,1)
        print("Division: ",div)
else:
    
    print("Invalid operator!")