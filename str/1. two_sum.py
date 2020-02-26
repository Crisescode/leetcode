# https://leetcode-cn.com/problems/two-sum/
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# For example, Given nums = [2, 7, 11, 15], target = 9, return [0, 1], Because nums[0] + nums[1] = 2 + 7 = 9.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#


class Solution:
    # Time: o(n^2)
    # Space: o(1)
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution2:
    # Time:
    # Space:
    def twoSum(self, nums, target):
        pass


if __name__ == "__main__":
    solu_1 = Solution()
    result = solu_1.twoSum([2, 4, 1, 0, 5], 2)
    assert result == [0, 3]
    print(result)
