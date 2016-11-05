from collections import defaultdict

def merge(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort()
    stack = [intervals[0]]
    answer = 0
    for interval in intervals:
        temp = stack.pop()
        if temp[1] >= interval[0]:
            if interval[1] > temp[1]:
                stack.append([temp[0], interval[1]])
            else:
                stack.append(temp)
        else:
            stack.append(temp)
            stack.append(interval)
    for interval in stack:
        answer += interval[1] - interval[0] + 1
    return answer


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        pins, logs, queries = map(int, input().split())
        pin_to_intervals = defaultdict(list)
        tag_to_pins = defaultdict(list)
        tag_to_unique_users = {}
        for j in range(pins):
            pin = int(input())
            tags = input().split()
            for tag in tags:
                tag_to_pins[tag].append(pin)
        for j in range(logs):
            pin, start, end = map(int, input().split())
            pin_to_intervals[pin].append([start,end])
        for j in range(queries):
            tag = input()
            if tag in tag_to_unique_users:
                print(tag_to_unique_users[tag])
                continue
            result_intervals = []
            for pin in tag_to_pins[tag]:
                if pin in pin_to_intervals:
                    result_intervals += pin_to_intervals[pin]
            unique_users = merge(result_intervals)
            print(unique_users)
            tag_to_unique_users[tag] = unique_users
