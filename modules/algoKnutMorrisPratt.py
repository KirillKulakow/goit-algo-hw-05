# Create module with functionality of Knuth-Morris-Pratt algorithm

def compute_lps_array(pattern_text):
    """Compute the Longest Prefix Suffix (LPS) array."""
    lps = [0] * len(pattern_text)
    length = 0  # length of the previous longest prefix suffix
    i = 1
    while i < len(pattern_text):
        if pattern_text[i] == pattern_text[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def knuth_morris_pratt_search(text_search, pattern_text):
    """
    Perform the Knuth-Morris-Pratt search algorithm.
    Returns a list of starting indices where the pattern is found in the text.
    """
    matches = []
    len_pattern = len(pattern_text)
    len_text = len(text_search)

    # Handle empty pattern or text edge cases
    if len_pattern == 0:
        return [i for i in range(len_text + 1)]
    if len_text == 0:
        return []

    lps = compute_lps_array(pattern_text)
    i = 0  # index for text_search
    j = 0  # index for pattern_text

    while i < len_text:
        # If characters match, advance both pointers
        if pattern_text[j] == text_search[i]:
            i += 1
            j += 1

        # If we've matched the entire pattern
        if j == len_pattern:
            matches.append(i - j)  # Add match position to results
            j = lps[j - 1]  # Look for the next match
        # If we have a mismatch after some matches
        elif i < len_text and pattern_text[j] != text_search[i]:
            if j != 0:
                j = lps[j - 1]  # Skip comparisons using LPS values
            else:
                i += 1

    return matches

# Example usage:
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    knuth_morris_pratt_search(text, pattern)
    # Output: Pattern found at index 10
    text2 = "THIS IS A TEST TEXT"
    pattern2 = "TEST"
    knuth_morris_pratt_search(text2, pattern2)
    # Output: Pattern found at index 10
    text3 = "AABAACAADAABAABA"
    pattern3 = "AABA"
    knuth_morris_pratt_search(text3, pattern3)
    # Output: Pattern found at index 0