def main():
    n = int(input())
    arr = [n]
    while n != 1 :
        if n % 2 == 0 :
            n = n // 2 
        else :
            n = (n*3) + 1
        arr.append(n)
    return arr
 
 
# t = int(input())
# for _ in range(t):
res = main()
print(*res)