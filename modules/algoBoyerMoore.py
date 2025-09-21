# Create module with functionality of Boyer-Moore algorithm

def bad_character_heuristic(pattern_text):
    """Create the bad character heuristic table."""
    bad_char = {}
    for i in range(len(pattern_text)):
        bad_char[pattern_text[i]] = i
    return bad_char


def boyer_moore_search(text_search, pattern_text):
    """Perform the Boyer-Moore search algorithm.

    Returns:
        list: A list of indices where the pattern was found
    """
    matches = []
    len_pattern = len(pattern_text)
    len_text = len(text_search)
    bad_char = bad_character_heuristic(pattern_text)
    s = 0  # s is the shift of the pattern with respect to text
    while s <= len_text - len_pattern:
        j = len_pattern - 1
        while j >= 0 and pattern_text[j] == text_search[s + j]:
            j -= 1
        if j < 0:
            matches.append(s)
            s += (len_pattern - bad_char.get(text_search[s + len_pattern], -1)) if s + len_pattern < len_text else 1
        else:
            last_letter_idx = bad_char.get(text_search[s + j], -1)
            s += max(1, j - last_letter_idx)
    return matches

# Example usage:
if __name__ == "__main__":
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    result = boyer_moore_search(text, pattern)
    print(f"Pattern found at indices: {result}")
    # Output: Pattern found at indices: [0, 10]

    text2 = "AABAACAADAABAABA"
    pattern2 = "AABA"
    result2 = boyer_moore_search(text2, pattern2)
    print(f"Pattern found at indices: {result2}")
    # Output: Pattern found at indices: [0, 9, 12]

    text3 = "ABABDABACDABABCABAB"
    pattern3 = "ABABCABAB"
    result3 = boyer_moore_search(text3, pattern3)
    print(f"Pattern found at indices: {result3}")
    # Output: Pattern found at indices: [10]
