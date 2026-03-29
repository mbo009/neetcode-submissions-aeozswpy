class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = len(word) - 1, len(abbr) - 1
        acc = 0
        acc_len = 1

        while j >= 0:
            if abbr[j].isdigit():
                num = int(abbr[j])
                # Sprawdzenie zera wiodącego: 
                # Jeśli to ZERO i za nim nie ma już więcej cyfr (to jest początek liczby)
                if num == 0 and (j == 0 or not abbr[j-1].isdigit()):
                    return False
                
                acc += num * acc_len
                acc_len *= 10
                j -= 1
            else:
                # Najpierw wykonaj skok o zgromadzone acc
                if acc > 0:
                    i -= acc
                    acc, acc_len = 0, 1
                
                # Potem sprawdź czy litery się zgadzają
                if i < 0 or word[i] != abbr[j]:
                    return False
                i -= 1
                j -= 1
        
        if acc > 0:
            i -= acc
            
        return i == -1