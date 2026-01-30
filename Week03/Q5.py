monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")

print("Monday class:", monday_class)
print("Wednesday class:", wednesday_class)

both_classes = monday_class & wednesday_class
print("Attended both classes:", both_classes)

all_students = monday_class | wednesday_class
print("Attended either class:", all_students)

only_monday = monday_class - wednesday_class
print("Only Monday:", only_monday)

only_one = monday_class ^ wednesday_class
print("Only one class (not both):", only_one)

print("Is Monday subset of all students?", monday_class <= all_students)

print()

print("=" * 50)
print("Question 5: Contact Book")
print("=" * 50)

contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

print("Alice's number:", contacts["Alice"])

contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)

contacts["Bob"] = "555-0000"
print("Contacts after updating Bob:", contacts)

del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)

print("All names:", contacts.keys())

print("All numbers:", contacts.values())

print("Total contacts:", len(contacts))

print()

print("=" * 50)
print("Question 6: Inventory Management System")
print("=" * 50)

inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}

print("=== Current Inventory ===")
for product, details in inventory.items():
    price = details[0]
    quantity = details[1]
    print(product + " - Price: $" + str(price) + ", Quantity: " + str(quantity))

print()

electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}

all_products = electronics | accessories
print("All product categories:", all_products)

print()

prices = []
for product in inventory:
    price = inventory[product][0]
    prices.append(price)
print("Price list:", prices)

prices.sort()
print("Sorted prices:", prices)
print("Lowest price: $" + str(prices[0]))
print("Highest price: $" + str(prices[-1]))

print()

inventory["Headphones"] = (49.99, 20)

mouse_price = inventory["Mouse"][0]
inventory["Mouse"] = (mouse_price, 12)

del inventory["Monitor"]

print("=== Final Inventory ===")
for product, details in inventory.items():
    price = details[0]
    quantity = details[1]
    print(product + " - Price: $" + str(price) + ", Quantity: " + str(quantity))