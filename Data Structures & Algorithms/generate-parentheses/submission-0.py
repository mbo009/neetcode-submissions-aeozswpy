class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def parenthesisRec(left, right, curr_path):
            if left == n and right == n:
                res.append(curr_path)
                return
            
            if left < n:
                parenthesisRec(left + 1, right, curr_path + "(")
            if right < n and left > right:
                parenthesisRec(left, right + 1, curr_path + ")")
            
        parenthesisRec(0, 0, "")
        return res