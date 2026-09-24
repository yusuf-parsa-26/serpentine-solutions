# serpentine-solutions
My Python LeetCode solutions, organized by problem-solving pattern.

## Solutions

### 1. Two Sum

[View my Python solution](solutions/0001_two_sum.py)

I go through the list once and use a dictionary to remember the index of each number I have seen. For each number, I calculate the complement needed to reach the target. If that complement is already in the dictionary, I return its saved index and the current index. Otherwise, I save the current number and its index. If no pair is found, the code returns `[-1,-1]`.

**Time complexity:** O(n) on average, with constant-time dictionary lookups.  
**Space complexity:** O(n) for the dictionary.
