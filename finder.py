n = list(map(str,input().split()))
x = ''
searched = input()
new = input()
print(n)
for i in range(len(n)):
    if searched in n[i]:
        n[i]=new + n[i].split(searched)[1]
        
for i in n:
    x=x+i+' '
print(x)

