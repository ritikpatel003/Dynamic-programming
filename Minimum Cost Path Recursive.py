import sys
h=int(input())
v=int(input())
arr=[]
for i in range(v):
	x=list(map(int,input().split()))
	arr.append(x)
def sol(i,j,h,v):
	if i==h-1 and j==v-1:
		return arr[i][j]
	if i>=h or j>=v:
		return sys.maxsize
	return min(sol(i+1,j,h,v),sol(i,j+1,h,v))+arr[i][j]

print(sol(0,0,h,v))

