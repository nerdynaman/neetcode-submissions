class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptrA, ptrB = 0, len(numbers)-1
        while ptrA < ptrB:
            currVal = numbers[ptrA]+numbers[ptrB]
            if currVal == target:
                return [ptrA+1,ptrB+1]
            elif currVal < target:
                ptrA +=1
            else:
                ptrB -= 1

