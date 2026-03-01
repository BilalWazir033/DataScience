num1=int(input("Enter number of subjects: "))
obtainedmarks=0
for i in range(num1):
    sub=float(input(f"Enter number for subject {i+1}: "))
    obtainedmarks+=sub
print("Obtained Marks: ",obtainedmarks)
totalmarks=100*num1
print("Total Marks: ",totalmarks)
average=float(obtainedmarks/totalmarks)*100
print("Average: ",average)
if average>=90:
    print("Grade: A")
elif average>=80:
    print("Grade: B")
elif average>=70:
    print("Grade: C")
elif average>=60:
    print("Grade: D")
else:
    print("Grade: F")