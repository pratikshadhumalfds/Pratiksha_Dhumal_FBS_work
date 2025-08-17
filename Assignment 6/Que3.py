###pascal's Triangle...

n=4
for i in range(n):
    val=1
    for j in range(i+1):
        print(val,end=' ')
        val=val*(i-j)//(j+1)
    print()    