marks = {
    "Ram": 100,
    "Roshan" : 23,
    "Harry": 56,
    0: "Ram"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Ram":99,"Sita":100}) # Updates the dictionary
# print(marks)

print(marks["Ram2"]) # Returns an Error
print(marks.get("Ram2")) # Prints None