class Solution:
    def __init__(self):
        self.separator = "#!"
    def encode(self, strs: List[str]) -> str:
        encoded = []

        for word in strs:
            encoded.append(self.separator)
            encoded.append(word)
        
        return "".join(encoded)
    
    def decode(self, s: str) -> List[str]:
        return s.split(self.separator)[1:]
        