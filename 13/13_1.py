from ast import literal_eval
import sys
import io

def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return 1
        elif l == r:
            return 0
        return -1

    l = [l] if isinstance(l, int) else l
    r = [r] if isinstance(r, int) else r

    lrmin = min(len(l), len(r))

    for i in range(lrmin):
        n = compare(l[i], r[i])
        if n == -1:
            return n
        elif n == 1:
            return n

    return compare(len(l), len(r))


def main(file=[]):
    data = [literal_eval(line) for line in file if line != "\n"]
    s = 0
    for i in range(1, len(data), 2):
        if compare(data[i-1], data[i]) == 1:
            s += (i//2)+1
    print(s)
    

if __name__ == "__main__":
    with io.open(sys.argv[1], "r") as f:
        file = f.readlines()
        main(file)


