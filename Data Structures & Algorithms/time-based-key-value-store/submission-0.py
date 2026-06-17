class TimeMap:

    def __init__(self):
        self.map = {} # { key : list of [value, timestamp] }

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map: # initialize every new key with empty list
            self.map[key] = []
        self.map[key].append([value, timestamp]) # append key's list with its value and timestamp

    def get(self, key: str, timestamp: int) -> str:
        res, value = '', self.map.get(key, []) # initialize res to empty string and value to its key's list 
        l, r = 0, len(value) - 1 # range of search is 0 to length of list

        while l <= r:
            mid = (l + r) // 2
            if value[mid][1] <= timestamp:
                res = value[mid][0] # if we found a timestamp smaller than requested, then we save it to res and move left pointer up
                l = mid + 1
            else: # else move right pointer down
                r = mid - 1
        return res # return res

