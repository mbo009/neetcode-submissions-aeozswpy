class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = dict(Counter(s1))
        current_window = dict(Counter(s2[:len(s1)]))

        for i in range(len(s1), len(s2)):
            if counter == current_window:
                return True
            else:
                current_window[s2[i - len(s1)]] -= 1
                if current_window[s2[i - len(s1)]] == 0:
                    del current_window[s2[i - len(s1)]]

                current_window[s2[i]] = current_window.get(s2[i], 0) + 1

        
        return counter == current_window
        