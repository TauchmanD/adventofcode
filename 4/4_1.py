import io
def main(file=[]):
    r = 0
    for line in file:
        x, y = line.split(",")
        x1, x2 = map(int, x.split("-"))
        y1, y2 = map(int, y.split("-"))
        x = list(range(x1, x2+1))
        y = list(range(y1, y2+1))
        l = lambda a, b: a in b
        if all([l(i, y) for i in x]) or all([l(i, x) for i in y]):
            r+=1
    print(r)

if __name__ == "__main__":
    with io.open("input.txt", "r") as f:
        file = f.readlines()
    main(file)