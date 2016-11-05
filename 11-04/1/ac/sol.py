def good(word):
    return 'pin' in word \
       and word not in {'pin', 'pins', 'pinned', 'pinning', 'pinner', 'pinners'}

def main():
    T = int(input())
    for _ in range(T):
        words = [word.lower() for word in input().split()]

        count = 0
        for word in words:
            if good(word):
                count += 1

        print(count)

main()
