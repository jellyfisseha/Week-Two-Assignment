# 1. Create an empty list
my_list = []
print("1. Empty list:", my_list)
# Output: []

# 2. Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("2. After appending 10, 20, 30, 40:", my_list)
# Output: [10, 20, 30, 40]

# 3. Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print("3. After inserting 15 at index 1:", my_list)
# Output: [10, 15, 20, 30, 40]

# 4. Extend with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print("4. After extending with [50, 60, 70]:", my_list)
# Output: [10, 15, 20, 30, 40, 50, 60, 70]

# 5. Remove the last element
my_list.pop()
print("5. After removing the last element:", my_list)
# Output: [10, 15, 20, 30, 40, 50, 60]

# 6. Sort in ascending order
my_list.sort()
print("6. After sorting in ascending order:", my_list)
# Output: [10, 15, 20, 30, 40, 50, 60]

# 7. Find and print the index of 30
index_of_30 = my_list.index(30)
print("7. Index of 30:", index_of_30)
# Output: 3
