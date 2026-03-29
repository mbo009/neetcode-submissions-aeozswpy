from collections import deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        path_simplified = ""
        for i in range(1, len(path)):
            if not path[i - 1] == path[i] == '/':
                path_simplified += path[i]

        stack = []
        for directory in path_simplified.split('/'):
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory and directory != ".":
                stack.append(directory)
        
        return "/"+ "/".join(directory for directory in stack) 