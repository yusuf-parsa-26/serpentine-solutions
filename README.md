# serpentine-solutions

My Python LeetCode solutions, sorted by problem number. Each entry includes a summarized question, my approach, and time and space complexity.

## Index

| Number | Problem | Code |
|---:|---|---|
| 1 | [Two Sum](#1-two-sum) | [Python](solutions/0001_two_sum.py) |
| 9 | [Palindrome Number](#9-palindrome-number) | [Python](solutions/0009_palindrome_number.py) |
| 14 | [Longest Common Prefix](#14-longest-common-prefix) | [Python](solutions/0014_longest_common_prefix.py) |
| 15 | [3Sum](#15-3sum) | [Python](solutions/0015_3sum.py) |
| 18 | [4Sum](#18-4sum) | [Python](solutions/0018_4sum.py) |
| 22 | [Generate Parentheses](#22-generate-parentheses) | [Python](solutions/0022_generate_parentheses.py) |
| 26 | [Remove Duplicates from Sorted Array](#26-remove-duplicates-from-sorted-array) | [Python](solutions/0026_remove_duplicates_from_sorted_array.py) |
| 33 | [Search in Rotated Sorted Array](#33-search-in-rotated-sorted-array) | [Python](solutions/0033_search_in_rotated_sorted_array.py) |
| 35 | [Search Insert Position](#35-search-insert-position) | [Python](solutions/0035_search_insert_position.py) |
| 39 | [Combination Sum](#39-combination-sum) | [Python](solutions/0039_combination_sum.py) |
| 48 | [Rotate Image](#48-rotate-image) | [Python](solutions/0048_rotate_image.py) |
| 53 | [Maximum Subarray](#53-maximum-subarray) | [Python](solutions/0053_maximum_subarray.py) |
| 54 | [Spiral Matrix](#54-spiral-matrix) | [Python](solutions/0054_spiral_matrix.py) |
| 73 | [Set Matrix Zeroes](#73-set-matrix-zeroes) | [Python](solutions/0073_set_matrix_zeroes.py) |
| 77 | [Combinations](#77-combinations) | [Python](solutions/0077_combinations.py) |
| 78 | [Subsets](#78-subsets) | [Python](solutions/0078_subsets.py) |
| 81 | [Search in Rotated Sorted Array II](#81-search-in-rotated-sorted-array-ii) | [Python](solutions/0081_search_in_rotated_sorted_array_ii.py) |
| 88 | [Merge Sorted Array](#88-merge-sorted-array) | [Python](solutions/0088_merge_sorted_array.py) |
| 90 | [Subsets II](#90-subsets-ii) | [Python](solutions/0090_subsets_ii.py) |
| 121 | [Best Time to Buy and Sell Stock](#121-best-time-to-buy-and-sell-stock) | [Python](solutions/0121_best_time_to_buy_and_sell_stock.py) |
| 125 | [Valid Palindrome](#125-valid-palindrome) | [Python](solutions/0125_valid_palindrome.py) |
| 128 | [Longest Consecutive Sequence](#128-longest-consecutive-sequence) | [Python](solutions/0128_longest_consecutive_sequence.py) |
| 153 | [Find Minimum in Rotated Sorted Array](#153-find-minimum-in-rotated-sorted-array) | [Python](solutions/0153_find_minimum_in_rotated_sorted_array.py) |
| 189 | [Rotate Array](#189-rotate-array) | [Python](solutions/0189_rotate_array.py) |
| 206 | [Reverse Linked List](#206-reverse-linked-list) | [Python](solutions/0206_reverse_linked_list.py) |
| 242 | [Valid Anagram](#242-valid-anagram) | [Python](solutions/0242_valid_anagram.py) |
| 268 | [Missing Number](#268-missing-number) | [Python](solutions/0268_missing_number.py) |
| 283 | [Move Zeroes](#283-move-zeroes) | [Python](solutions/0283_move_zeroes.py) |
| 387 | [First Unique Character in a String](#387-first-unique-character-in-a-string) | [Python](solutions/0387_first_unique_character_in_a_string.py) |
| 485 | [Max Consecutive Ones](#485-max-consecutive-ones) | [Python](solutions/0485_max_consecutive_ones.py) |
| 507 | [Perfect Number](#507-perfect-number) | [Python](solutions/0507_perfect_number.py) |
| 704 | [Binary Search](#704-binary-search) | [Python](solutions/0704_binary_search.py) |
| 867 | [Transpose Matrix](#867-transpose-matrix) | [Python](solutions/0867_transpose_matrix.py) |
| 876 | [Middle of the Linked List](#876-middle-of-the-linked-list) | [Python](solutions/0876_middle_of_the_linked_list.py) |
| 2149 | [Rearrange Array Elements by Sign](#2149-rearrange-array-elements-by-sign) | [Python](solutions/2149_rearrange_array_elements_by_sign.py) |

## Solutions

### 1. Two Sum

[Original LeetCode question](https://leetcode.com/problems/two-sum/description/) · [View my Python solution](solutions/0001_two_sum.py)

**Question:** Given integer values in `nums` and a `target`, identify two different array positions whose values total the target. Return their indices in either order; exactly one valid pair is guaranteed.

**My approach:**

I go through the list once and use a dictionary to remember the index of each number I have seen. For each number, I calculate the complement needed to reach the target. If that complement is already in the dictionary, I return its saved index and the current index. Otherwise, I save the current number and its index. If no pair is found, the code returns `[-1,-1]`.

**Time complexity:** O(n) on average, with constant-time dictionary lookups.  
**Space complexity:** O(n) for the dictionary.

### 9. Palindrome Number

[Original LeetCode question](https://leetcode.com/problems/palindrome-number/description/) · [View my Python solution](solutions/0009_palindrome_number.py)

**Question:** Decide whether an integer `x` has the same decimal representation when read in either direction. Return a boolean; negative integers are not palindromes.

**My approach:**

I reject negative numbers, reverse the digits using remainder and integer division, and compare the reversed number with the original.

**Time complexity:** O(d), where `d` is the number of decimal digits, assuming constant-time bounded-integer arithmetic.  
**Space complexity:** O(1) under LeetCode's bounded-integer constraints.

### 14. Longest Common Prefix

[Original LeetCode question](https://leetcode.com/problems/longest-common-prefix/description/) · [View my Python solution](solutions/0014_longest_common_prefix.py)

**Question:** Find the longest sequence of starting characters shared by every string in `strs`. Return that prefix, or `""` when the strings share no starting characters.

**My approach:**

I check each character of the first string against the same position in every other string. I add it to the prefix only if all strings match there, and stop at the first mismatch or a shorter string.

**Time complexity:** O(mL + L²) in the worst case, where `m` is the number of strings and `L` is the first string's length; repeated Python string concatenation can copy the growing prefix.  
**Space complexity:** O(L) for the returned prefix.

### 15. 3Sum

[Original LeetCode question](https://leetcode.com/problems/3sum/description/) · [View my Python solution](solutions/0015_3sum.py)

**Question:** Find every distinct combination of three values in `nums` that totals zero. Each triplet must use three separate array positions, and equivalent triplets must appear only once; output order does not matter.

**My approach:**

I sort the numbers, fix one number at a time, and use two pointers to find the other two. I move a pointer according to the sum and skip repeated values to avoid duplicate triplets.

**Time complexity:** O(n²), including sorting.  
**Space complexity:** O(n) auxiliary space for Python's in-place sort in the worst case; O(n²) including the returned triplets.

### 18. 4Sum

[Original LeetCode question](https://leetcode.com/problems/4sum/description/) · [View my Python solution](solutions/0018_4sum.py)

**Question:** Find every distinct group of four values in `nums` whose sum equals `target`. Use four different indices for each group and return each value combination once, in any order.

**My approach:**

I sort the array, fix two numbers, and use two pointers to find the remaining pair. I skip repeated values to avoid duplicate quadruplets.

**Time complexity:** O(n³), including sorting, where `n` is the array length.  
**Space complexity:** O(n) auxiliary space for Python's sort in the worst case; O(n + q) including `q` returned quadruplets.

### 22. Generate Parentheses

[Original LeetCode question](https://leetcode.com/problems/generate-parentheses/description/) · [View my Python solution](solutions/0022_generate_parentheses.py)

**Question:** Produce every valid parentheses string using exactly `n` opening brackets and `n` closing brackets. Each string must be balanced and properly nested.

**My approach:**

I recursively fill a buffer with opening or closing brackets while tracking their balance. I prune negative balances or balances above `n`, and save complete strings only when the balance is zero.

**Time complexity:** O(n·Cₙ), where Cₙ = C(2n,n)/(n+1) is the nth Catalan number, including string construction.  
**Space complexity:** O(n) auxiliary space; O(n·Cₙ) including the results.

### 26. Remove Duplicates from Sorted Array

[Original LeetCode question](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/) · [View my Python solution](solutions/0026_remove_duplicates_from_sorted_array.py)

**Question:** For a non-decreasing integer array `nums`, remove repeated values in place and return the unique-value count `k`. Its first `k` positions must hold each distinct value once in sorted order; positions after that do not matter.

**My approach:**

I use a set to remove duplicates, convert the unique values to a list, and sort them. I copy that list into the front of `nums` and return its length.

**Time complexity:** O(n + u log u) on average with hash-set operations, where `n` is the input length and `u` is the number of unique values.  
**Space complexity:** O(u) for the set, list, and sorting memory.

### 33. Search in Rotated Sorted Array

[Original LeetCode question](https://leetcode.com/problems/search-in-rotated-sorted-array/description/) · [View my Python solution](solutions/0033_search_in_rotated_sorted_array.py)

**Question:** Search for `target` in an array of distinct integers that was sorted in ascending order and may have been rotated. Return the target's index, or -1 if absent, using O(log n) time.

**My approach:**

I identify which half is sorted, check whether the target lies within its range, and discard the other half. I return the matching index or -1.

**Time complexity:** O(log n), where `n` is the array length.  
**Space complexity:** O(1).

### 35. Search Insert Position

[Original LeetCode question](https://leetcode.com/problems/search-insert-position/description/) · [View my Python solution](solutions/0035_search_insert_position.py)

**Question:** In an ascending array of distinct integers, locate `target` or determine the position where it should be inserted to keep the array sorted. Return that index using O(log n) time.

**My approach:**

I use binary search to find the first index whose value is at least the target. I save each possible position and search left; if none exists, I return the array length.

**Time complexity:** O(log n), where `n` is the array length.  
**Space complexity:** O(1).

### 39. Combination Sum

[Original LeetCode question](https://leetcode.com/problems/combination-sum/description/) · [View my Python solution](solutions/0039_combination_sum.py)

**Question:** From distinct positive integers in `candidates`, produce every unique combination that totals `target`. A candidate may be reused any number of times; changing only the order of chosen values does not create a new combination.

**My approach:**

I either include the current candidate and keep its index to allow reuse, or remove it and advance to the next candidate. I save a copy when the sum reaches the target and stop branches that exceed it.

**Time complexity:** O(C(m+D+1,m) + R·D) as a worst-case upper bound, where `m` is the candidate count, `D = floor(target / min(candidates))`, `R` is the number of results, and C(a,b) is the binomial coefficient.  
**Space complexity:** O(m+D) auxiliary space; O(m+D+R·D) including the results.

### 48. Rotate Image

[Original LeetCode question](https://leetcode.com/problems/rotate-image/description/) · [View my Python solution](solutions/0048_rotate_image.py)

**Question:** Turn an `n × n` image matrix 90° clockwise by updating the supplied matrix in place. Perform the rotation without constructing another 2D matrix.

**My approach:**

I transpose the square matrix by swapping cells across the main diagonal, then reverse each row to rotate it 90° clockwise in place.

**Time complexity:** O(n²) for an `n × n` matrix.  
**Space complexity:** O(1) auxiliary space.

### 53. Maximum Subarray

[Original LeetCode question](https://leetcode.com/problems/maximum-subarray/description/) · [View my Python solution](solutions/0053_maximum_subarray.py)

**Question:** Among all non-empty contiguous portions of an integer array `nums`, find the greatest possible sum and return that sum.

**My approach:**

I add each number to a running subarray sum and update the best sum before resetting a negative running sum to zero. This lets a new subarray start at the next number while still handling an array containing only negative numbers.

**Time complexity:** O(n).  
**Space complexity:** O(1).

### 54. Spiral Matrix

[Original LeetCode question](https://leetcode.com/problems/spiral-matrix/description/) · [View my Python solution](solutions/0054_spiral_matrix.py)

**Question:** Return the values of an `m × n` matrix in a clockwise spiral, starting at the top-left corner and proceeding around successive inner layers. Include every cell exactly once.

**My approach:**

I track the four boundaries of the unvisited area and read its top row, right column, bottom row, and left column. Then I move the boundaries inward and repeat.

**Time complexity:** O(mn), where `m` and `n` are the matrix dimensions.  
**Space complexity:** O(mn) for the returned list; O(1) auxiliary space beyond it.

### 73. Set Matrix Zeroes

[Original LeetCode question](https://leetcode.com/problems/set-matrix-zeroes/description/) · [View my Python solution](solutions/0073_set_matrix_zeroes.py)

**Question:** Update an `m × n` matrix in place so that every row or column containing an original zero becomes entirely zero. Zeroes introduced during the update must not trigger additional rows or columns.

**My approach:**

I first record the rows and columns containing original zeroes in two sets. In a second pass, I set every cell in those rows or columns to zero.

**Time complexity:** O(mn) on average with hash-set operations, where `m` and `n` are the matrix dimensions.  
**Space complexity:** O(m + n) for the row and column sets.

### 77. Combinations

[Original LeetCode question](https://leetcode.com/problems/combinations/description/) · [View my Python solution](solutions/0077_combinations.py)

**Question:** List every selection of `k` distinct numbers from the integers 1 through `n`. Selections that differ only in ordering are the same combination; return each combination once, in any order.

**My approach:**

I build combinations in increasing order, recurse from the next number, and undo each choice. When the combination reaches length `k`, I save a copy.

**Time complexity:** O(∑₍d=0₎ᵏ C(n,d) + k·C(n,k)), counting all explored partial combinations and result copies; C(a,b) is the binomial coefficient.  
**Space complexity:** O(k) auxiliary space; O(k·C(n,k)) including the results.

### 78. Subsets

[Original LeetCode question](https://leetcode.com/problems/subsets/description/) · [View my Python solution](solutions/0078_subsets.py)

**Question:** For an array `nums` containing distinct integers, return its entire power set, including the empty subset and the full set. Every subset must appear once; output order is unrestricted.

**My approach:**

I explore including and excluding each number, undoing the inclusion before the exclusion branch. At the end of the array, I save a copy of the current subset.

**Time complexity:** O(n·2ⁿ), including subset copies.  
**Space complexity:** O(n) auxiliary space; O(n·2ⁿ) including the results.

### 81. Search in Rotated Sorted Array II

[Original LeetCode question](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/) · [View my Python solution](solutions/0081_search_in_rotated_sorted_array_ii.py)

**Question:** Determine whether `target` occurs in a rotated non-decreasing integer array that may contain repeated values. Return a boolean and avoid unnecessary search steps; duplicates can prevent a guaranteed logarithmic search.

**My approach:**

I use binary search, identify a sorted half, and keep the half whose range can contain the target. If the left, middle, and right values are equal, I shrink both boundaries to handle duplicates.

**Time complexity:** O(n) in the worst case because duplicates can force one-step boundary reductions; O(log n) when each iteration can discard a half.  
**Space complexity:** O(1).

### 88. Merge Sorted Array

[Original LeetCode question](https://leetcode.com/problems/merge-sorted-array/description/) · [View my Python solution](solutions/0088_merge_sorted_array.py)

**Question:** Merge the first `m` valid entries of sorted `nums1` with all `n` entries of sorted `nums2`. Store the non-decreasing merged sequence directly in `nums1`, whose last `n` slots are placeholders; do not return a new array.

**My approach:**

I compare the last unmerged elements of `nums1` and `nums2`, writing the larger one into the last open slot of `nums1`. When `nums1`'s original elements are exhausted, I copy any remaining elements of `nums2` into the front.

**Time complexity:** O(m + n).  
**Space complexity:** O(1).

### 90. Subsets II

[Original LeetCode question](https://leetcode.com/problems/subsets-ii/description/) · [View my Python solution](solutions/0090_subsets_ii.py)

**Question:** Produce all subsets of `nums`, which may contain repeated integers, including the empty subset. A subset may use a value up to its frequency in the input, but identical subsets must be returned only once.

**My approach:**

I sort the numbers and explore including or excluding each value. After undoing an inclusion, I skip equal values before the exclusion branch to avoid duplicate subsets.

**Time complexity:** O(n·2ⁿ) in the worst case, including sorting and subset copies.  
**Space complexity:** O(n) auxiliary space; O(n·2ⁿ) including the results in the worst case.

### 121. Best Time to Buy and Sell Stock

[Original LeetCode question](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/) · [View my Python solution](solutions/0121_best_time_to_buy_and_sell_stock.py)

**Question:** Using daily stock prices, find the largest profit from buying once and selling on a later day. Return zero if no profitable transaction is possible.

**My approach:**

I track the lowest buying price seen so far and update the best profit whenever a later price is higher. If no profitable trade exists, I return zero.

**Time complexity:** O(n), where `n` is the number of prices.  
**Space complexity:** O(1).

### 125. Valid Palindrome

[Original LeetCode question](https://leetcode.com/problems/valid-palindrome/description/) · [View my Python solution](solutions/0125_valid_palindrome.py)

**Question:** Determine whether a string reads identically in both directions when letter case is ignored and all characters except letters and digits are skipped. Return a boolean; an empty remaining sequence is valid.

**My approach:**

I use pointers at both ends, skip characters that are not letters or digits, and compare the remaining characters without case sensitivity. I return false at the first mismatch.

**Time complexity:** O(n).  
**Space complexity:** O(1).

### 128. Longest Consecutive Sequence

[Original LeetCode question](https://leetcode.com/problems/longest-consecutive-sequence/description/) · [View my Python solution](solutions/0128_longest_consecutive_sequence.py)

**Question:** From an unsorted integer array, find the greatest number of distinct values forming an uninterrupted run such as `a, a+1, a+2`. The values need not be adjacent in the array; return the length using O(n) time.

**My approach:**

I put all numbers in a set. I start counting only from numbers with no predecessor, follow each consecutive run, and keep the longest length.

**Time complexity:** O(n) on average with hash-set lookups.  
**Space complexity:** O(n) for the set.

### 153. Find Minimum in Rotated Sorted Array

[Original LeetCode question](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/) · [View my Python solution](solutions/0153_find_minimum_in_rotated_sorted_array.py)

**Question:** Find the smallest value in a non-empty array of distinct integers obtained by rotating an ascending sorted array. A full rotation may leave the array unchanged; the search must take O(log n) time.

**My approach:**

I compare the middle value with the rightmost value to identify the sorted half. I record the middle value as a possible minimum and continue searching the half that can contain a smaller value.

**Time complexity:** O(log n), where `n` is the array length.  
**Space complexity:** O(1).

### 189. Rotate Array

[Original LeetCode question](https://leetcode.com/problems/rotate-array/description/) · [View my Python solution](solutions/0189_rotate_array.py)

**Question:** Shift an integer array `nums` circularly to the right by a non-negative number of steps `k`. Values that move past the last position wrap around to the beginning.

**My approach:**

I reduce `k` modulo the array length, reverse the whole array, then reverse the first `k` elements and the remaining elements separately. The three reversals rotate the array in place.

**Time complexity:** O(n).  
**Space complexity:** O(1).

### 206. Reverse Linked List

[Original LeetCode question](https://leetcode.com/problems/reverse-linked-list/description/) · [View my Python solution](solutions/0206_reverse_linked_list.py)

**Question:** Given the head of a singly linked list, reverse the node order and return the new head. An empty input list remains empty.

**My approach:**

I recursively reverse the rest of the list, point the next node back to the current node, and remove the old forward link. I return the new head.

**Time complexity:** O(n), where `n` is the number of nodes.  
**Space complexity:** O(n) for the recursion stack.

### 242. Valid Anagram

[Original LeetCode question](https://leetcode.com/problems/valid-anagram/description/) · [View my Python solution](solutions/0242_valid_anagram.py)

**Question:** Check whether two lowercase English strings contain exactly the same characters with the same frequency, so one can be rearranged into the other. Return a boolean.

**My approach:**

I reject unequal lengths, count each string's character frequencies in separate dictionaries, and compare the dictionaries.

**Time complexity:** O(n) on average with dictionary operations for equal-length strings of length `n`; O(1) when their lengths differ.  
**Space complexity:** O(u) for distinct characters; O(1) under LeetCode's fixed lowercase English alphabet.

### 268. Missing Number

[Original LeetCode question](https://leetcode.com/problems/missing-number/description/) · [View my Python solution](solutions/0268_missing_number.py)

**Question:** An array of length `n` contains distinct integers drawn from 0 through `n`, with exactly one value absent. Return that missing value, including when it is 0 or `n`.

**My approach:**

I sort the numbers, check whether zero is missing, then scan for the first gap in the expected sequence. If there is no gap, I return the array length.

**Time complexity:** O(n log n) in the worst case, dominated by sorting.  
**Space complexity:** O(n) auxiliary space for Python's sort in the worst case.

### 283. Move Zeroes

[Original LeetCode question](https://leetcode.com/problems/move-zeroes/description/) · [View my Python solution](solutions/0283_move_zeroes.py)

**Question:** Modify `nums` in place to place every zero after all nonzero values, preserving the nonzero values' original relative order. The problem requires doing this without copying the array.

**My approach:**

I collect nonzero values in their original order, copy them back to the front of the array, and fill the remaining positions with zeroes.

**Time complexity:** O(n), where `n` is the array length.  
**Space complexity:** O(n) in the worst case for the temporary list.

### 387. First Unique Character in a String

[Original LeetCode question](https://leetcode.com/problems/first-unique-character-in-a-string/description/) · [View my Python solution](solutions/0387_first_unique_character_in_a_string.py)

**Question:** Find the earliest character in `s` that occurs exactly once in the entire string. Return its zero-based index, or -1 when every character repeats.

**My approach:**

I first count how often each character appears using a dictionary. I scan the string again from left to right and return the first index whose character has a count of one. If there is none, I return -1.

**Time complexity:** O(n) on average, where `n` is the string length.  
**Space complexity:** O(u) for the dictionary, where `u` is the number of distinct characters (at most O(n)).

### 485. Max Consecutive Ones

[Original LeetCode question](https://leetcode.com/problems/max-consecutive-ones/description/) · [View my Python solution](solutions/0485_max_consecutive_ones.py)

**Question:** For an array containing only zeroes and ones, return the length of its longest uninterrupted run of ones.

**My approach:**

I move `right` through the array and count the current streak of ones. At a zero, I reset the streak and move `left` past that zero. I keep the largest streak seen.

**Time complexity:** O(n).  
**Space complexity:** O(1).

### 507. Perfect Number

[Original LeetCode question](https://leetcode.com/problems/perfect-number/description/) · [View my Python solution](solutions/0507_perfect_number.py)

**Question:** Determine whether a positive integer equals the sum of all its positive divisors smaller than itself. Return a boolean; the number itself must be excluded from the sum.

**My approach:**

I start the divisor sum at 1, then check potential divisors only up to the square root of `num`. Whenever I find a divisor, I add it and its paired divisor, counting a square root only once. Finally, I compare the sum with `num`.

**Time complexity:** O(√n), where `n` is `num`.  
**Space complexity:** O(1).

### 704. Binary Search

[Original LeetCode question](https://leetcode.com/problems/binary-search/description/) · [View my Python solution](solutions/0704_binary_search.py)

**Question:** Locate `target` in an ascending sorted array of distinct integers. Return its index or -1 if it is missing, using an O(log n) search.

**My approach:**

I compare the middle value with the target and discard the half that cannot contain it. I return the matching index or -1 when the search range is empty.

**Time complexity:** O(log n), where `n` is the array length.  
**Space complexity:** O(1).

### 867. Transpose Matrix

[Original LeetCode question](https://leetcode.com/problems/transpose-matrix/description/) · [View my Python solution](solutions/0867_transpose_matrix.py)

**Question:** Return the transpose of a rectangular integer matrix: original rows become columns, and the value at `[i][j]` appears at `[j][i]`. An `m × n` input produces an `n × m` result.

**My approach:**

I create a new matrix with the row and column counts exchanged, then copy each value from position `[i][j]` to `[j][i]`.

**Time complexity:** O(mn), where `m` and `n` are the matrix dimensions.  
**Space complexity:** O(mn) for the returned matrix; O(1) auxiliary space beyond it.

### 876. Middle of the Linked List

[Original LeetCode question](https://leetcode.com/problems/middle-of-the-linked-list/description/) · [View my Python solution](solutions/0876_middle_of_the_linked_list.py)

**Question:** Return the middle node of a non-empty singly linked list. For an even number of nodes, choose the second of the two middle nodes.

**My approach:**

I move a slow pointer one node and a fast pointer two nodes at a time. When the fast pointer reaches the end, the slow pointer is at the middle, choosing the second middle for an even-length list.

**Time complexity:** O(n), where `n` is the number of nodes.  
**Space complexity:** O(1).

### 2149. Rearrange Array Elements by Sign

[Original LeetCode question](https://leetcode.com/problems/rearrange-array-elements-by-sign/description/) · [View my Python solution](solutions/2149_rearrange_array_elements_by_sign.py)

**Question:** An even-length array contains equal counts of positive and negative values and no zeroes. Return an arrangement that starts positive and alternates signs, while preserving the original relative order within each sign group.

**My approach:**

I make one pass through the array, collecting positive and negative numbers into separate lists in their original order. Then I write them back to `nums` alternately: a positive number at each even index and a negative number at the following odd index. Finally, I return the rearranged array.

**Time complexity:** O(n) for the two passes through the elements.  
**Space complexity:** O(n) for the positive and negative lists.
