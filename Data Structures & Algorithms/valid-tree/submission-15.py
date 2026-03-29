class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        in_degree = [0] * n
        seen = set()

        for u, v in sorted(edges):
            smaller = min(u, v)
            bigger = max(u, v)

            if smaller in seen and bigger in seen:
                return False

            if smaller not in seen and bigger not in seen:
                in_degree[bigger] += 1
            elif smaller not in seen:
                in_degree[smaller] += 1
            else:
                in_degree[bigger] += 1

            seen.add(smaller)
            seen.add(bigger)
        
        zero_count = in_degree.count(0)
        one_count = in_degree.count(1)
        
        return n == (zero_count + one_count) and zero_count == 1