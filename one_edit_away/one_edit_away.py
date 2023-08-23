def is_one_away(s1: str, s2: str) -> bool:
    """
    Checks if two strings are one edit away from each other.
    """

    # Check if the difference in lengths is too large to be one edit away
    if abs(len(s1) - len(s2)) > 1:
        return False

    # Initialize a counter to keep track of the number of edits
    edit_count = 0

    # Iterate over the characters in both strings
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            # If the characters are different, increment the edit count
            edit_count += 1
            # If the edit count is greater than 1, the strings are not one edit away
            if edit_count > 1:
                return False

    # If the edit count is 0 or 1, the strings are one edit away
    return edit_count <= 1

print(is_one_away("abcde", "abcd"))