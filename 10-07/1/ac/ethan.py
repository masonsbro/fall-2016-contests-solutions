T = int(raw_input())

for t in range(T):
    names = [raw_input().split() for _ in range(5)]
    if len(set(map(lambda x: x[0], names))) == 5:
        print "HAPPINESS"
    else:
        print "DISAPPOINTMENT"
