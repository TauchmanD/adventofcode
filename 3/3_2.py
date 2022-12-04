import string
import io
def main(file=[]):
    chars = list(string.ascii_letters)
    r = 0
    for i in range(len(file)//3):
        i1, i2, i3 = file[i*3], file[i*3+1], file[i*3+2]
        s = list(filter(lambda x: x in i1 and x in i2, i3))[0]
        n = chars.index(s) + 1
        r += n
    print(r)

if __name__ == "__main__":
    with io.open("input.txt", "r") as f:
        file = f.readlines()
    main(file)
