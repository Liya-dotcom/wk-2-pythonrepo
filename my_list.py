my_list = []
for num in [10, 20, 30, 40]:
    my_list.append(num) # Append numbers to the list
my_list.insert(1, 15)   # Insert 15 at index 1
my_list.extend([50, 60, 70])    # Extend the list with more numbers
my_list.remove(70)  # Remove 70 from the list
my_list.sort(reverse=False) # Sort the list in ascending order
print(my_list[3])   # Output: 30

print("Append:", my_list) # Output: [10, 15, 20, 30, 40, 50, 60]

