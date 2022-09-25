 
def main():
    s = str(input())
    res = 1
    l = 0
    for i in range(1,len(s)):
        if s[i] == s[l] :
            res = max(i-l + 1 , res )
        else :
            l = i
    
    return res
 
 
 
res = main()
print(res)