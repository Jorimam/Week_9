user_db = {
	"Jo":{
		"user_name": "Jo",
		"password": "pwd",
		"balance": 2000,
		"is_verified": True
		},
	}
	
verification_amount = 1500
action = input("""
+******************************+
|LOGIN AND REGISTRATION PORTAL |
| 1. Type 'l' to login	       |
| 2, Type 'r' to register      |
|			       |
+******************************+
"""
)
if action == "l":
	user_name = str(input("Enter user name\n"))
	if user_name in user_db:
		password = input("Enter password\n")
		if password == user_db[user_name]["password"]:
			print(f"Welcome {user_name}")
			print(user_db[user_name])
		else:
			print(f"Password does not match {user_name}")
	else:
		print("User does not exist! Register instead")
		
elif action == "r":
	user_name = str(input("Create user name\n"))
	if user_name in user_db:
		print("User Already exist")
		print("Choose login option or choose another user name")
	else:
		password = input("Create password\n")
		confirm_password = input("Confirm password\n")
		if confirm_password == password:
			available_balance = float(input("Enter availavle balance\n"))
			user = dict(
				username = user_name,
				password = password,
				available_balance = available_balance
				)
			user_db.update({user_name:user})
			user["is_verified"] = False
			print("User created successfully")
			print(user)
			print("Verification will cost 1500")
			verify = str(input("Do you wish to verify? yes or no\n"))
			if verify == "yes":
				if user["available_balance"] >= verification_amount:
					user["available_balance"] -= 1500
					user["is_verified"] = True
					print("Login successful")
					print(user)
					print(user_db)
				else:
					 print(f"Verfication costs: {verification_amount}")
					 print(f"You cannot be verified due to Insufficeint funds: {available_balance}")
					 print("Login successful")
					 print(user_db)
			elif verify == "no":
				print("Login successful")
				print(user)
				print(user_db)
			else:
				print("Invalid response")
		else:
			print("Password missmatch")
	
else:
	print("Error!")
	print("Kindly follow the given instructions")
