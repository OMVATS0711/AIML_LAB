person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])


person["job"] = "Engineer"
print("\nUpdated dictionary with new key-value pair:", person)


person["age"] = 31
print("\nUpdated age:", person["age"])


if "city" in person:
    print("\n'city' key exists in the dictionary.")
else:
    print("\n'city' key does not exist in the dictionary.")

print("\nList of all keys:", list(person.keys()))
print("List of all values:", list(person.values()))
