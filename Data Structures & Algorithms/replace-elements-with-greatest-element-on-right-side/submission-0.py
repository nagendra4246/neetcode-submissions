class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxEle = -1 
        for i in range(len(arr) - 1,-1,-1):
            curEle = arr[i]
            arr[i] = maxEle
            maxEle = max(maxEle,curEle)
        return arr
            
        