class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while True:
            mid = self.split(nums, left, right)
            if mid == k - 1:
                return nums[mid]
            elif mid > k - 1:
                right = mid - 1
            else:
                left = mid + 1
        
    def split(self, nums, left, right):
        pivot = nums[left]
        i = left + 1
        j = right
        while i <= j:
            if nums[i] < pivot and nums[j] > pivot :
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            if nums[i] >= pivot:
                i += 1
            if nums[j] <= pivot:
                j -= 1
        nums[left], nums[j] = nums[j], nums[left]
        return j


test = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(test.findKthLargest(nums, k))
