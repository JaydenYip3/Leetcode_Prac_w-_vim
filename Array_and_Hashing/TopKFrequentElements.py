import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []
        for key,val in count.items():
            heap.append((val,key))
        result = heapq.nlargest(k, heap)
        
        result_final = [x[1] for x in result]
        return result_final 

print(Solution().topKFrequent([1,2,3,4], 2))
print(Solution().topKFrequent([1,33,3,4], 2))
