n = int(input("Enter the input: "))

rev = 0
d = 0
x = n

while x>0:
    d = x%10
    x = int(x/10)
    rev = rev*10+d

if rev==n:
    print(True)
else:
    print(False)
