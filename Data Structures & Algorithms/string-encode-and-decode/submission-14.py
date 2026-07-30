class Solution:    
    def encode(self, strs: List[str]) -> str:
        return "".join([f"{word}ø" for word in strs])
    
    def decode(self, s: str) -> List[str]:
        return s.split("ø")[:-1]
        