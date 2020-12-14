
# Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is
# not more than a given number ‘C’. Each item can only be selected once, which means either we put an item in the knapsack or we skip it.

def solve_knapsack(profit, weight, capacity):
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profit))]
    return knapsack(dp, profit, weight, capacity, 0)


def knapsack(dp, profit, weight, capacity, currentIndex):
    if capacity <= 0 or currentIndex >= len(profit):
        return 0
    if dp[currentIndex][capacity] != -1:
        return dp[currentIndex][capacity]
    profit1 = 0
    if weight[currentIndex] <= capacity:
        profit1 = profit[currentIndex] + knapsack(
            dp, profit, weight, capacity - weight[currentIndex],
            currentIndex + 1
        )
    profit2 = knapsack(
        dp, profit, weight, capacity, currentIndex + 1
    )

    dp[currentIndex][capacity] = max(profit1, profit2)
    return dp[currentIndex][capacity]


print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
