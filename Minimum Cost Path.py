import sys
h=int(input())
v=int(input())
arr=[]
for i in range(v):
	x=list(map(int,input().split()))
	arr.append(x)
dp=[[0 for i in range(h+1)] for j in range(v+1)]
for i in range(h+1):
	dp[0][i]=sys.maxsize
for i in range(v+1):
	dp[i][0]=sys.maxsize
for i in range(1,h+1):
	for j in range(1,v+1):
		if i==1 and j==1:
			dp[j][i]=arr[0][0]
		else:
			dp[j][i]=min(dp[j-1][i],dp[j][i-1])+arr[j-1][i-1]
print(dp)

'''
6
6
0 1 4 2 8 2
4 3 6 5 0 4
1 2 4 1 4 6
2 0 7 3 2 2
3 1 5 9 2 4
2 7 0 8 5 1
