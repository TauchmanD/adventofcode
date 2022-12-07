import io


def main(file=[]):
    stack = []
    pointer = -1
    max_size = 100000
    total = 0
    for line in file:
        match line.split():
            case "$", "cd", "..":
                if stack[pointer] <= max_size:
                    total += stack[pointer]
                pointer -= 1
                last = stack.pop(-1)
                stack[pointer] += last
            case "$", "cd", x:
                stack.append(0)
                pointer += 1
            case "$", "ls": pass
            case "dir", x: pass
            case size, _:
                stack[pointer] += int(size)
    print("Result",total)




if __name__ == "__main__":
    with io.open("input.txt", "r") as f:
        file = f.readlines()
    main(file)
