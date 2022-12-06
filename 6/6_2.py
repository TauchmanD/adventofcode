import io


def main(file=[]):
    buffer_size = 14
    r = buffer_size
    buffer = list(file[:buffer_size])
    for c in file[buffer_size:]:
        if len(set(buffer)) == buffer_size:
            break
        buffer.append(c)
        buffer.pop(0)
        r+=1
    print(r)


if __name__ == "__main__":
    file = input()
    if not file:
        with io.open("input.txt", "r") as f:
            file = f.read()
    main(file)
