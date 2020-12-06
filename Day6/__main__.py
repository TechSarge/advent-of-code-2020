import os
import re
import string

def parseFile1(file):
    outfile = []
    tempfile = file.read().split("\n\n")
    for entry in tempfile:
        entry = entry.replace("\n", "").replace("\r", "") # remove new lines 
        outfile.append(entry)
    return outfile

def parseFile2(file):
    tempfile = file.read().split("\n\n")

    return tempfile

    

def solve1(file) -> int:
    sum = 0
    for group in file:
        letters = []
        for letter in group:
            if letter not in letters:
                letters.append(letter)
        sum += len(letters)
    return sum

def solve2(file) -> int:
    sum = 0
    for group in file:
        persons = group.split("\n")
        alph = list(string.ascii_lowercase)
        response = list(string.ascii_lowercase)
        for person in persons:
            for letter in alph:
                if letter not in person:
                    try:
                        response.remove(letter)
                    except:
                        pass
        sum += len(response)

    return sum


if __name__ == "__main__":
    data = open(os.path.dirname(__file__) + "\input", "r") # open files for the program to run
    data2 = open(os.path.dirname(__file__) + "\input", "r") # open files for the program to run

    sample = open(os.path.dirname(__file__) + "\sample", "r")
    sample2 = open(os.path.dirname(__file__) + "\sample", "r")

    print("Part 1 sample:")
    print(solve1(parseFile1(sample)))
    print("Part 1 input:")
    print(solve1(parseFile1(data)))

    print("Part 2 sample:")
    print(solve2(parseFile2(sample2)))
    print("part 2 input:")
    print(solve2(parseFile2(data2)))

