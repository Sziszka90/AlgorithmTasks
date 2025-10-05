"""
Problem
-------
Coin Change (minimum coins) — dynamic programming.

Given an array of distinct positive integers `coins` representing coin
denominations and an integer `amount`, return the fewest number of coins
that you need to make up that amount. If the amount cannot be made up by any
combination of the coins, return -1.

Example:
Input: coins = [1, 2, 5], amount = 11
Output: 3  # 11 = 5 + 5 + 1

Complexity (typical DP): O(n * amount) time, O(amount) extra space
"""

from typing import List


class Solution:
    """Template for the Coin Change (minimum coins) problem.

    The usual dynamic programming solution builds a dp table where dp[a] is
    the minimum coins to make amount a. This template intentionally leaves
    the method unimplemented so you can implement it yourself.
    """

    def coin_change(self, coins: List[int], amount: int) -> int:
        """Return the minimum number of coins to make `amount` or -1 if impossible.

        Args:
            coins: list of distinct positive coin denominations
            amount: target amount (>= 0)

        Returns:
            Minimum number of coins required to make `amount`, or -1 if not possible.
        """
        if amount < 0:
            return -1
        if amount == 0:
            return 0

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        return dp[amount] if dp[amount] <= amount else -1



if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print("Example input: coins=", coins, ", amount=", amount)
    print("Expected output: 3  # 11 = 5 + 5 + 1")
    result = Solution().coin_change(coins, amount)
    print("Result:", result)
