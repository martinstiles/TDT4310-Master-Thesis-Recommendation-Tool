from pathlib import Path

with open(Path(__file__).parent / "data.txt", "r") as file:
    c = 0
    for line in [line for line in file.readlines()]:
        if len(line.split(" | ")) != 6:
            print(line)
            print(c)
            print("####################")
        c += 1

    # TODO: THERE IS A PROBLEM WITH THE RETRIEVAL, WHICH HAPPENS WHEN
    # THE FRIST <p> CONTAINS MORE THAN JUST TEXT. MAKE THAT METHOD GENERIC
    # AND SEE IF THAT FIXES THE ISSUE

    # print(len([line for line in file.readlines()
    #            if len(line.split(" | ")) == 6]))
