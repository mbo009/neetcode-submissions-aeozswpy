class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        prefix = [0] * len(height)
        max_prefix = 0
        sufix = [0] * len(height)
        max_sufix = 0

        for i in range(1, len(height)):
            prefix[i] = max(max_prefix, height[i - 1])
            if prefix[i] > max_prefix:
                max_prefix = prefix[i]

        for i in range(len(height) - 2, 0, -1):
            sufix[i] = max(max_sufix, height[i + 1])
            if sufix[i] > max_sufix:
                max_sufix = sufix[i]
        
        print(prefix, sufix)
        return sum(max(min(prefix[i], sufix[i]) - height[i], 0) for i in range(len(height)))

# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 1 x x x 1 0 0
# 0 1 x 1 x x x 1 1 0
# 0 1 x 1 1 x 1 1 1 1

# 2: prefix = 0
# 0: prefix = 2
# 

