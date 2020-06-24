#Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
#
#Example:
#
#Input: 3
#Output: 5
#Explanation:
#Given n = 3, there are a total of 5 unique BST's:
#
#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [-1] * (n+1)     # memo[i] is number of ways for i nodes
        return self.helper(n, memo)

    def helper(self, n, memo):
        if n <= 1:
            return 1    # 1 tree for n==0 (empty tree) and 1 tree for n==1

        if memo[n] != -1:
            return memo[n]

        count = 0
        for i in range(1, n+1):     # take each number 1...n as root
            # all numbers < i form left subtree, all > i form right subtree
            # multiply possibilities
            count += self.helper(i-1, memo) * self.helper(n-i, memo)
        memo[n] = count
        return count