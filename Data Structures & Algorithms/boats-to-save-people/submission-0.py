class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sorted_people = sorted(people)
        i = 0
        j = len(people) - 1
        curr_boat = 0
        boat_count = 0

        while i <= j:
            if sorted_people[i] + sorted_people[j] <= limit:
                i += 1 
            
            j -= 1
            boat_count += 1
            
        return boat_count