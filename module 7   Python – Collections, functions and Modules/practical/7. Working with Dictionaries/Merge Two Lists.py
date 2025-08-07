# Merge Two Lists into a Dictionary Using a Loop


# Two lists
keys = ['name', 'age', 'city']
values = ['Piyush', 22, 'Ahmedabad']

# Create an empty dictionary
merged_dict = {}

# Use a loop to merge
for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

# Print the merged dictionary
print("Merged Dictionary:")
print(merged_dict)
