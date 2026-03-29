class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        buffer = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            digit1 = ord(num1[i]) - ord('0')
            for j in range(len(num2) - 1, -1, -1):
                digit2 = ord(num2[j]) - ord('0')
                product = digit1 * digit2
                pos = i + j + 1
                total = product + buffer[pos]

                buffer[pos] = total % 10
                buffer[pos - 1] += total // 10
        
        i = 0
        while i < len(buffer) and buffer[i] == 0:
            i += 1
        
        return "".join(str(buffer[j]) for j in range(i, len(buffer)))