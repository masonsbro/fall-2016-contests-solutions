
def main():
	cases = int(input())
	for a in range(0, cases):
		numItems, numTake = map(int, input().split())
		items = input().split()
		inventory = {}
		start = -1
		finish = -1
		minTake = 2**32
		done = False

		while (not done):
			# pull start forward
			if (len(inventory) == numTake):
				start += 1
				if (start == len(items)):
					done = True
				else:
					inventory[items[start]] = inventory[items[start]] - 1
					if (inventory[items[start]] == 0):
						del inventory[items[start]]
			else: # push finish back
				finish += 1
				if (finish == len(items)):
					done = True
				else:
					if (items[finish] in inventory):
						inventory[items[finish]] = inventory[items[finish]] + 1
					else:
						inventory[items[finish]] = 1

			if (len(inventory) == numTake and finish - start < minTake):
				minTake = finish - start

		if (minTake == 2**32):
			print('-1')
		else:
			print(str(minTake))

main()