"""
    U of U general catalog website sucks so I wrote this code to check which HF, LS, and PS
    classes overlap with the DV and IR requirements I need.
    Author: Benjamin Keefer
    Version: November 12th, 2024
"""
dataset = []
# TODO make the first filename the one that the subsequent ones need to overlap with
files = ["IR.txt", "LS.txt", "PS.txt"]

def main():
    for i in range(len(files)):
        read(files[i])
    overlap()

def overlap():
    check = dataset[0]
    for i in range(1,len(files)):
        keys = list(dataset[i].keys())
        # TODO: Adjust comment depending on class designation
        print(files[i].split(".")[0] + " and IR")
        print("=================")
        count = 0
        idx = 0
        for l in dataset[i].values():
            for num in l:
                if(keys[idx] in check and check[keys[idx]].__contains__(num)):
                    print(keys[idx] + " " + num)
                    count += 1
            idx += 1
        if(count == 0):
            print("no overlapping classes")
        print()

def read(currentFile):
    dict = {}

    with open(currentFile, "r") as input:
        line = input.readline().rstrip()
        while line != "":
            line = input.readline().rstrip()
            sections = line.split(" ")
            previous = ""
            for i in range(len(sections)):
                if(i % 2 == 1):
                    numbers = sections[i].split(",")
                    digits = []
                    for num in numbers:
                        digits.append(num)
                    dict[previous] = digits
                else:
                    previous = sections[i]
    dataset.append(dict)

if __name__ == "__main__":
    main()
