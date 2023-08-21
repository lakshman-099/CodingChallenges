def is_rotation(list1, list2):
    # Check if the lengths of the two lists are equal
    if len(list1) != len(list2):
        return False

    # Define the key element as the first element of the first list
    key = list1[0]
    key_index = -1

    # Search for the key element's index in the second list
    for i in range(len(list2)):
        if list2[i] == key:
            key_index = i
            break
    
    # If the key element is not found in the second list, return False
    if key_index == -1:
        return False
    
    # Check if the elements match when rotated
    for i in range(len(list1)):
        # Calculate the corresponding index in the second list using modular arithmetic
        j = (key_index + i) % len(list1)
        
        # Compare the elements at index i in list1 and index j in list2
        if list1[i] != list2[j]:
            return False
    
    # If all pairs of elements match, return True
    return True

print(is_rotation([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7, 1, 2, 3]))