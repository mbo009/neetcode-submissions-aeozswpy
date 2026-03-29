from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_tasks = Counter(tasks)
        last_tasks = {task: -1 for task, _ in count_tasks.items()}
        cycles = 0

        while len(count_tasks) > 0:
            possible_tasks = []
            for task, last in last_tasks.items():
                if last == -1 or cycles - last > n:
                    possible_tasks.append(task)
            
            max_count = 0
            max_task = None
            for task in possible_tasks:
                if count_tasks[task] > max_count:
                    max_count = count_tasks[task]
                    max_task = task
            
            if max_task:
                count_tasks[max_task] -= 1
                last_tasks[max_task] = cycles
                if count_tasks[max_task] == 0:
                    del count_tasks[max_task]
                    del last_tasks[max_task]

            cycles += 1

        return cycles
# Solution:
# 1. Count which characters occur how many times x
# 2. Create dict where task: last_cycle
# 3. Iterate through keys, and find possible characters that where in n range
# 4. Pick the one with the most count
# 5. If task count == 0, delete from counter

# X, X, Y, Y
# X : 2
# Y : 2

            

