def common_elements(array1,array2):
    common_elements_list = []
    for element in array2:
        # Check if the element is present in array1
        if element in array1:
            # If found, add it to the list of common elements
            common_elements_list.append(element)
    # Check if any common elements were found
    if common_elements_list:
        return common_elements_list
    return None
print(common_elements([0,1,2,4],[0,1,3,4,5,6]))