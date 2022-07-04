num = list(map(int,input().split()))
k = int(input())
print(list(str(int(''.join(str(i) for i in num))+k)))