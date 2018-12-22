class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1 or n == 0:
            return 0
        step = 0
        i = 0
        while i < n:
            step += 1
            if nums[i] + i >= n - 1:
                return step
            maxI = 0
            temp = 0
            for j in range(nums[i]):
                if maxI < nums[i + j + 1] + j:
                    maxI = nums[i + j + 1] + j
                    temp = j
            i += temp + 1
                
test = Solution()
nums = [2,3,1,1,4]
print(test.jump(nums))