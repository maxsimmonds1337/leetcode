class Solution:

    def isBadVersion(self, v):
        """
        :type v: int
        :rtype: bool
        """
        if(v<=83):
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
                
            if(self.isBadVersion(guess) == True): ## see if it's okay
                ## this means this one is bad, so the good is in the lower half of the array
                ## Check left, and see if it is bad, if it is, we've found it
                if(self.isBadVersion(guess-1) == False):
                    return guess-1
                else:
                    high = guess - 1
            else:
                ## this means it returned a good version, the bad is in the upper array
                low = guess + 1
        if(self.isBadVersion(guess) == True):
            return guess
        else:
            return -1

def main():
    solution = Solution()
    ans = solution.firstBadVersion(100)
    print(ans)

if __name__ == "__main__":
    main()