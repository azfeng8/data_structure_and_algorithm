# 150 Leetcodes

The goal is to complete and study 150 problems and log progress.

The focus is on Leetcode easy/medium, but I will do a few hard ones.

Run `progress.py` to see how many easy/medium/hard have been done.

Each file in this folder, `{name of leetcode question}.py`, will have a comment at the top with difficulty "Easy", "Medium" or "Hard".

Labels:

- CODE PASS: code was accepted and successfully solves test cases.
- CODE FAIL: code fails some test cases.
- STUDYING: solutions under study.
- STUDY COMPLETE: code passing and top solutions have been studied.

Note: numbered files correspond to the Leetcode question number. Those were done before Summer 2024. This repository mainly includes Leetcode solutions from August 2024 and later to prepare for the the 2024-2025 hiring season.

# 8-18-2024: Day 5

#### top k frequent elements (med) - CODE PASS

#### Two Sum (easy) CODE PASS - STUDY COMPLETE

#### LRU Cache (med) STUDY COMPLETE
- Using Doubly-linked list with circular and sentinel extensions.

# 8-17-2024: Day 4

#### LRU Cache (med) CODE PASS
- Using array as a FIFO queue and hash table.

#### Happy number (easy) CODE PASS - Study 99% complete
- My solution uses hash set.
- Best solution uses Floyd's Slow/Fast pointer for cycle detection.
- To study proof of Floyd's algorithm correctness.

# 8-16-2024: Day 3

#### kth_smallest_pair_distance (Hard) Study 1/3 Complete
- Using bucket sort.
- To study binary search with DP algorithm.
- To study binary search with sliding window algorithm.

# 8-15-2024: Day 2

#### kth_largest_element_in_a_stream (Easy) Study Complete


# 8-14-2024: Day 1

#### kth_largest_element_in_a_stream (Easy) CODE PASS
- My solution: Using binary search.
- Best solution: Using heap.

First solution: - 1 hour
- Binary search for left neighbor element to insert.

#### kth_smallest_pair_distance (Hard) CODE FAIL
- Using slightly smarter brute force for O(N^2) time complexity.

First solution: - 45 minutes FAIL
18/19 test cases pass. Last one times out.
