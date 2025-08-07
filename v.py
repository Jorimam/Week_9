user_db = {
	"jo": {
		"name": "jo",
		"age": 12
		}
	}
print(user_db)

name = str(input("Name"))
age = int(input("age"))
user = dict(name = name, age = age)
print(user)
user_db.update({user: user})
print(user_db)
