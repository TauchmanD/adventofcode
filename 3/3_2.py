import string
def main():
    chars = list(string.ascii_letters)
    i1, i2, i3 = input(), input(), input()
    r = 0
    while i1 and i2 and i3:
        s = list(filter(lambda x: x in i1 and x in i2, i3))[0]
        n = chars.index(s) + 1
        r += n
        i1, i2, i3 = input(), input(), input()
    print(r)

if __name__ == "__main__":
    main()
