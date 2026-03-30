class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}:{s}")
        return "".join(encoded)
            

    def decode(self, s: str) -> List[str]:
        decoded = []
        offset = 0
        length = 0
        while offset < len(s):
            i = offset
            while s[i] != ":":
                length = length * 10 + int(s[i])
                i+=1
            start = i+1
            end = start + length

            decoded.append(s[start:end])
            offset=end
            length = 0
        return decoded

                


