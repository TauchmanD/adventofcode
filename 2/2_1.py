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
        if (y == rps[x]):
            t += 0 + vals[y]
        elif (x == rps[y]):
            t += 6 + vals[y]
        else:
            t += 3 + vals[y]
        r += t
    print(r)

if __name__ == "__main__":
    with io.open("input.txt", "r") as f:
        file = f.readlines()
    main(file)
