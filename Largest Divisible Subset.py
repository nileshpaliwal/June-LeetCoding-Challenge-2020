#Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
#
#Si % Sj = 0 or Sj % Si = 0.
#
#If there are multiple solutions, return any subset is fine.
#
#Example 1:
#
#Input: [1,2,3]
#Output: [1,2] (of course, [1,3] will also be ok)
#Example 2:
#
#Input: [1,2,4,8]
#Output: [1,2,4,8]


class Solution(object):
    def largestDivisibleSubset(self, nums):
        max_to_set = {-1 : set()}    
        nums.sort()

        for num in nums:

            num_set = set()         
            for max_in_s, s in max_to_set.items():
                if num % max_in_s == 0 and len(s) > len(num_set):
                    num_set = s

            max_to_set[num] = num_set | {num}    

        return list(max(max_to_set.values(), key = len))    

