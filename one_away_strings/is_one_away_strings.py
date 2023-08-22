"""
the following code determines whether two strings are one edit away from each other.
"""
def is_one_away(s1: str, s2: str) -> bool:
    # Check if the difference in lengths is too large to be one edit away
    if abs(len(s1) - len(s2)) >= 2:
        return False
    # If the lengths are the same, check for differences in characters
    elif len(s1) == len(s2):
        return is_one_away_same_length(s1, s2)
    # If s1 is longer than s2, check for differences in characters with different lengths
    elif len(s1) > len(s2):
        return is_one_away_diff_length(s1, s2)
    # If s2 is longer than s1, check for differences in characters with different lengths
    else:
        return is_one_away_diff_length(s2, s1)

def is_one_away_same_length(s1, s2):
    count_diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count_diff += 1
            if count_diff > 1:
                return False
    return True

def is_one_away_diff_length(s1, s2):
    i = 0
    count_diff = 0
    while i < len(s2):
        if s1[i + count_diff] == s2[i]:
            i += 1
        else:
            count_diff += 1
            if count_diff > 1:
                return False
    return True

print(is_one_away("abcde", "abc"))