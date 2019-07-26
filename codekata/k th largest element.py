n1,n2=map(int,input().split())
inp=list(map(int,input().split()))
inp.sort(reverse=True)
print(inp[n2-1])
