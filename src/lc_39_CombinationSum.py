# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

def combinationSum(candidates, target):
    ans = []

    def backtrack(remain, idx, path):
        if remain == 0:
            ans.append(path.copy())
            return
        if idx == len(candidates) or remain < 0:
            return

        path.append(candidates[idx])
        backtrack(remain - candidates[idx], idx, path)
        path.pop()

        backtrack(remain, idx + 1, path)
    backtrack(target, 0, [])
    return ans


def combinationSumDP(candidates, target):
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]

    for c in candidates:
        for t in range(c, target + 1):
            for comb in dp[t - c]:
                newComb = comb.copy()
                newComb.append(c)
                dp[t].append(newComb)

    print(dp)

    return dp[target]


if __name__ == '__main__':
    print(combinationSum([2, 3, 6, 7], 7))
    print(combinationSumDP([2, 3, 6, 7], 7))
