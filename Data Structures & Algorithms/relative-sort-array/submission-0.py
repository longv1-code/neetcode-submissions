class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        res = []
        state = [False] * len(arr1)
        r = 0
        for r in range(len(arr2)):
            for l in range(len(arr1)):
                if arr1[l] == arr2[r]:
                    res.append(arr1[l])
                    state[l] = True
        
        for i in range(len(state)):
            if not state[i]:
                res.append(arr1[i])

        return res