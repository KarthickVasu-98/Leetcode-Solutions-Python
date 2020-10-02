n = -123

a = str(abs(n))
a = a.strip()
a = a[::-1]
output = int(a)

if output>= 2**31 or output<= -2**31:
    print(0)
elif n<0:
    print(-1*output)
else:
    print(output)
