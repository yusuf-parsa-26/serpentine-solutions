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

### 15. 3Sum

[View my Python solution](solutions/0015_3sum.py)

I sort the numbers, fix one number at a time, and use two pointers to find the other two. I move a pointer according to the sum and skip repeated values to avoid duplicate triplets.

**Time complexity:** O(n²), including sorting.  
**Space complexity:** O(n) auxiliary space for Python's in-place sort in the worst case; O(n²) including the returned triplets.

### 54. Spiral Matrix

[View my Python solution](solutions/0054_spiral_matrix.py)

I track the four boundaries of the unvisited area and read its top row, right column, bottom row, and left column. Then I move the boundaries inward and repeat.

**Time complexity:** O(mn), where `m` and `n` are the matrix dimensions.  
**Space complexity:** O(mn) for the returned list; O(1) auxiliary space beyond it.

### 48. Rotate Image

[View my Python solution](solutions/0048_rotate_image.py)

I transpose the square matrix by swapping cells across the main diagonal, then reverse each row to rotate it 90° clockwise in place.

**Time complexity:** O(n²) for an `n × n` matrix.  
**Space complexity:** O(1) auxiliary space.

### 128. Longest Consecutive Sequence

[View my Python solution](solutions/0128_longest_consecutive_sequence.py)

I put all numbers in a set. I start counting only from numbers with no predecessor, follow each consecutive run, and keep the longest length.

**Time complexity:** O(n) on average with hash-set lookups.  
**Space complexity:** O(n) for the set.

### 77. Combinations

[View my Python solution](solutions/0077_combinations.py)

I build combinations in increasing order, recurse from the next number, and undo each choice. When the combination reaches length `k`, I save a copy.

**Time complexity:** O(∑₍d=0₎ᵏ C(n,d) + k·C(n,k)), counting all explored partial combinations and result copies; C(a,b) is the binomial coefficient.  
**Space complexity:** O(k) auxiliary space; O(k·C(n,k)) including the results.

### 39. Combination Sum

[View my Python solution](solutions/0039_combination_sum.py)

I either include the current candidate and keep its index to allow reuse, or remove it and advance to the next candidate. I save a copy when the sum reaches the target and stop branches that exceed it.

**Time complexity:** O(C(m+D+1,m) + R·D) as a worst-case upper bound, where `m` is the candidate count, `D = floor(target / min(candidates))`, `R` is the number of results, and C(a,b) is the binomial coefficient.  
**Space complexity:** O(m+D) auxiliary space; O(m+D+R·D) including the results.

### 22. Generate Parentheses

[View my Python solution](solutions/0022_generate_parentheses.py)

I recursively fill a buffer with opening or closing brackets while tracking their balance. I prune negative balances or balances above `n`, and save complete strings only when the balance is zero.

**Time complexity:** O(n·Cₙ), where Cₙ = C(2n,n)/(n+1) is the nth Catalan number, including string construction.  
**Space complexity:** O(n) auxiliary space; O(n·Cₙ) including the results.

### 90. Subsets II

[View my Python solution](solutions/0090_subsets_ii.py)

I sort the numbers and explore including or excluding each value. After undoing an inclusion, I skip equal values before the exclusion branch to avoid duplicate subsets.

**Time complexity:** O(n·2ⁿ) in the worst case, including sorting and subset copies.  
**Space complexity:** O(n) auxiliary space; O(n·2ⁿ) including the results in the worst case.

### 78. Subsets

[View my Python solution](solutions/0078_subsets.py)

I explore including and excluding each number, undoing the inclusion before the exclusion branch. At the end of the array, I save a copy of the current subset.

**Time complexity:** O(n·2ⁿ), including subset copies.  
**Space complexity:** O(n) auxiliary space; O(n·2ⁿ) including the results.

### 206. Reverse Linked List

[View my Python solution](solutions/0206_reverse_linked_list.py)

I recursively reverse the rest of the list, point the next node back to the current node, and remove the old forward link. I return the new head.

**Time complexity:** O(n), where `n` is the number of nodes.  
**Space complexity:** O(n) for the recursion stack.

### 876. Middle of the Linked List

[View my Python solution](solutions/0876_middle_of_the_linked_list.py)

I move a slow pointer one node and a fast pointer two nodes at a time. When the fast pointer reaches the end, the slow pointer is at the middle, choosing the second middle for an even-length list.

**Time complexity:** O(n), where `n` is the number of nodes.  
**Space complexity:** O(1).

### 153. Find Minimum in Rotated Sorted Array

[View my Python solution](solutions/0153_find_minimum_in_rotated_sorted_array.py)

I compare the middle value with the rightmost value to identify the sorted half. I record the middle value as a possible minimum and continue searching the half that can contain a smaller value.

**Time complexity:** O(log n), where `n` is the array length.  
**Space complexity:** O(1).

### 81. Search in Rotated Sorted Array II

[View my Python solution](solutions/0081_search_in_rotated_sorted_array_ii.py)

I use binary search, identify a sorted half, and keep the half whose range can contain the target. If the left, middle, and right values are equal, I shrink both boundaries to handle duplicates.

**Time complexity:** O(n) in the worst case because duplicates can force one-step boundary reductions; O(log n) when each iteration can discard a half.  
**Space complexity:** O(1).

### 33. Search in Rotated Sorted Array

[View my Python solution](solutions/0033_search_in_rotated_sorted_array.py)

I identify which half is sorted, check whether the target lies within its range, and discard the other half. I return the matching index or -1.

**Time complexity:** O(log n), where `n` is the array length.  
**Space complexity:** O(1).

### 35. Search Insert Position

[View my Python solution](solutions/0035_search_insert_position.py)

I use binary search to find the first index whose value is at least the target. I save each possible position and search left; if none exists, I return the array length.

**Time complexity:** O(log n), where `n` is the array length.  
**Space complexity:** O(1).

### 18. 4Sum

[View my Python solution](solutions/0018_4sum.py)

I sort the array, fix two numbers, and use two pointers to find the remaining pair. I skip repeated values to avoid duplicate quadruplets.

**Time complexity:** O(n³), including sorting, where `n` is the array length.  
**Space complexity:** O(n) auxiliary space for Python's sort in the worst case; O(n + q) including `q` returned quadruplets.

### 704. Binary Search

[View my Python solution](solutions/0704_binary_search.py)

I compare the middle value with the target and discard the half that cannot contain it. I return the matching index or -1 when the search range is empty.

**Time complexity:** O(log n), where `n` is the array length.  
**Space complexity:** O(1).

### 867. Transpose Matrix

[View my Python solution](solutions/0867_transpose_matrix.py)

I create a new matrix with the row and column counts exchanged, then copy each value from position `[i][j]` to `[j][i]`.

**Time complexity:** O(mn), where `m` and `n` are the matrix dimensions.  
**Space complexity:** O(mn) for the returned matrix; O(1) auxiliary space beyond it.

### 73. Set Matrix Zeroes

[View my Python solution](solutions/0073_set_matrix_zeroes.py)

I first record the rows and columns containing original zeroes in two sets. In a second pass, I set every cell in those rows or columns to zero.

**Time complexity:** O(mn) on average with hash-set operations, where `m` and `n` are the matrix dimensions.  
**Space complexity:** O(m + n) for the row and column sets.

### 121. Best Time to Buy and Sell Stock

[View my Python solution](solutions/0121_best_time_to_buy_and_sell_stock.py)

I track the lowest buying price seen so far and update the best profit whenever a later price is higher. If no profitable trade exists, I return zero.

**Time complexity:** O(n), where `n` is the number of prices.  
**Space complexity:** O(1).

### 268. Missing Number

[View my Python solution](solutions/0268_missing_number.py)

I sort the numbers, check whether zero is missing, then scan for the first gap in the expected sequence. If there is no gap, I return the array length.

**Time complexity:** O(n log n) in the worst case, dominated by sorting.  
**Space complexity:** O(n) auxiliary space for Python's sort in the worst case.

### 283. Move Zeroes

[View my Python solution](solutions/0283_move_zeroes.py)

I collect nonzero values in their original order, copy them back to the front of the array, and fill the remaining positions with zeroes.

**Time complexity:** O(n), where `n` is the array length.  
**Space complexity:** O(n) in the worst case for the temporary list.

### 26. Remove Duplicates from Sorted Array

[View my Python solution](solutions/0026_remove_duplicates_from_sorted_array.py)

I use a set to remove duplicates, convert the unique values to a list, and sort them. I copy that list into the front of `nums` and return its length.

**Time complexity:** O(n + u log u) on average with hash-set operations, where `n` is the input length and `u` is the number of unique values.  
**Space complexity:** O(u) for the set, list, and sorting memory.

### 242. Valid Anagram

[View my Python solution](solutions/0242_valid_anagram.py)

I reject unequal lengths, count each string's character frequencies in separate dictionaries, and compare the dictionaries.

**Time complexity:** O(n) on average with dictionary operations for equal-length strings of length `n`; O(1) when their lengths differ.  
**Space complexity:** O(u) for distinct characters; O(1) under LeetCode's fixed lowercase English alphabet.

### 9. Palindrome Number

[View my Python solution](solutions/0009_palindrome_number.py)

I reject negative numbers, reverse the digits using remainder and integer division, and compare the reversed number with the original.

**Time complexity:** O(d), where `d` is the number of decimal digits, assuming constant-time bounded-integer arithmetic.  
**Space complexity:** O(1) under LeetCode's bounded-integer constraints.
