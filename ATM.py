balance = 10000
print("Enter amount you want to withdraw\n")
amount = float(input())

if amount <= balance and amount > 0:
	if amount % 1000 == 0:
		balance -= amount
		print(f"You have withdrawn ${amount} and your balance is {balance}")
	else:
		print("Can only dispense a thousand note")
elif amount > balance:
        print("Insufficient funds")
else:
	print("Invalid input")

