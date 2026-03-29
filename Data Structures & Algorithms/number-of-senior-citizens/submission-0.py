class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 for detail in details if int(detail[-4:-2]) > 60)

# 0 - 9 phone
# 10 - gender
# 11-12 age