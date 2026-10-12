# Grouping Anagrams

## Solution

```python
class Solution:  
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        res = defaultdict(list)

        for s in strs:  
            count = [0] * 26

            for c in s:  
                count[ord(c) - ord('a')] += 1  
            res[tuple(count)].append(s)

        return list(res.values())  
```  

We'll create a frequency map to represent this string.


``` python
       for s in strs:  
            count = [0] * 26  
```  
For every string `s`  in `strs`  We will create a character frequency count, `count` .

The next couple of steps are updating the frequency count.

Finally, add the frequency count to the result dict.   First, convert the list to a tuple, so that it can be hashed:  `tuple(count)` .  I think you may have check/add the key to the `result` as a list first.  

``` python 
hashable_count = tuple(count)

if hashable_count not in res:   
	res[hashable_count] = []

res[hashable_count].append(s)
```

We have now added one of the input string to the key in the result set.  If there are any other anagrams, they will get appended to this list, mapped to the same key.

Finally, we get can just get the values for `res` , for the `list` of `lists` .