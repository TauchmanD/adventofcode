import io
def main(file=[]):
    r = 0
    for line in file:
        (x1, x2), (y1, y2) = map(lambda x: map(int, x.split("-")), line.split(","))
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