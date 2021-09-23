class Solution:

    def isBadVersion(self, v):
        """
        :type v: int
        :rtype: bool
        """
        if(v<=4):
            return False
        else:
            return True

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = range(1,n) ## Generate a list of nums, up to n
        high = n
        low = 0
       
        while(low != high & high > low):
            guess = nums[(high+low)//2] ## start in the middle
                
            if(isBadVersion(guess) == True): ## see if it's okay
                ## this means this one is bad, so the good is in the lower half of the array
                high = guess - 1
            else:
                ## this means it returned a good version, the bad is in the upper array
                low = guess + 1
        if(isBadVersion(guess) == True):
            return guess
        else:
            return -1

def main():
    solution = Solution()
    print(solution.isBadVersion(10))

if __name__ == "__main__":
    main()