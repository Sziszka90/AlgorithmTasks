"""
Problem
-------
Count subarrays with sum less than or equal to k (sliding window).

Given a list of non-negative integers `nums` and an integer `k`, return the
number of contiguous subarrays whose sum is <= k.

Note: The standard sliding-window technique (two pointers) works when the
array contains only non-negative numbers because the window sum only increases
when the right pointer moves and only decreases when the left pointer moves.
For arrays with negative numbers a different approach is required.

Example:
Input: nums = [1, 1, 1], k = 2
Subarrays with sum <= 2: [1], [1], [1], [1,1], [1,1] => 5
Output: 5

Complexity: O(n) time, O(1) extra space (for non-negative arrays)
"""

from typing import List


class Solution:
    """Solution skeleton for counting subarrays with sum <= k.

    Implement using a sliding-window / two-pointer approach when `nums` are
    non-negative. This template intentionally leaves the method unimplemented
    so you can implement it yourself.
    """

    def count_subarrays_leq_k(self, nums: List[int], k: int) -> int:
        """Return the count of contiguous subarrays with sum <= k.

        Args:
            nums: list of non-negative integers
            k: integer threshold (>= 0)

        Returns:
            Number of contiguous subarrays whose sum is <= k.
        """
        """
        Problem
        -------
        Count subarrays with sum less than or equal to k (sliding window).

        Given a list of non-negative integers `nums` and an integer `k`, return the
        number of contiguous subarrays whose sum is <= k.

        Note: The standard sliding-window technique (two pointers) works when the
        array contains only non-negative numbers because the window sum only increases
        when the right pointer moves and only decreases when the left pointer moves.
        For arrays with negative numbers a different approach is required.

        Example:
        Input: nums = [1, 1, 1], k = 2
        Subarrays with sum <= 2: [1], [1], [1], [1,1], [1,1] => 5
        Output: 5

        Complexity: O(n) time, O(1) extra space (for non-negative arrays)
        """

        from typing import List


        class Solution:
            """Solution for counting subarrays with sum <= k using sliding window.

            This implementation assumes `nums` contains only non-negative integers.
            For arrays with negative numbers this method is not correct.
            """

            def count_subarrays_leq_k(self, nums: List[int], k: int) -> int:
                """Return the count of contiguous subarrays with sum <= k.

                Uses a two-pointer sliding window. For each right index `r`, we move
                the left pointer `l` until the window sum is <= k, then all subarrays
                that end at `r` and start between `l` and `r` are valid: (r - l + 1).

                Args:
                    nums: list of non-negative integers
                    k: integer threshold (>= 0)

                Returns:
                    Number of contiguous subarrays whose sum is <= k.
                """
                if k < 0:
                    return 0

                count = 0
                left = 0
                window_sum = 0

                for right, val in enumerate(nums):
                    window_sum += val

                    while left <= right and window_sum > k:
                        window_sum -= nums[left]
                        left += 1

                    count += (right - left + 1)

                return count


        if __name__ == "__main__":
            examples = [
                ( [1, 1, 1], 2 ),  # expected 5
                ( [7, 6, 5, 4, 3, 2, 1], 5 ),
            ]

            for nums, k in examples:
                result = Solution().count_subarrays_leq_k(nums, k)
                print(f"nums={nums}, k={k} -> count={result}")
