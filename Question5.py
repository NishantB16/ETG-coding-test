arr=[1,2,3,4]
N=len(arr)
def maxprofit(self,arr):
    buy=0
    sell=1 
    max_prof=0
    while sell<N:
        curr_prof=arr[sell]-arr[buy]
        if arr[buy]<arr[sell]:
            max_prof=max(curr_prof,max_prof)
        else:
            buy=sell
            sell+=1 
    print("max_prof")        