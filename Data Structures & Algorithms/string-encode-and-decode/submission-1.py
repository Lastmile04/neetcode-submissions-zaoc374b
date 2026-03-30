class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for str in strs:
            encoded.append(f"{len(str)}:{str}")
        return "".join(encoded)



    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        length = 0
        while i<len(s):
            while s[i] != ":":
                length = length * 10 + int(s[i])
                i+=1
            decoded.append(s[i+1:i+length+1])
            i = i+length+1
            length = 0
        return decoded
