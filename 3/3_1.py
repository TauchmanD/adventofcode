import string
def main():
    chars = list(string.ascii_letters)
    i = input()
    r = 0
    while i != "e":
        i1 = i[:len(i)//2]
        i2 = i[len(i)//2:]
        s = list(filter(lambda x: x in i1, i2))[0]
        n = chars.index(s) + 1
        r += n
        i = input()
    print(r)

if __name__ == "__main__":
    main()