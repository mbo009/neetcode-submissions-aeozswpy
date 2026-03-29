class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num // 2 + 2):
            squared = i * i
            if squared >= num:
                if squared == num:
                    return True
                break
        return False