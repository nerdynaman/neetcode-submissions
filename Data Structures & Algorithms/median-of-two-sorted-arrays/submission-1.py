class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            arrA, arrB = nums1, nums2
        else:
            arrA, arrB = nums2, nums1

        low, high = 0, len(arrA)
        leftPartCount = (len(arrA) + len(arrB) + 1)//2 
        # we know how many values will be part of left partition of final array -done
        # idea is for arr A we will find mid of array
        # first (leftPartCount - mid) elements will be taken from arr B
        while low<=high:
            arrAValues = (low + high)//2
            arrBValues = leftPartCount - arrAValues
            aLeft = arrA[arrAValues-1] if arrAValues>0 else float('-inf')
            aRight = arrA[arrAValues] if arrAValues<len(arrA) else float('inf')
            bLeft = arrB[arrBValues-1] if arrBValues>0 else float('-inf')
            bRight = arrB[arrBValues] if arrBValues<len(arrB) else float('inf')


            if aLeft > bRight:
                high = arrAValues - 1
            elif bLeft>aRight:
                low = arrAValues + 1
            else:
                if (len(arrA)+len(arrB))%2 == 0:
                    return ( max(aLeft,bLeft) + min(aRight, bRight) )/2
                return max(aLeft, bLeft)