"""
You are helping a restaurant in Jos implement an automated discount system for their weekend promo.

The rules are:
1. Customers with a loyalty card get a 10% discount.,
2. If the customer's order amount is above 20,000 NGN:
3. Loyalty card holders get an additional 5% discount.,
4. Non-loyalty card holders get a free soft drink instead.,
,
Students (verified with student ID) get an extra 5% discount on top of whatever they qualify for.,

Customer data is stored in a dictionary like this:

customer = {
    "name": "Godiya",
    "order_amount": 25000,
    "loyalty_card": True,
    "is_student": False
}

Write a nested if-else block that:
Calculates the final discount or freebie for the customer.,
Stores the result in a dictionary called order_summary.,
Prints out a summary for the cashier.,
"""
customer = {
    "name": "Godiya",
    "order_amount": 25000,
    "loyalty_card": True,
    "is_student": False
}

amount = 20000
discount = 0
payable = 0
order_discount = 0
student_discount = 0
if customer["loyalty_card"] == True:
    discount = customer["order_amount"] * 0.1
    payable = customer["order_amount"] - discount
    if customer["order_amount"] > amount:
        order_discount = customer["order_amount"] * 0.05
        payable = customer["order_amount"] - discount - order_discount
        if customer["is_student"] == True:
            payable = customer["order_amount"] - discount - order_discount - student_discount


elif customer["loyalty_card"] == False and customer["order_amount"] > amount:
    discount = customer["order_amount"] * 0.1
    payable = customer["order_amount"] - discount
    
else:
    payable = customer["order_amount"] - discount
    print("You get a free drink")
customer.update({"Payable": payable})
print(customer)
