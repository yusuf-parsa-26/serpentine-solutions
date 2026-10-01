class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        brackets = [""]*(n*2)

        def solve(idx,total):
            if idx >= len(brackets):
                if total == 0:
                    result.append("".join(brackets))
                return
            
            if total > len(brackets)//2:
                return
            elif total < 0:
                return
            
            brackets[idx] = "("
            Sum = total + 1
            solve(idx+1,Sum)
            brackets[idx] = ")"
            Sum = total - 1
            solve(idx+1,Sum)
        solve(0,0)
        return result
        
