'''
password = int(input("Create password\n>>>>"))

confirm = int(input("Enter password\n>>>>"))

if password == confirm:
	print("Password match")
else:
	print("Password does not match")
'''

user_db = ["core", "tk", "mp"]
is_verified = True
user_name = str(input("Enter your name\n"))
if user_name in user_db:
	print("User exist")
	password = int(input("Create password\n>>>>"))
	confirm = int(input("Enter password\n>>>>"))
	if password == confirm:
		print("Login successful")
		if is_verified:
			print("Also is verified")
	else:
		print("Password does not match")

else:
	print("User does not exist")
