#Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
#Example 1:
#
#Input: n = 12
#Output: 3 
#Explanation: 12 = 4 + 4 + 4.
#Example 2:
#
#Input: n = 13
#Output: 2
#Explanation: 13 = 4 + 9.


class Solution(object):

    memo = [0, 1]   # memo is persistent so that calls to numSquares() build on previous results

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while len(self.memo) <= n:
            self.memo.append(1 + min(self.memo[-i*i] for i in range(1, int(len(self.memo)**0.5)+1)))

        return self.memo[n]