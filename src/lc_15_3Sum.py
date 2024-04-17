# Given an integer array nums, return all the triplets[nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def threeSum(nums):
    result = []
    if len(nums) < 3:
        return result

    nums.sort()

    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        low = i + 1
        hi = len(nums) - 1
        while low < hi:
            sum = nums[i]+nums[low]+nums[hi]
            if sum == 0:
                result.append([nums[i], nums[low], nums[hi]])
                last_low = nums[low]
                last_hi = nums[hi]
                while low < hi and nums[low] == last_low:
                    low += 1
                while low < hi and nums[hi] == last_hi:
                    hi -= 1

            elif sum > 0:
                hi -= 1
            else:
                low += 1

    return result


if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
