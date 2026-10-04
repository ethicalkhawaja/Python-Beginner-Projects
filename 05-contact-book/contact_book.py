contacts = {}

name = input("Enter contact name: ")
phone = input("Enter phone number: ")

contacts[name] = phone

print("Contact saved!")

print("Name:", name)
print("Phone:", contacts[name])
