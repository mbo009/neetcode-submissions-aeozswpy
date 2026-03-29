class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = {char: i for i, char in enumerate(order)}
        return "".join(sorted(s, key=lambda x: order_dict.get(x, len(s) + 1)))
