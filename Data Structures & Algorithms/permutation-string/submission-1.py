class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        countS1 = collections.Counter(s1)
        countS2 = {}

        L = 0
        for R in range(len(s2)):
            countS2[s2[R]] = countS2.get(s2[R], 0) + 1
            if R - L + 1 >= len(s1):
                if countS1 == countS2:
                    return True
                
                countS2[s2[L]] -= 1
                if countS2[s2[L]] == 0:
                    del countS2[s2[L]]
                
                L += 1
    
        return False