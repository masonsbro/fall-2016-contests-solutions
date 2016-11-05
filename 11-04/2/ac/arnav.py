class Color(object):
    def __init__(self, inp):
        self.red = int(inp[1:3], 16)
        self.green = int(inp[3:5], 16)
        self.blue = int(inp[5:7], 16)

    def __str__(self):
        def hexify(s):
            frag = hex(s)[2:]
            if len(frag) == 1:
                return '0' + frag
            else:
                return frag

        return '#{}{}{}'.format(hexify(self.red), hexify(self.green), hexify(self.blue)).upper()

    def __repr__(self):
        return 'Color({}, {}, {})'.format(hex(self.red), hex(self.green), hex(self.blue))

def dist(pinA, pinB):
    redDelta = pinA.red - pinB.red
    greenDelta = pinA.green - pinB.green
    blueDelta = pinA.blue - pinB.blue

    return redDelta * redDelta + greenDelta * greenDelta + blueDelta * blueDelta

def solve():
    numPins, query = input().split()
    numPins = int(numPins)
    query = Color(query)
    pins = [Color(input()) for _ in range(numPins)]

    pins.sort(key=lambda pin: str(pin))
    pins.sort(key=lambda pin: dist(pin, query))

    print("Case {}:".format(query))
    for pin in pins:
        print(pin)

def main():
    T = int(input())
    for _ in range(T):
        solve()

main()
