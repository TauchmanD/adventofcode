import sys
import io


def main(file=[]):
    x = 1
    cycle = 0
    s = 0

    for line in file:
        cycle += 1

        if tc(cycle):
            s += x * cycle

        if "addx" in line:
            _, v = line.split()
            cycle += 1
            if tc(cycle):
                s += x * cycle
            x += int(v)
    print(s)


def tc(c):
    return (c == 20) or (c % 40 == 20 and 0 < c <= 220 )


if __name__ == "__main__":
    with io.open(sys.argv[1], "r") as f:
        file = f.readlines()
        main(file)
