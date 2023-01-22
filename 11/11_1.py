import sys
import io
import re
import math

def main(file=[]):
    monkeys = dict()
    for monkey in file:
        line = monkey.split("\n")
        id = int(re.findall("(\d+)", line[0])[0])
        monkeys[id] = dict()
        monkeys[id]["items"] = [int(a) for a in re.findall("(\d+)", line[1])]
        operation, operand = re.findall("(\+|\*)\s(old|\d+)", line[2])[0]
        monkeys[id]["opn"] = operation
        monkeys[id]["op"] = operand
        monkeys[id]["div"] = int(re.findall("(\d+)", line[3])[0])
        monkeys[id]["true"] = int(re.findall("(\d+)", line[4])[0])
        monkeys[id]["false"] = int(re.findall("(\d+)", line[5])[0])
        monkeys[id]["r"] = 0


    i = 0
    while i < 20:
        for id, monkey in monkeys.items():
            m = monkeys[id]
            while m["items"]:
                worry_item = m["items"].pop(0)
                m["r"] += 1
                match monkey["opn"]:
                    case '*':
                        op = worry_item if m["op"] == "old" else int(m["op"])
                        worry_item *= op
                    case "+":
                        worry_item += int(m["op"])
                worry_item = worry_item // 3
                if worry_item % m["div"] == 0:
                    monkeys[monkey["true"]]["items"].append(worry_item)
                else:
                    monkeys[monkey["false"]]["items"].append(worry_item)
        i += 1
    res = sorted([m['r'] for m in monkeys.values()])
    print(res[-1] * res[-2])

if __name__ == "__main__":
    with io.open(sys.argv[1], "r") as f:
        file = f.read().split("\n\n")
        main(file)
