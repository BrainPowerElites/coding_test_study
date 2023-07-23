import sys
sys.stdin=open("input.txt", "r")  

def DFS(L, s, tot): 
    global cnt
    if L==k: 
        if tot%m==0:
            cnt+=1
    else: 
        for i in range(s, n):          
            DFS(L+1, i+1, tot+a[i])


if __name__ == "__main__": 
    n, k = map(int, input().split()) 
    a = list(map(int, input().split())) 
    m = int(input()) 
    cnt = 0
    tot = 0
    DFS(0, 0, 0)
    print(cnt)
