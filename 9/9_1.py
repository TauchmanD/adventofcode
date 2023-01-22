import sys
import io


def main(file=[]):
    seen = []
    hx, hy = 0,0
    tx, ty = 0,0

    for line in file:
        d, a = line.split()
        a=int(a)
        match d:
            case "R":
                dx, dy = 1,0
            case "D":
                dx, dy = 0,-1
            case "L":
                dx, dy = -1,0
            case "U":
                dx, dy = 0,1
        for i in range(a):
            hx+=dx
            hy+=dy
            if max(abs(hx-tx), abs(hy-ty)) > 1:
                tx+=(hx-tx)//abs(hx-tx) if (hx-tx) else 0
                ty+=(hy-ty)//abs(hy-ty) if (hy-ty) else 0
            if (tx,ty) not in seen:
                seen.append((tx,ty))
    print(len(seen))


if __name__ == "__main__":
    with io.open(sys.argv[1], "r") as f:
        file = f.readlines()
        main(file)
