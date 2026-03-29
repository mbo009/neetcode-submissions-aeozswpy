class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i, row in enumerate(words):
            for j in range(len(row)):
              if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True  