# NeetCode 150 - Contains Duplicate

Source: https://neetcode.io/problems/duplicate-integer/question?list=neetcode150

## Problem: Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

## Hints

* Compare every element in one string with every other element in the other string.
* Optimize by sorting the arrays.  What is the runtime? Can we improve?
* How do you improve an O(n.logn) runtime?   You typically need O(n) to loop over element, so any operation would have to be O(1).  What operations are fixed cost (  O(1)  )?
* When dealing with anagrams, frequency maps are useful.




## Freqency Maps

You can either have a list of 26 ints, and keep incrementing the count for each character as they are found.

Alternatively, have a map of characters to counts, and then increment the count for each character as they are found.
    One problem is that you can't increment a frequency if it doesn't already exist.  You can try:

    ``` python

        if char not in freq_map:
            freq_map[char] = 0
        freq_map[char] += 1

    ```
    