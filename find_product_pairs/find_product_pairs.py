def find_product_pairs(nums:list,target:int):
    num_to_index={}  # Dictionary to store number-to-index mapping
    pairs=[]
    if len(nums)<2:
        return 'Invalid input' # Handle cases with too few numbers
    for i,num in enumerate(nums):
        if num !=0 and target % num == 0:
            complement=target//num
            if complement in num_to_index:
                pairs.append((num,complement))
        num_to_index[num]=i # Store the index of the number for future reference
    if not pairs:
        return 'No pairs found' # Handle the case where no pairs are found
    return pairs
print(find_product_pairs([2,2,3],6))