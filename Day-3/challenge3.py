print("="*30)
print("       MOVIE TICKET           ")
print("="*30)

age = int(input("Enter your age: "))

if age < 5:
    print("Free")

elif 5 <= age < 13:
    print("₹100")

elif 13 <= age < 18:
    print("₹150")

elif age >= 18:
    print("₹200")

