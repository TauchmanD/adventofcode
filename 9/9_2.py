import sys
import io


def main(file=[]):
    seen = set()
    rope = [[0,0] for i in range(10)]
    seen.add(tuple(rope[-1]))

    for line in file:
        d, a = line.split()
        a=int(a)
        for _ in range(a):
            match d:
                case "R":
                    dx, dy = 1,0
                case "D":
                    dx, dy = 0,-1
                case "L":
                    dx, dy = -1,0
                case "U":
                    dx, dy = 0,1

            rope[0][0] += dx
            rope[0][1] += dy
            for x in range(1,10):
                dx = rope[x-1][0] - rope[x][0]
                dy = rope[x-1][1] - rope[x][1]
                if max(abs(dx), abs(dy)) > 1:
                    rope[x][0] += dx//abs(dx) if dx else 0
                    rope[x][1] += dy//abs(dy) if dy else 0
                seen.add(tuple(rope[-1]))
    print(len(seen))


if __name__ == "__main__":
    with io.open(sys.argv[1], "r") as f:
        file = f.readlines()
        main(file)
