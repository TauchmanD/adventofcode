import sys
import io
from collections import deque
import string


def bfs(start, end):
    q = deque()
    v = set()
    q.append([start])
    while q:
        path = q.popleft()
        y, x = path[-1]
        if (y, x) not in v:
            v.add((y, x))
            if (y,x) == end:
                return len(path) - 1
            l = grid[y][x]
            h1 = d[l]
            for dy, dx in dirs:
                ny, nx = y + dy, x + dx
                if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                    l = grid[ny][nx]
                    h2 = d[l]
                    if h2 <= h1 + 1:
                        np = path[:]
                        np.append((ny, nx))
                        q.append(np)



def main(file=[]):
    global grid
    grid = list(line.strip() for line in file)
    global d
    d = {chr(i): i - 96 for i in range(97, 97+26)}
    d['S'] = 1
    d['E'] = 26
    global dirs
    dirs = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
    ]
    for i, line in enumerate(grid):
        if "S" in line:
            start = (i, line.index("S"))
        if "E" in line:
            end = (i, line.index("E"))
    print(bfs(start, end))


if __name__ == "__main__":
    with io.open(sys.argv[1], "r") as f:
        file = f.readlines()
        main(file)
