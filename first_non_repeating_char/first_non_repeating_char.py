def first_non_repeating(given_string):
    char_count = {}
    
    # Count the occurrences of each character in the given string
    for index, char in enumerate(given_string):
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    # Iterate through the given string to find the first non-repeating character
    for char in given_string:
        if char_count[char] == 1:
            return char  # Return the first non-repeating character found
    
    return None  # Return None if no non-repeating character is found

result = first_non_repeating("ababefg")
print(result)  # Output: 'e'