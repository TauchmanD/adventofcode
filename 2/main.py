def main():
    r=0
    remap = {"X":"A","Y":"B","Z":"C"}
    rps = {"A":"C", "B":"A", "C":"B"}
    vals = {"A":1, "B": 2, "C": 3}
    x, y = input().split()
    while x!="e":
        y = remap[y]
        t=0
        if(y=="A"):
            t += vals[rps[x]]
        elif(y=="B"):
            t += 3 + vals[x]
        else:
            t += 6 + vals[list(rps.keys())[list(rps.values()).index(x)]]
        r+=t
        x, y = input().split()
    print(r)


if __name__ == "__main__":
    main()