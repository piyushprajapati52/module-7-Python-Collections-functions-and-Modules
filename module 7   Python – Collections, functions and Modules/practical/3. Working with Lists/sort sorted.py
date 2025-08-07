# Original list


number = [5,2,6,4,8,9]


# Using sorted() - returns a new sorted list (original list remains unchanged)

sorted_number = sorted(number)
print("Using sorted:", sorted_number)
print("Original list after sorted:", number)

# Using sort() - sorts the list in-place (modifies the original list)
number.sort()
number.sort()
print("Using sort:", number)