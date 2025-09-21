# goit-algo-hw-05

## String Search Algorithm Analysis

Based on the performance tests of the three string search algorithms:

1. **Boyer-Moore** was the fastest algorithm in 4 out of 5 test cases:
   - Large repeated text: 0.021s
   - Pattern not found: 0.003s (significantly faster)
   - Long text with short pattern: 0.019s
   - Long pattern: 0.016s

2. **Knuth-Morris-Pratt (KMP)** was fastest in 1 test case:
   - Pattern at the end: 0.013s

3. **Rabin-Karp** was not the fastest in any test case, but performed consistently across different scenarios.

### Conclusion
Boyer-Moore generally shows the best performance, especially when patterns are not found or with longer texts. KMP can be more efficient in specific cases where the pattern appears near the end of the text.