def main():
    r = 0
    x, y = input().split(",")
    x1, x2 = map(int, x.split("-"))
    y1, y2 = map(int, y.split("-"))
    x = list(range(x1, x2+1))
    y = list(range(y1, y2+1))
    l = lambda a, b: a in b
    while x != [0]:
        if all([l(i, y) for i in x]) or all([l(i, x) for i in y]):
            r+=1
        x, y = input().split(",")
        x1, x2 = map(int, x.split("-"))
        y1, y2 = map(int, y.split("-"))
        x = list(range(x1, x2+1))
        y = list(range(y1, y2+1))
    print(r)

if __name__ == "__main__":
    main()