# serpentine-solutions
My Python LeetCode solutions, organized by problem-solving pattern.

## Solutions

### 1. Two Sum

[View my Python solution](solutions/0001_two_sum.py)

I go through the list once and use a dictionary to remember the index of each number I have seen. For each number, I calculate the complement needed to reach the target. If that complement is already in the dictionary, I return its saved index and the current index. Otherwise, I save the current number and its index. If no pair is found, the code returns `[-1,-1]`.

**Time complexity:** O(n) on average, with constant-time dictionary lookups.  
**Space complexity:** O(n) for the dictionary.

### 2149. Rearrange Array Elements by Sign

[View my Python solution](solutions/2149_rearrange_array_elements_by_sign.py)

I make one pass through the array, collecting positive and negative numbers into separate lists in their original order. Then I write them back to `nums` alternately: a positive number at each even index and a negative number at the following odd index. Finally, I return the rearranged array.

**Time complexity:** O(n) for the two passes through the elements.  
**Space complexity:** O(n) for the positive and negative lists.

### 53. Maximum Subarray

[View my Python solution](solutions/0053_maximum_subarray.py)

I add each number to a running subarray sum and update the best sum before resetting a negative running sum to zero. This lets a new subarray start at the next number while still handling an array containing only negative numbers.

**Time complexity:** O(n).  
**Space complexity:** O(1).

### 485. Max Consecutive Ones

[View my Python solution](solutions/0485_max_consecutive_ones.py)

I move `right` through the array and count the current streak of ones. At a zero, I reset the streak and move `left` past that zero. I keep the largest streak seen.

**Time complexity:** O(n).  
**Space complexity:** O(1).

### 189. Rotate Array

[View my Python solution](solutions/0189_rotate_array.py)

I reduce `k` modulo the array length, reverse the whole array, then reverse the first `k` elements and the remaining elements separately. The three reversals rotate the array in place.

**Time complexity:** O(n).  
**Space complexity:** O(1).

### 125. Valid Palindrome

[View my Python solution](solutions/0125_valid_palindrome.py)

I use pointers at both ends, skip characters that are not letters or digits, and compare the remaining characters without case sensitivity. I return false at the first mismatch.

**Time complexity:** O(n).  
**Space complexity:** O(1).

### 14. Longest Common Prefix

[View my Python solution](solutions/0014_longest_common_prefix.py)

I check each character of the first string against the same position in every other string. I add it to the prefix only if all strings match there, and stop at the first mismatch or a shorter string.

**Time complexity:** O(mL + L²) in the worst case, where `m` is the number of strings and `L` is the first string's length; repeated Python string concatenation can copy the growing prefix.  
**Space complexity:** O(L) for the returned prefix.

### 88. Merge Sorted Array

[View my Python solution](solutions/0088_merge_sorted_array.py)

I compare the last unmerged elements of `nums1` and `nums2`, writing the larger one into the last open slot of `nums1`. When `nums1`'s original elements are exhausted, I copy any remaining elements of `nums2` into the front.

**Time complexity:** O(m + n).  
**Space complexity:** O(1).

### 507. Perfect Number

[View my Python solution](solutions/0507_perfect_number.py)

I start the divisor sum at 1, then check potential divisors only up to the square root of `num`. Whenever I find a divisor, I add it and its paired divisor, counting a square root only once. Finally, I compare the sum with `num`.

**Time complexity:** O(√n), where `n` is `num`.  
**Space complexity:** O(1).

### 387. First Unique Character in a String

[View my Python solution](solutions/0387_first_unique_character_in_a_string.py)

I first count how often each character appears using a dictionary. I scan the string again from left to right and return the first index whose character has a count of one. If there is none, I return -1.

**Time complexity:** O(n) on average, where `n` is the string length.  
**Space complexity:** O(u) for the dictionary, where `u` is the number of distinct characters (at most O(n)).
