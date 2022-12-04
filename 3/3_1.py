import string
import io
def main(file=[]):
    chars = list(string.ascii_letters)
    r = 0
    for line in file:
        i1, i2 = line[:len(line)//2], line[len(line)//2:]
        s = list(filter(lambda x: x in i1, i2))[0]
        n = chars.index(s) + 1
        r += n
    print(r)

if __name__ == "__main__":
    with io.open("input.txt", "r") as f:
        file = f.readlines()
    main(file)