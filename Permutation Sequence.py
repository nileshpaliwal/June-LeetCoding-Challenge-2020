#The set [1,2,3,...,n] contains a total of n! unique permutations.
#
#By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
#
#"123"
#"132"
#"213"
#"231"
#"312"
#"321"
#Given n and k, return the kth permutation sequence.
#
#Note:
#
#Given n will be between 1 and 9 inclusive.
#Given k will be between 1 and n! inclusive.
#Example 1:
#
#Input: n = 3, k = 3
#Output: "213"
#Example 2:
#
#Input: n = 4, k = 9
#Output: "2314"

class Solution(object):
    def getPermutation(self, n, k):
        chars = [str(i) for i in range(1, n+1)]    
        permutations = factorial(n)              
        k -= 1                                  
        result = []

        while chars:
            digit = n * k // permutations       
            result.append(chars[digit])        
            del chars[digit]                   
            permutations //= n                      
            k -= digit * permutations
            n -= 1

        return "".join(result)

        """
        :type n: int
        :type k: int
        :rtype: str
        """
        