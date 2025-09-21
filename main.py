# Test alghorithms with timeit module

import timeit
from modules.algoRabinKarp import rabin_karp_search
from modules.algoBoyerMoore import boyer_moore_search
from modules.algoKnutMorrisPratt import knuth_morris_pratt_search


def test_algorithms():
    # Test with different text types and patterns
    # use text from ./text/...txt files
    # Open and read text files
    with open("./text/first.txt", "r", encoding="utf-8") as f:
        first_text = f.read()

    with open("./text/second.txt", "r", encoding="utf-8") as f:
        second_text = f.read()

    # Test cases based on text types
    test_cases = [
        {
            "name": "Short Text",
            "text": "ABABDABACDABABCABAB",
            "pattern": "ABABCABAB",
            "iterations": 100000
        },
        {
            "name": "First Text",
            "text": first_text,
            "pattern": "Реалізація",  # Adjust pattern as needed
            "iterations": 1000
        },
        {
            "name": "Second Text",
            "text": second_text,
            "pattern": "Реалізація",  # Adjust pattern as needed
            "iterations": 100
        }
    ]


    for case in test_cases:
        print(f"\n--- Testing with {case['name']} ---")
        text, pattern = case["text"], case["pattern"]
        iterations = case["iterations"]

        print("Testing Rabin-Karp Algorithm:")
        rk_time = timeit.timeit(lambda: rabin_karp_search(text, pattern), number=iterations)
        print(f"Rabin-Karp took {rk_time:.6f} seconds")

        print("\nTesting Boyer-Moore Algorithm:")
        bm_time = timeit.timeit(lambda: boyer_moore_search(text, pattern), number=iterations)
        print(f"Boyer-Moore took {bm_time:.6f} seconds")

        print("\nTesting Knuth-Morris-Pratt Algorithm:")
        kmp_time = timeit.timeit(lambda: knuth_morris_pratt_search(text, pattern), number=iterations)
        print(f"Knuth-Morris-Pratt took {kmp_time:.6f} seconds")

        # Determine the fastest algorithm
        times = {"Rabin-Karp": rk_time, "Boyer-Moore": bm_time, "KMP": kmp_time}
        fastest = min(times, key=times.get)
        print(f"\nFastest algorithm for this case: {fastest}")

if __name__ == "__main__":
    test_algorithms()