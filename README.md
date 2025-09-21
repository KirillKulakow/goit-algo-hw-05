# goit-algo-hw-05

## String Search Algorithm Analysis

Based on the performance tests of the three string search algorithms:

1. **Boyer-Moore** was consistently the fastest algorithm in all test cases:
   - Short Text: 0.153477s
   - First Text (long): 0.898211s
   - Second Text: 0.044542s

2. **Knuth-Morris-Pratt (KMP)** showed moderate performance:
   - Short Text: 0.304219s
   - First Text (long): 6.457286s
   - Second Text: 0.287936s

3. **Rabin-Karp** was the slowest in all test cases:
   - Short Text: 0.291916s
   - First Text (long): 7.655416s
   - Second Text: 0.342471s

### Conclusion
Boyer-Moore consistently demonstrates superior performance across all tested text scenarios. The performance gap is particularly notable in longer texts, where Boyer-Moore is approximately 7-8 times faster than Rabin-Karp and KMP. This makes Boyer-Moore the recommended choice for general string searching applications.
