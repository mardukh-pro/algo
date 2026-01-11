from ast import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lst = nums + nums
        return lst


lst = [1,2,3]


solution = Solution()
print(solution.getConcatenation(lst))