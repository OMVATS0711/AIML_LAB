
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)


print("First Element:", my_list[0])
print("Last Element:", my_list[-1])


my_list[2] = 35
print("List after modifying the third element:", my_list)


my_list.append(60)  
print("List after appending 60:", my_list)


my_list.insert(2, 25)  
print("List after inserting 25 at index 2:", my_list)


my_list.remove(40)
print("List after removing 40:", my_list)


my_list.sort()
print("List after sorting:", my_list)


my_list.reverse()
print("List after reversing:", my_list)


print("Sliced list (first three elements):", my_list[:3])


print("Length of the list:", len(my_list))
