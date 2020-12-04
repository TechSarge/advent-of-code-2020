import re 


def passport(file):
    # file = open("sample", "r")

    file = file.read().split("\n\n")
    counter = 0
    for port in file:
        port = port.replace("\n", " ").replace("\r", " ") # remove new lines 
        port = port + " "
        print(port)

        birth = re.search("(byr:\d\d\d\d)", port) # get birth year
        # print(birth)
        if birth != None and 1920 <= int(birth.group()[4:]) <= 2002:
            None
            # print('birth correct')
        else:
            print("birth wrong ")
            continue

        issue = re.search("(iyr:\d\d\d\d)", port) # get issue year

        if issue != None and 2010 <= int(issue.group()[4:]) <= 2020:
            None
            # print('issue correct')
        else:
            print("issue date wrong")
            continue

        eyr = re.search("(eyr:\d\d\d\d)", port) # get experiation year
        if eyr != None and 2020 <= int(eyr.group()[4:]) <= 2030:
            None
            # print('expiration correct')
        else:
            print("experation date wrong")
            continue

        cm = re.search("(hgt:([0-9]+)cm)", port)

        inches = re.search("(hgt:([0-9]+)in)", port)

    
        if cm:
            # hight = re.search("(hgt:([0-9]+)cm)", port)
            hight = cm.group()[4:(len(cm.group()))-2]

        elif inches:
            # hight = re.search("(hgt:([0-9]+)in)", port)
            hight = inches.group()[4:(len(inches.group()))-2]
        else:
            continue

        if cm and 150 <= int(hight) <= 193:
            None
            # print("cm height matches")
        elif inches and 59 <= int(hight) <= 76:
            None
            # print("matches inches ")
        else:
            print("hieght wrong")
            continue


        hcl = re.search("(hcl:#(?:[0-9a-fA-F]{6}))", port)
        # print(hcl)
        if hcl != None:
            None
            # print("hair match")
        else:
            print("hair color wrong")
            continue

        
        ecl = re.search("(ecl:[a-z]{3})", port)
        # print(ecl)
        if ecl != None and (ecl.group()[4:] == "amb" or ecl.group()[4:] == "blu" or ecl.group()[4:] == "brn" or ecl.group()[4:] == "gry" or ecl.group()[4:] == "grn" or ecl.group()[4:] == "hzl" or ecl.group()[4:] == "oth"):
            None
            # print("eye color matches")
        else:
            print("eye color wrong")
            continue


        pid = re.search("(pid:[0-9]{9} )", port)

        if pid:
            None
        else:
            print("pid wrong\n")
            continue
        counter = counter + 1
        print(counter)

    print(counter)


if __name__ == "__main__":
    file = open("input", "r")
    passport(file)
