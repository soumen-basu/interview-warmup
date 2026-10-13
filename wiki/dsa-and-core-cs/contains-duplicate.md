# Contains duplicate

## Summary
The Contains Duplicate problem is the entry point to the NeetCode 150 Arrays & Hashing problem set. It evaluates candidate understanding of fundamental lookup time complexities, demonstrating how to trade auxiliary memory for algorithmic speed using hash sets to detect repeated elements in linear $O(N)$ time.

## Key points
- **Problem statement**: Given an integer array `nums`, return `True` if any value appears at least twice; return `False` if all elements are distinct.
- **Algorithmic trade-offs**:
  - *Brute force*: Nested loop comparison yielding $O(N^2)$ time and $O(1)$ space.
  - *Sorting*: In-place sort comparing adjacent neighbors yielding $O(N \log N)$ time and $O(1)$ auxiliary space.
  - *Hash set (Optimal)*: In-memory set tracking visited elements yielding $O(N)$ time and $O(N)$ space with early exit capability.
- **Python idiomatic solutions**: Can be implemented in a single pass with a `set` for early exit or as a concise length comparison `len(nums) != len(set(nums))`.

## Details

### Problem description and signature
Given an integer array `nums`, return `True` if any element is repeated:
```python
def containsDuplicate(nums: list[int]) -> bool:
    pass
```

### Approach 1: Hash set with early termination (Optimal)
Maintain a hash set of previously seen integers. As soon as an element is found that already exists in the set, return `True` immediately without processing the remaining elements:

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

### Approach 2: Length comparison (Concise Python)
Convert the list to a set and compare collection lengths:
```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
```
*Note*: While clean and concise, this always processes all $N$ elements and allocates memory for the entire set, foregoing early exit opportunities.

### Approach 3: In-place sorting (Space-optimized)
If auxiliary memory is strictly constrained ($O(1)$ space limit):
```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
```
- **Time complexity**: $O(N \log N)$ due to sorting.
- **Space complexity**: $O(1)$ or $O(N)$ depending on the sorting algorithm implementation (Python's Timsort uses $O(N)$ space worst case).

### Frequency maps vs. Hash sets
For simple duplicate existence, a hash set is superior because storing counts is unnecessary. When solving downstream problems (such as Top K Frequent Elements or Group Anagrams), frequency mapping with dictionary counters (`collections.Counter` or `defaultdict`) becomes necessary to record occurrences.

## Related
- [[Group anagrams]]
- [[DSA and core CS]]
- [[AI/ML engineer interview preparation]]

## References
- Source: NeetCode_ContainsDuplicate.md (NeetCode 150)
