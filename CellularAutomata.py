import numpy as np
import matplotlib.pyplot as plt


def switcher(lenghtOfBinaryNumber, binaryNumber): #Populating an array with the selected number in binary form
    table = np.zeros(8, dtype=int)
    if lenghtOfBinaryNumber == 1:
        table[-1] = binaryNumber
        return table
    elif lenghtOfBinaryNumber == 2:
        for i in range(1, 3):
            table[-i] = int(binaryNumber[-i])
        return table
    elif lenghtOfBinaryNumber == 3:
        for i in range(1, 4):
            table[-i] = int(binaryNumber[-i])
        return table
    elif lenghtOfBinaryNumber == 4:
        for i in range(1, 5):
            table[-i] = int(binaryNumber[-i])
        return table
    elif lenghtOfBinaryNumber == 5:
        for i in range(1, 6):
            table[-i] = int(binaryNumber[-i])
        return table
    elif lenghtOfBinaryNumber == 6:
        for i in range(1, 7):
            table[-i] = int(binaryNumber[-i])
        return table
    elif lenghtOfBinaryNumber == 7:
        for i in range(1, 8):
            table[-i] = int(binaryNumber[-i])
        return table
    elif lenghtOfBinaryNumber == 8:
        for i in range(1, 9):
            table[-i] = int(binaryNumber[-i])
        return table
    else:
        print("You entered to big number")
        exit()


def cellularAutomata(steps, steps2): #Calculation of CA performance
    area = np.zeros((steps, steps), dtype=int)
    area[0][steps2] = 1
    numberToCalculate = int(input("Enter the number for which we calculate (0-255). Number must be intiger:\n"))
    while numberToCalculate < 0:
        print("The number must be positive!")
        exit()
    numberInBinary = bin(numberToCalculate)[2:11]
    array = switcher(len(numberInBinary), numberInBinary)
    k = 1
    for j in range(steps):
        b = 1
        while b < (steps - 1):
            binary = str(area[j][b - 1]) + str(area[j][b]) + str(area[j][b + 1])
            binary = int(binary, 2)
            area[k][b] = array[binary]
            b = b + 1
        if k < (steps - 1):
            k = k + 1
    return area


def main(): #Displaying the result
    steps = int(input("How many steps do you want to do?\n"))
    steps2 = int(input("Where do you want to start? (0-number of steps)\n"))
    x = cellularAutomata(steps, steps2)
    fig = plt.figure(figsize=(100, 100))
    ax = plt.axes()
    ax.set_axis_off()
    ax.imshow(x, interpolation='none', cmap='RdPu')
    plt.show()


main()
