from Queue import PriorityQueue

T = int(raw_input())

for t in range(T):
    numEsc, numFloors, numHeroes = map(int, raw_input().split())
    adj = {i: [] for i in range(numFloors)}
    for esc in range(numEsc):
        speed, div, direction = raw_input().split()
        speed, div = int(speed), int(div)
        numStops = (numFloors - 1) / div + 1
        if direction == "DOWN":
            for i in range(0, numStops - 1):
                adj[div*i].append((div*(i+1), div*speed))
        else:
            for i in range(numStops - 1, 0, -1):
                adj[div*i].append((div*(i-1), div*speed))
    starts = map(int, raw_input().split())
    q = PriorityQueue()
    q.put((0, numFloors - 1))
    minTime = [None]*numFloors
    while not q.empty():
        cost, floor = q.get()
        if minTime[floor] is not None: continue
        minTime[floor] = cost
        for nextFloor, addCost in adj[floor]:
            if minTime[nextFloor] is None:
                q.put((cost + addCost, nextFloor))
    finishTimes = map(lambda x: minTime[x], starts)
    if any(map(lambda x: x is None, finishTimes)):
        print "IMPOSSIBLE"
    else:
        print max(finishTimes)
