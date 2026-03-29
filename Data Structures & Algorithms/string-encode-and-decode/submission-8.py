class Solution:
    def encode_str(self, string):
        encoded_str = ""
        key = 0

        for character in string:
            encoded_str += chr((ord(character) + key) % 256)
            key += 1

        return encoded_str
    
    def decode_str(self, string):
        decoded_str = ""
        key = 0

        for character in string:
            decoded_str += chr((ord(character) - key) % 256)
            key += 1

        return str(decoded_str)


    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + self.encode_str(s)
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(self.decode_str(s[j+1 : j+1+length]))
            i = j + 1 + length
        return res