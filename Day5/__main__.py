import os

def findSeat(seat):
    '''
    find the seat the ticket is for
    '''
    row = range(127)
    column = range(7)
    for i in range(7):
        '''
        split the rows in half acording to first 7 chars
        if front it keeps the bottom half of numbers
        if back it keeps the top half of numbers
        '''
        if seat[i] == "F":
            row = row[:len(row)//2]
        else:
            row = row[len(row)//2 + 1:]
    for i in range(7, 10):
        '''
        determine column of the seat last 3 charictures
        if L it keeps the bottom half (low) of the integers
        if R it keeps the top half (high) of the integers
        '''
        if seat[i] == "L":
            column = column[:len(column)//2]
        else:
            column = column[len(column)//2 + 1:]
    '''return the seat id (row * 8) + column'''
    return (row.start * 8) + column.start

def findmyseat(seats):
    for i in range(len(seats) - 1):
        if seats[i] + 2 == seats[i + 1]:
            return seats[i] + 1

if __name__ == "__main__":
    data = open(os.path.dirname(__file__) + "\input", "r") # open files for the program to run
    sample = open(os.path.dirname(__file__) + "\sample", "r")
    # section 1 of part 1
    assert findSeat("FBFBBFFRLR") == 357
    assert findSeat("BFFFBBFRRR") == 567
    '''
    no sample for either parts completely because none was given and I did not generate sample data
    '''
    seats = []
    for line in data.read().splitlines():
        seats.append(findSeat(line))

    seats.sort()
    print("highest value: " + str(max(seats)))

    print("your seat: " + str(findmyseat(seats)))