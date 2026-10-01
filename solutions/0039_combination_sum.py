class Solution:

    def solve(self,idx,total,subset,nums,target,result):
        if total == target:
            result.append(subset.copy())
            return
        elif total > target:
            return
        if idx >= len(nums):
            return
        Sum = total + nums[idx]
        subset.append(nums[idx])
        self.solve(idx,Sum,subset,nums,target,result)
        Sum = total
        subset.pop()
        self.solve(idx+1,Sum,subset,nums,target,result)
        
        
        
        
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        self.solve(0,0,[],candidates,target,result)
        return result
        
