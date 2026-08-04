class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_count = {}
        arr2_set = set(arr2)
        end = []
        res = []

        for num in arr1:
            if num not in arr2_set:
                end.append(num)
            arr1_count[num] = 1 + arr1_count.get(num, 0)
        end.sort()

        for num in arr2:
            for _ in range(arr1_count[num]):
                res.append(num)

        return res + end