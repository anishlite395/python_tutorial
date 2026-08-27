print("="*30)
print("     GRADE CALCULATOR         ")
print("="*30)

marks = int(input("Enter the marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks")

elif marks >= 90:
    grade = 'A'
    print("Your grade is "+grade)

elif marks >= 80:
    grade = 'B'
    print("Your grade is "+grade)

elif marks >= 70:
    grade = 'C'
    print("Your grade is "+grade)

elif marks >= 60:
    grade = 'D'
    print("Your grade is "+grade)

elif marks < 60:
    grade = 'F'
    print("You Failed")





else:
    print("Invalid Marks")