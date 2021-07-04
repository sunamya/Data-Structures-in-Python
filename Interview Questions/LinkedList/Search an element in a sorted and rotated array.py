#Approach 1:Built-in Function
def search(self, nums: List[int], target: int) -> int:
        return(nums.index(target))

#Approach 2:
def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)
        mid=(l+h)//2
        if(l>h):
            return -1
        if nums[mid]==target:
            return mid
        if nums[l]<nums[mid]:
            if target>=nums[l] and target<=nums[mid]:
                return search(nums[l:mid-1],target)
            return search(nums[mid+1:h],target)
        if target>=nums[mid] and target<=nums[h]:
            return search(nums[mid+1:h],target)
        return search(nums[l:mid-1],target)