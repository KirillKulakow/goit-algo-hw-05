# Test alghorithms with timeit module

import timeit
from modules.algoRabinKarp import rabin_karp_search
from modules.algoBoyerMoore import boyer_moore_search
from modules.algoKnutMorrisPratt import knuth_morris_pratt_search


def test_algorithms():
    # Test with different text types and patterns
    test_cases = [
        {
            "name": "Large repeated text",
            "text": "ABABDABACDABABCABAB" * 1000,
            "pattern": "ABABCABAB",
            "iterations": 10
        },
        {
            "name": "Pattern at the end",
            "text": "A" * 10000 + "ABABCABAB",
            "pattern": "ABABCABAB",
            "iterations": 10
        },
        {
            "name": "Pattern not found",
            "text": "ABABDABACDABABCABAB" * 1000,
            "pattern": "XYXYXYXYX",
            "iterations": 10
        },
        {
            "name": "Long text, short pattern",
            "text": "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 1000,
            "pattern": "XYZ",
            "iterations": 10
        },
        {
            "name": "Long pattern",
            "text": "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 1000,
            "pattern": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "iterations": 10
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