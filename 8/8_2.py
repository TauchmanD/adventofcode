import numpy as np
import sys
import io


def main(file=[]):
    trees = [[int(char) for char in line if char != "\n"] for line in file]
    v = 0
    end = len(trees)-1
    trees = np.array(trees)
    for i in range(1, end):
        for j in range(1,end):
            tmp = 1
            row = trees[i, :]
            column = trees[:, j]
            t = trees[i,j]
            r = row[j+1:]
            l = np.flip(row[:j])
            d = column[i+1:]
            u = np.flip(column[:i])
            if max(r) >= t:
                tmp *= np.argmax(r >= t) + 1
            else:
                tmp *= len(r)
                
            if max(d) >= t:
                tmp *= np.argmax(d >= t) + 1
            else:
                tmp *= len(d)

            if max(l) >= t:
                tmp *= np.argmax(l >= t) + 1
            else:
                tmp *= len(l)

            if max(u) >= t:
                tmp *= np.argmax(u >= t) + 1
            else:
                tmp *= len(u)

            if tmp > v:
                v = tmp
    print(v)


if __name__ == "__main__":
    with io.open(sys.argv[1], "r") as f:
        file = f.readlines()
        main(file)
