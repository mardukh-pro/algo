from operator import indexOf
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        pass


nums = [2, 5, 1, 3, 4, 7]
n = 3
# --------------------------




arr1 = nums[:n]
arr2 = nums[n:]

res_list = []

for i in range(len(arr1)):
    res_list.append(arr1[i])
    res_list.append(arr2[i])


print(res_list)