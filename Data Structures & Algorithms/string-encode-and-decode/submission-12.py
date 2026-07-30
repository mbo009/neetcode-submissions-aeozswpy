class Solution:
    def __init__(self):
        self.separator = "ø"
    
    def encode(self, strs: List[str]) -> str:
        return "".join([f"{word}{self.separator}" for word in strs])
    
    def decode(self, s: str) -> List[str]:
        return s.split(self.separator)[:-1]
        