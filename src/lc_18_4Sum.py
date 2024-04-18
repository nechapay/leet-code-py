# Given an array nums of n integers, return an array of all the unique
# quadruplets[nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

def fourSum(nums, target):
    def kSum(nums, target, k):
        res = []

        if not nums:
            return res

        avg = target // k
        if avg < nums[0] or nums[-1] < avg:
            return res

        if k == 2:
            return twoSum(nums, target)

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for subset in kSum(nums[i+1:], target - nums[i], k - 1):
                    res.append([nums[i]] + subset)

        return res

    def twoSum(nums, target):
        res = []
        low = 0
        hi = len(nums) - 1

        while low < hi:
            curr_sum = nums[low] + nums[hi]
            if curr_sum < target or (low > 0 and nums[low] == nums[low - 1]):
                low += 1
            elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[low], nums[hi]])
                low += 1
                hi -= 1

        return res

    if len(nums) < 4:
        return []

    nums.sort()
    return kSum(nums, target, 4)


if __name__ == '__main__':
    print(fourSum([1, 0, -1, 0, -2, 2], 0))
