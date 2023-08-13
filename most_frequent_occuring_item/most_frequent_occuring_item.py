def most_frequent(array:list)->int:
     # Initialize variables to track the most frequent item and its count
    max_count,max_item=0,None
    # Create a dictionary to store occurrences of items in the array
    occurrances={}
    for item in array:
        if item in occurrances:
            # Increment the count for the current item
            occurrances[item]+=1
             # Update max_count and max_item if the current item's count is higher
            if occurrances[item]>max_count:
                max_count=occurrances[item]
                max_item=item
        else:
            occurrances[item]=1
    return max_item
print(most_frequent([1,2,1,3,4,5,1]))