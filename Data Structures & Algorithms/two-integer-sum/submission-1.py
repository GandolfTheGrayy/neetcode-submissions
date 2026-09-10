class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        compliment = 0
        ans = []
        comp_map = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in comp_map:
                ans.append(comp_map[compliment])
                ans.append(i)
                return ans

            comp_map[nums[i]] = i
