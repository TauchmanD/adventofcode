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
            row = trees[i, :]
            column = trees[:, j]
            t = trees[i,j]
            r = row[j+1:]
            l = row[:j]
            d = column[i+1:]
            u = column[:i]
            if t > max(r) or t > max(u) or t > max(d) or t > max(l):
                v += 1
                print(t)
                print(r)
                print(i, j)
    v += len(trees) * 4 - 4
    print(v)


if __name__ == "__main__":
    with io.open(sys.argv[1], "r") as f:
        file = f.readlines()
        main(file)
