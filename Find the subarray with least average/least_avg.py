import sys

def find_subarray(arr,k,len_):
    av = sys.maxsize
    a = []
    for i in range(len_-k):
        new_av = 0
        l = []
        for j in range(k):
            new_av += arr[i+j]
            l.append([i+j])
        new_av/=k
        if new_av<av:
            av = new_av
            a = l
    return a



len_ = int(input("enter the length of list:"))
a = []
for i in range(len_):
    a.append(int(input()))
k = int(input("enter the length of the subarray:"))
result_ = find_subarray(a,k,len_)
print(result_)
