class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        j = 0
        black_count = 0
        curr_min = float('inf')
        while i < len(blocks) and j < len(blocks):
            # print(i, j, black_count, curr_min, blocks[i: j + 1])
            if blocks[j] == "B":
                black_count += 1
            
            if j - i == (k - 1):
                curr_min = min(curr_min, k - black_count)
                if blocks[i] == "B":
                    black_count -= 1
                i += 1
            j += 1
        
        return curr_min