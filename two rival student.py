import sys
sys.stdin = open("input.in","r")
sys.stdout = open("output.out","w")
for _ in range(int(input())):
	n,x,a,b=map(int,input().split())
	t=min(n-1,abs(a-b)+x)
	print(t)