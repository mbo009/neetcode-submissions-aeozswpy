class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ip_arr = []

        def backtrack(i, dots, curr_ip):
            if dots == 4 and i == len(s):
                self.ip_arr.append(curr_ip[:-1])
                return
        
            if dots >= 4 or i >= len(s):
                return

            if s[i] == "0":
                backtrack(i + 1, dots + 1, curr_ip + s[i] + ".")
                return
     
            for j in range(1, 4):
                if i + j - 1 > len(s):
                    break
                if int(s[i : i + j]) <= 255:
                    backtrack(i + j, dots + 1, curr_ip + s[i : i + j] + ".")
    
            return

        backtrack(0, 0, "")
        return self.ip_arr               