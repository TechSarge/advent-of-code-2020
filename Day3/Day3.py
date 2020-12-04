

def countPath(rightIncrement, down, path):
    total = 0
    file = open(path, "r")
    Lines = file.read().splitlines()
    colums = len(Lines[0])
    print(colums)
    right = 0
    for line in Lines:
        if right >= colums:
            right = right - colums
        print(right)
        if line[right] == "#":
            total = total + 1
        print(line[:right] + "|" + line[right+1:] + "    " + str(right) + "   " + str(rightIncrement))

        right = 3 + right
    return total

def countPath2(rightIncrement, down, path):
    total = 0
    file = open(path, "r")
    Lines = file.read().splitlines()
    colums = len(Lines[0])
    print(colums)
    right = 0
    Num = 0
    while Num < len(Lines):
        line = Lines[Num]
        if right >= colums:
            right = right - colums
        print(right)
        if line[right] == "#":
            total = total + 1
        print(line[:right] + "|" + line[right+1:] + "    " + str(right) + "   " + str(rightIncrement))

        right = rightIncrement + right
        Num = Num + down
    return total

if __name__ == "__main__":
    print(countPath2(1, 1, "input") * countPath2(3, 1, "input") * countPath2(5, 1, "input") * countPath2(7, 1, "input") * countPath2(1, 2, "input"))