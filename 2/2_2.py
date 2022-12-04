import io

def main(file=[]):
    pass
    
if __name__ == "__main__":
    with io.open("input.txt", "r") as f:
        file = f.readlines()
    main(file)