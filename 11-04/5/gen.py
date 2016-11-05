from random import randrange
t = 10
print(t)
for i in range(t):
    n = 50
    m = 500
    q = 20
    tags = 30
    print(str(n)+" "+str(m)+" "+str(q))
    for j in range(n):
        print(j)
        print(str(0)+" ",end="")
        for k in range(1,tags):
            r = randrange(0,2)
            if r == 1:
                print(str(k)+" ",end="")
        print()
    for j in range(m):
        pin = randrange(0,n)
        start_user = randrange(0, 10)
        end_user = randrange(10, 100)
        print(str(pin)+" "+str(start_user)+" "+str(end_user))
    for j in range(q):
        tag = randrange(0, tags)
        print(tag)
