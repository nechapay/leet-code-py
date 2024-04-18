# Given an integer array nums of length n and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

def threeSumClosest(nums, target):
    if len(nums) < 3:
        return 2**31-1

    nums.sort()
    ans = sum(nums[:3])

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        cur_min_sum = nums[i] + nums[i+1] + nums[i+2]
        cur_max_sum = nums[i] + nums[-2] + nums[-1]
        if cur_min_sum >= target:
            if abs(cur_min_sum - target) < abs(ans-target):
                return cur_min_sum
            else:
                return ans
        if cur_max_sum < target:
            if abs(cur_max_sum - target) < abs(ans-target):
                ans = cur_max_sum
            continue

        # two pointer search
        low = i + 1
        hi = len(nums) - 1
        while low < hi:
            sm = nums[i]+nums[low]+nums[hi]
            if abs(sm - target) < abs(ans - target):
                ans = sm
            if sm == target:
                return sm
            elif sm < target:
                low += 1
            else:
                hi -= 1

    return ans


if __name__ == '__main__':
    print(threeSumClosest([-1, 2, 1, -4], 1))
