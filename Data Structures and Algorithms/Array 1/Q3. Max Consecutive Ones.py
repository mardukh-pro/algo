from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0
        for n in nums:
            if n == 1:
                current_count += 1
                if current_count > max_count:
                    max_count = current_count
            else:
                current_count = 0
        return max_count


solution = Solution()

numbers1 = [1, 1, 0, 1, 1, 1]
print(solution.findMaxConsecutiveOnes(numbers1))
