list1 = [7, 2, 9]
list2 = [4, 1, 6]

# Create a single list that combines both lists and returns a sorted list in ascending order.

list_comb = list1 + list2 # [7,2,9,4,1,6]
list_comb.sort()

print(list_comb)