class Solution:
    '''
    empty string -> "" -> [""]
    '''
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res # "hello world" -> "5#hello5#world"
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + length + 1])
            i = j + length + 1
        
        return res