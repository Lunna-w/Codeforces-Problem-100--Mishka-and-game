n = int(input())

mishka = 0
chris = 0

for i in range(n):
    m, c = list(map(int, input().split()))
    if m > c:
        mishka += 1
    elif m < c:
        chris += 1
    

if mishka > chris:
    print("Mishka")
elif chris > mishka:
    print("Chris")
else:
    print("Friendship is magic!^^")
