# Create module with algorithm of Rabin-Karp

def rabin_karp_search(text_search, pattern_text, prime=101):
    """Perform the Rabin-Karp search algorithm."""
    len_pattern = len(pattern_text)
    len_text = len(text_search)
    if len_pattern == 0 or len_text == 0 or len_pattern > len_text:
        return []

    d = 256  # Number of characters in the input alphabet
    p = 0  # Hash value for pattern
    t = 0  # Hash value for text
    h = 1
    matches = []

    # The value of h would be "pow(d, len_pattern-1)%prime"
    for i in range(len_pattern - 1):
        h = (h * d) % prime

    # Calculate the hash value of pattern and first window of text
    for i in range(len_pattern):
        p = (d * p + ord(pattern_text[i])) % prime
        t = (d * t + ord(text_search[i])) % prime

    # Slide the pattern over text one by one
    for i in range(len_text - len_pattern + 1):
        # Check the hash values of the current window of text and pattern.
        if p == t:
            # Check for characters one by one
            if text_search[i:i + len_pattern] == pattern_text:
                matches.append(i)

        # Calculate hash value for next window of text: Remove leading digit,
        # add trailing digit
        if i < len_text - len_pattern:
            t = (d * (t - ord(text_search[i]) * h) + ord(text_search[i + len_pattern])) % prime

            # We might get negative value of t, converting it to positive
            if t < 0:
                t += prime

    return matches

# Example usage:
if __name__ == "__main__":
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    result = rabin_karp_search(text, pattern)
    print(f"Pattern found at indices: {result}")
    # Output: Pattern found at indices: [0, 10]

    text2 = "AABAACAADAABAABA"
    pattern2 = "AABA"
    result2 = rabin_karp_search(text2, pattern2)
    print(f"Pattern found at indices: {result2}")
    # Output: Pattern found at indices: [0, 9, 12]

    text3 = "ABABDABACDABABCABAB"
    pattern3 = "ABABCABAB"
    result3 = rabin_karp_search(text3, pattern3)
    print(f"Pattern found at indices: {result3}")
    # Output: Pattern found at indices: [10]