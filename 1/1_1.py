import io

def main(file=[]):
    mx = 0
    tmp = 0
    for line in file:
        if line != '\n':
            tmp += int(line)
            mx=max(tmp, mx)
        else:
            tmp = 0
    print(mx)  # 1 - jen mx bez sumy

if __name__ == "__main__":
    with io.open("input.txt", "r") as f:
        file = f.readlines()
    main(file)
