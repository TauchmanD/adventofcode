
import sys
import io

def sprite(cycle, r, x):
    mid = cycle % 40
    if not mid:
        r+=1
        print()
    if mid-1 <= x <= mid+1:
        print("#", end="")
    else:
        print(".", end="")

def main(file=[]):
    x = 1
    cycle = 0
    r = 0

    for line in file:
        sprite(cycle, r, x)
        cycle += 1
        

        if "addx" in line:
            _, v = line.split()
            sprite(cycle,r,x)
            cycle += 1
            x += int(v)


def tc(c):
    return (c == 20) or (c % 40 == 20 and 0 < c <= 220 )


if __name__ == "__main__":
    with io.open(sys.argv[1], "r") as f:
        file = f.readlines()
        main(file)
