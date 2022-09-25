def main():
    n = int(input())
    arr = list(map(int,input().split()))
    res = 0 
    vis = {i for i in range(1,n+1)}
    for ele in arr :
        vis.remove(ele)
    return list(vis)[0]
 
 
 
res = main()
print(res)