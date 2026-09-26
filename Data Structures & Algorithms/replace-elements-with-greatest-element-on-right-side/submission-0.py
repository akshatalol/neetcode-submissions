class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            c = max(arr[(i+1):(len(arr))], default=-1)
            arr[i]=c
        return arr


        