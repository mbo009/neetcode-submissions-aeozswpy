from collections import OrderedDict


class TimeMap:
    def __init__(self):
        self.data = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        values = self.data[key]
        i = 0
        j = len(values) - 1
        res = ""

        while i <= j:
            mid = (i + j) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                i = mid + 1
            else:
                j = mid - 1
        
        return res