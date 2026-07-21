class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #O(log(min(m,n))) time and O(1) space 
        if len(nums1)>len(nums2):
            A,B = nums2, nums1
            n = len(B)
            m = len(A)
        else: 
            A,B = nums1,nums2
            m = len(A)
            n = len(B)

        #size of combined left half
        half =(m+n+1)//2
        low,high = 0,m
        while low<=high:
            i = (low+high)//2
            j = half-i
            #store only boundary values 
            left_A = A[i-1] if i>0 else float('-inf')
            right_A = A[i] if i<m else float('inf')
            left_B = B[j-1] if j>0 else float('-inf')
            right_B = B[j] if j<n else float('inf')
            #max of left should <= min of right across arrays
            if left_A<=right_B and left_B<=right_A:
                if (m+n)%2:
                    return max(left_A,left_B)
                return (max(left_A,left_B)+min(right_A,right_B))/2
            elif left_A>right_B: 
                high = i-1
            else: 
                low=i+1

        