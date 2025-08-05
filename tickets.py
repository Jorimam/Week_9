print("Enter your age\n")
age = int(input())
if age >= 18:
    print("You can buy a ticket")
    if age >= 60:
        print("Senior discount")
elif age >= 12 and age < 18:
    print("Teen ticket")
else:
    print("Kids ticket")
   
