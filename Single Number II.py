#Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
#
#Note:
#
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
#Example 1:
#
#Input: [2,2,3,2]
#Output: 3
#Example 2:
#
#Input: [0,1,0,1,0,1,99]
#Output: 99


class Solution(object):
    def singleNumber(self, nums):
        freq = {}
        
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in freq:
            if freq[i]==1:
                return i
        