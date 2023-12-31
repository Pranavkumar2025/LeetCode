class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        # Reverse the entire array
        self.reverse(nums, 0, n - 1)
        
        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)
        
        # Reverse the remaining elements
        self.reverse(nums, k, n - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
