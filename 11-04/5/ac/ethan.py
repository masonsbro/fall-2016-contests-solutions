def intersection(a, b):
    return (a[0], max(b[1], a[1]))

def intersects(a, b):
    return b[0] <= a[1]

def union(intervals):
    intervals = sorted(intervals)
    ans = [intervals[0]]
    for interval in intervals[1:]:
        if intersects(ans[-1], interval):
            ans[-1] = intersection(ans[-1], interval)
        else:
            ans.append(interval)
    return ans

def size(intervals):
    ans = 0
    for interval in intervals:
        ans += interval[1] - interval[0] + 1
    return ans

T = int(raw_input())

for t in range(T):
    N, M, Q = map(int, raw_input().split())
    tags = {}
    intervals = {}
    ans = {}
    for n in range(N):
        pin_id = int(raw_input())
        pin_tags = raw_input().split()
        tags[pin_id] = pin_tags
    for m in range(M):
        pin_id, interval_start, interval_end = map(int, raw_input().split())
        for tag in tags[pin_id]:
            if tag not in intervals:
                intervals[tag] = []
            intervals[tag].append((interval_start, interval_end))
    for tag in intervals:
        ans[tag] = size(union(intervals[tag]))
    for q in range(Q):
        tag = raw_input()
        if tag in ans:
            print ans[tag]
        else:
            print 0
