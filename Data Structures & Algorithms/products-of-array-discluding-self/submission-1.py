class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zero_count = nums.count(0)
        result =[]

        if zero_count > 1:
            return [0] * len(nums)

        if zero_count == 1:
            nonzero_product = math.prod([x for x in nums if x != 0])

            for i in nums:
                if i == 0:
                    result.append(nonzero_product)
                else:
                    result.append(0)
        
            return result

        total_product = math.prod(nums)

        for i in nums:
            result.append(round(total_product / i))
            
        return result

        