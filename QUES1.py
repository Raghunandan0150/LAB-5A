x=int(input("Enter x:"))
y=int(input("Enter y:"))
N=int(input("Enter n:"))

for i in range(x+1,y+1):
    if i % N == 0:
        print(i)
