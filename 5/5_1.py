import io
import re

def main(file=[]):
    creates = {
        "1": ["F", "T", "C", "L", "R", "P", "G", "Q"],
        "2": ["N", "Q", "H", "W", "R", "F", "S", "J"],
        "3": ["F", "B", "H", "W", "P", "M", "Q"],
        "4": ["V", "S", "T", "D", "F"],
        "5": ["Q", "L", "D", "W", "V", "F", "Z"],
        "6": ["Z", "C", "L", "S"],
        "7": ["Z", "B", "M", "V", "D", "F"],
        "8": ["T", "J", "B"],
        "9": ["Q", "N", "B", "G", "L", "S", "P", "H"]
    }

    for line in file:
        m, f, t = map(int, re.findall("\d+", line))
        moving = creates[str(f)][len(creates[str(f)]) - m:len(creates[str(f)])]
        moving.reverse()
        creates[str(t)] = creates[str(t)] + moving
        for _ in range(m):
            creates[str(f)].pop()
    for x in creates.values():
        print(x[-1], end="")


if __name__ == "__main__":
    with io.open("input.txt", "r") as f:
        file = f.readlines()
    main(file)
