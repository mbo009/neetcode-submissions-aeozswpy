class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_set = set()
        for email in emails:
            i = 0
            curr = ""
            plus_found = False

            while email[i] != "@":
                if email[i] == "+":
                    plus_found = True
                elif not plus_found and email[i] != ".":
                    curr += email[i]

                i += 1
            
            emails_set.add(curr + email[i:])
        
        return len(emails_set)