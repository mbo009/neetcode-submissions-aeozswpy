class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
    
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            unique_emails.add(local.replace('.', '') + '@' + domain)
            
        return len(unique_emails)