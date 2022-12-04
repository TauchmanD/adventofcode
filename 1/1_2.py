import io


def main(file=[]):
    mx = [0, 0, 0]
    tmp = 0
    for line in file:
        if line != '\n':
            tmp += int(line)
            mx[mx.index(min(mx))] = max(tmp, min(mx))
        else:
            tmp = 0
    print(sum(mx))

if __name__ == "__main__":
    with io.open("input.txt", "r") as f:
        file = f.readlines()
    main(file)
