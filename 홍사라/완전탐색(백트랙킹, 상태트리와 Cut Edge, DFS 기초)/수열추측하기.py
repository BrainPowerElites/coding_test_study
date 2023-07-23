import sys
sys.stdin=open("input.txt", "rt")
def DFS(L, sum):
    if L==n and sum==f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i]=0

if __name__ == "__main__":
    n, f=map(int, input().split())
    p=[0]*n #순열 만들기 
    b=[1]*n #이항계수(파스칼)
    ch=[0]*(n+1) 
    #이항계수의 맨 끝은 다 1이므로, 그 안에 것들+(n-1)만 수정
    for i in range(1, n):
        b[i]=b[i-1]*(n-i)//i
    DFS(0, 0)
