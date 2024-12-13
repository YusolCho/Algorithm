K, N = map(int, input().split())
K_list = [int(input()) for _ in range(K)]

def binary_search(K_list, N):
    start, end = 1, max(K_list)

    while start <= end: 
        mid = (start+end)//2
        total = sum(k//mid for k in K_list)        

        if total >= N:
            start = mid + 1 
        else: 
            end = mid - 1
    return end

print(binary_search(K_list, N))