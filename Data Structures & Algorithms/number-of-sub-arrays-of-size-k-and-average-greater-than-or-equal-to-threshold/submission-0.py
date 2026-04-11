class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0
        
        curr_sum = sum(arr[:k])
        subarray_num = 0
        
        if curr_sum >= threshold * k:
            subarray_num += 1

        for j in range(k, len(arr)):
            curr_sum += arr[j]
            curr_sum -= arr[j - k]

            if curr_sum >= threshold * k:
                subarray_num += 1
        
        return subarray_num