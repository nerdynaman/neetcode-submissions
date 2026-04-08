class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we will make a frequency table in O(N)
        frequency = {}
        for number in nums:
            frequency[number] = frequency.get(number,0) + 1
        
        occurenceArray = [[] for i in range(len(nums))]
        for num, numFrequency in frequency.items():
            occurenceArray[numFrequency-1].append(num)
        
        result = []
        iterator = len(nums)-1
        while True:
            if k<1:
                break
            result.extend(occurenceArray[iterator])
            k -= len(occurenceArray[iterator])
            iterator -= 1

        
        return result

