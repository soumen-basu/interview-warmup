# Group anagrams

## Summary
The Group Anagrams problem is a foundational algorithmic challenge from the NeetCode 150 Arrays & Hashing roadmap. The objective is to partition a list of strings such that words with identical character frequencies are grouped together, using frequency mapping and immutable tuple keys to achieve optimal $O(N \cdot K)$ time complexity.

## Key points
- **Problem statement**: Given an array of strings `strs`, group all anagrams together into sublists.
- **Categorization key strategy**: Anagrams share an identical character frequency distribution; mapping a normalized count representation to a list of matching words clusters anagrams in a single pass.
- **Optimal complexity**: Using a 26-element character count tuple as a dictionary key achieves $O(N \cdot K)$ time complexity, outperforming the $O(N \cdot K \log K)$ sorting approach (where $N$ is the number of strings and $K$ is the maximum string length).
- **Python hashing mechanics**: Lists are unhashable in Python dictionaries; converting count arrays to `tuple(count)` satisfies immutability requirements for dictionary keys.

## Details

### Problem description and signature
Given an array of strings `strs`, group the anagrams together in any order:
```python
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    pass
```

### Approach 1: Character count tuple hash (Optimal)
Rather than sorting each string, count the frequency of each lowercase English letter (`a` through `z`):
1. Initialize a hash map `res = defaultdict(list)`.
2. For each string `s`, construct a fixed-size 26-element list `count = [0] * 26`.
3. Compute the offset for each character `ord(c) - ord('a')` and increment the count.
4. Convert `count` to an immutable tuple `tuple(count)` to serve as the dictionary key.
5. Append `s` to `res[tuple(count)]`.
6. Return `list(res.values())`.

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())
```

### Approach 2: Sorted string key (Alternative)
An intuitive alternative sorts the characters of each string to produce a canonical representation:
- Key: `''.join(sorted(s))`
- Time complexity: $O(N \cdot K \log K)$
- Space complexity: $O(N \cdot K)$
While simpler to write, this approach incurs a $\log K$ penalty per string compared to the direct frequency count array.

### Complexity analysis
- **Time complexity**: $O(N \cdot K)$, where $N$ is the number of strings and $K$ is the maximum length of a string in `strs`. Constructing the count array takes $O(K)$ time for each of the $N$ strings.
- **Space complexity**: $O(N \cdot K)$ to store the grouped strings in the hash map, plus $O(26) = O(1)$ auxiliary space per string for the frequency table.

## Related
- [[Contains duplicate]]
- [[DSA and core CS]]
- [[AI/ML engineer interview preparation]]

## References
- Source: Grouping Anagrams.md (NeetCode 150)
