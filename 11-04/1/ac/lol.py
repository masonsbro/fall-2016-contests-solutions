for _ in range(int(input())): print(sum(int('pin' in word.lower() and word.lower() not in {'pin', 'pins', 'pinned', 'pinning', 'pinner', 'pinners'}) for word in input().split())) 
