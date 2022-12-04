import io

def main(file=[]):
    r = 0
    remap = {"X": "A", "Y": "B", "Z": "C"}
    rps = {"A": "C", "B": "A", "C": "B"}
    vals = {"A": 1, "B": 2, "C": 3}
    for line in file:
        x, y = line.split()
        y = remap[y]
        t = 0
        if (y == "A"):
            t += vals[rps[x]]
        elif (y == "B"):
            t += 3 + vals[x]
        else:
            t += 6 + vals[list(rps.keys())[list(rps.values()).index(x)]]
        r += t
    print(r)

if __name__ == "__main__":
    with io.open("input.txt", "r") as f:
        file = f.readlines()
    main(file)
