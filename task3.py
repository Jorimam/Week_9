student = {
    "name": "legolas",
    "has_registered": False,
    "has_paid": True,
    "has_internet": True
}

if student["has_registered"]:
    if student["has_paid"]:
        print("You can sit for exams")
        if student["has_internet"]:
            print("Allow access")
        else:
            print("check internet access")
    else:
        print("Pay fees")
else:
    print("Access denied")
