class Solution:
    def reverseArray(self, arr):
        # code here
        self.reverse(arr,0,len(arr)-1)
        
    def reverse(self, arr, start, end):
        if start>=end:
            return
        arr[start],arr[end]=arr[end],arr[start]
        self.reverse(arr, start+1, end-1)
        