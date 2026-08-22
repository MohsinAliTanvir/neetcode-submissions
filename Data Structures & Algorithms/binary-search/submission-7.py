class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first=0
        last=len(nums)-1
        
        found = False

        while first <= last and not found:
            mid = int((first +last)/2)
            print("mid", mid)
            current_num=nums[mid]

            if current_num==target:
                found = True
                return mid
            elif current_num > target:
                last = mid-1
            else:
                first = mid + 1
        
        if not found:
            return -1
        