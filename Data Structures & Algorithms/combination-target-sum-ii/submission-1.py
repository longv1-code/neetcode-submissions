class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()
        def backtrack(start, total):
            if total == target:
                res.append(subset.copy())
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                total += candidates[i]
                backtrack(i + 1, total)

                subset.pop()
                total -= candidates[i]

        backtrack(0, 0)
        return res