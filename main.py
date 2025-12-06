n=int(input())
k26=0
k13=0
k2=0
for i in range(n):
    x =int(input())
    if x%26==0:
        k26+=1
    elif x %13==0:
        k13+=1
    elif x%2==0:
        k2+=1
result=k26*(n-k26)+k26*(k26-1)//2+k2*k13
print(result)


n = int(input())
k62=0
k31=0
k2=0
for i in range(n):
    x =int(input())
    if x %62 ==0:
        k62+=1
    elif x %31==0:
        k31+=1
    elif x %2==0:
        k2+=1
result=k62*(n-k62)+k62*(k62-1)//2+k2*k31
print(result)

