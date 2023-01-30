class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        holder = 0
        if len(nums) == 1 and nums[0] == val:
            return 0
        if len(nums) == 0:
            return 0
        for seeker in range(len(nums)):
            if nums[holder] == val and nums[seeker] != nums[holder]:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder+=1
            elif nums[holder] != val:
                holder += 1
        return holder
