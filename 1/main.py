import sys
import io
def main(input=0):
    x=0
    mx=[0,0,0] #1 - mx=0
    tmp=0
    while x!="x":
        if x != '':
            tmp+=int(x)
            mx[mx.index(min(mx))]=max(tmp,min(mx)) #1 - mx=max(tmp,mx))
        else:
            tmp=0
        x=input()
    print("r - ", sum(mx)) #1 - jen mx bez sumy


if __name__ == "__main__":
    main(input)