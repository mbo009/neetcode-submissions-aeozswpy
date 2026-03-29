from collections import deque, defaultdict

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        graph = defaultdict(list)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]

            for i in range(1, len(account)):
                email = account[i]
                graph[first_email].append(email)
                graph[email].append(first_email)
                email_to_name[email] = name
    
            if first_email not in email_to_name:
                email_to_name[first_email] = name

        seen = set()
        res = []

        for email in email_to_name:
            if email not in seen:
                seen.add(email)
                queue = deque([email])
                cluster = []
                
                while queue:
                    curr = queue.popleft()
                    cluster.append(curr)
                    for neighbor in graph[curr]:
                        if neighbor not in seen:
                            seen.add(neighbor)
                            queue.append(neighbor)
                res.append([email_to_name[email]] + sorted(cluster))
        
        return res