class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodArr = 1
        flag = 0
        for i in nums:
            if i == 0 :
                flag += 1
                continue
            prodArr *= i
        prodArrZero = prodArr
        prodArr = 0 if flag else prodArr
        
        resultArr = []
        for i in nums:
            if i != 0:
                resultArr.append(int(prodArr/i))
            elif flag == 1:
                resultArr.append(prodArrZero)
            else:
                resultArr.append(0)
            

        return resultArr