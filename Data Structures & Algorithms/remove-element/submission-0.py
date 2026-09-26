class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valid_count=0
        L=0
        for R in range(len(nums)):
            if nums[R]!=val:
                nums[L]=nums[R]
                L+=1
                valid_count+=1
        return valid_count
        

        
        