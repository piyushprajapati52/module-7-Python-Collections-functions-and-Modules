# Original dictionary
student = {
    "name": "Mitesh",
    "age": 20,
    "course": "Python Backend"
}

# Update value at a specific key
student["name"] = "Piyush"

# Display updated dictionary
print("Updated Dictionary:")
for key, value in student.items():
    print(f"{key} : {value}")
