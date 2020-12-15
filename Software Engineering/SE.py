import math
from fractions import Fraction


def LOC():
    print("Lines Of Code\n\n"
          "Complexity:\n"
          "1. Low\n"
          "2. Average\n"
          "3. High")
    Complexity = int(input("Enter Complexity: "))
    if Complexity == 1:
        EI, EO, EQ, ILF, EIF = 3, 4, 3, 7, 5
    elif Complexity == 2:
        EI, EO, EQ, ILF, EIF = 4, 5, 4, 10, 7
    else:
        EI, EO, EQ, ILF, EIF = 6, 7, 6, 15, 10

    ui = int(input("User Input: "))
    uo = int(input("User Output: "))
    ue = int(input("User Enquiry: "))
    uf = int(input("User Files: "))
    ei = int(input("External Interfaces: "))
    fr = int(input("Factor Rate: "))
    ufp = (ui * EI) + (uo * EO) + (ue * EQ) + (uf * ILF) + (ei * EIF)

    sumF = 0
    for i in range(14):
        rate = fr
        sumF += rate

    CAF = 0.65 + (0.01 * sumF)
    FP = ufp * CAF
    print(f"Function Point Analysis:\n"
          f"\tUnadjusted Function Points (UFP): {uf}\n"
          f"\tComplexity Adjustment Factor (CAF): {CAF}\n"
          f"\tFunction Points (FP): {FP}")


def basic_cocomo():
    print("Constructive Cost Model")
    print("Mode:\n"
          "\t1. Organic\n"
          "\t2. Semi-detached\n"
          "\t3. Embedded")
    mode = input("Mode: ")
    if mode == '1':
        a, b, c, d = 2.4, 1.05, 2.5, 0.38
    elif mode == '2':
        a, b, c, d = 3.0, 1.12, 2.5, 0.35
    else:
        a, b, c, d = 3.6, 1.20, 2.5, 0.32
    KLOC = int(input("Enter KLOC = "))

    effort = a * (KLOC ** b)
    d_time = c * (effort ** d)
    ass = effort / d_time
    p = KLOC / effort

    print("Effort: ", effort, "Person-Month")
    print("Development Time: ", d_time, "Month")
    print("Average Staff Size: ", float(ass), "Persons")
    print("Productivity: ", p)


def epl():
    print("Estimated Programing Length")
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    ln_n1 = math.log(n1, 2)
    ln_n2 = math.log(n2, 2)

    N = (n1 * ln_n1) + (n2 * ln_n2)
    print("N cap: ", N)
    print("\n______________________________________________________________________\n")
    print("Estimated Programing Level")
    l_cap = 2 * n2 / (n1 * N)
    print(f"Estimated Programming Level is 1/{l_cap}")
    print(f"Estimated Programming Level is 1/{Fraction(l_cap).limit_denominator()}")
    print("\n______________________________________________________________________\n")


def inter_cocomo():
    print("Constructive Cost Model")
    print("Mode:\n"
          "\t1. Organic\n"
          "\t2. Semi-detached\n"
          "\t3. Embedded")
    mode = input("Mode: ")
    if mode == '1':
        a, b = 3.2, 1.05
    elif mode == '2':
        a, b = 3.0, 1.12
    else:
        a, b = 2.8, 1.20
    KLOC = int(input("Enter KLOC: "))
    EAF = int(input("EAF: "))
    E = a * (KLOC ** b) * EAF
    print("E: ", E)


def generalizeSoftwareMatrix():

    def TokenCount():
        print(f"Software Matrices\n"
              f"------------------\n"
              f"Token Count:\n\n"
              f"n = Vocabulary of a program\n"
              f"n1 = Number of a unique operators\n"
              f"n2 = Number of unique Operands\n")
        n1 = float(input("Enter n1: "))
        n2 = float(input("Enter n2: "))
        return n1 + n2

    def ProgramLength():
        print(f"Software Matrices\n"
              f"------------------\n"
              f"Program Length:\n\n"
              f"N = Program Length\n"
              f"N1 = Total Occurrences of Operators\n"
              f"N2 = Total Occurrences of Operands\n")
        N1 = float(input("Enter N1: "))
        N2 = float(input("Enter N2: "))
        return N1 + N2

    def Volume():
        givenVON = input("Enter 1 if value Of Programing length (N) is given else Press Enter: ")
        if givenVON == '1':
            N = float(input("Input Program Length (N): "))
        elif givenVON == '\n':
            N = ProgramLength()
        else:
            N = ProgramLength()
        print(f"Program Length (N) = {N}")
        givenVOn = input("Enter 1 if value Of Token Count (n) is given else Press Enter: ")
        if givenVOn == '1':
            n = float(input("Input Program Length (N): "))
        elif givenVOn == '\n':
            n = TokenCount()
        else:
            n = TokenCount()
        ln_n = math.log(n, 2)
        volume = N * ln_n
        return volume

    def ProgramLevel():
        givenVOV = input("Enter 1 if value Of Volume (V) is given else Press Enter: ")
        if givenVOV == '1':
            V = float(input("Input Volume (V): "))
        elif givenVOV == '\n':
            V = Volume()
        else:
            V = Volume()
        Vstar = float(input("V* = "))
        Plevel = Vstar / V
        return Plevel

    def ProgramDifficulty():
        givenVOL = input("Enter 1 if value Of Program Level (L) is given else Press Enter: ")
        if givenVOL == '1':
            L = float(input("Program Level (L): "))
        elif givenVOL == '\n':
            L = ProgramLevel()
        else:
            L = ProgramLevel()
        # D = "1/" + Fraction(L).limit_denominator()
        D = 1 / L
        return D

    def Effort():
        givenV = input(f"Please Enter the Values You Have Without Spaceing like: DV\n"
                       f"Where \nV = Volume\n"
                       f"L = Program Level\n"
                       f"D = Program Difficulty\n\n"
                       f"Values :")
        if givenV == 'VL':
            givenVOV = input("Enter 1 if value Of Volume (V) is given else Press Enter: ")
            if givenVOV == '1':
                V = float(input("Input Volume (V): "))
            elif givenVOV == '\n':
                V = Volume()
            else:
                V = Volume()
            givenVOL = input("Enter 1 if value Of Program Level (L) is given else Press Enter: ")
            if givenVOL == '1':
                L = float(input("Program Level (L): "))
            elif givenVOL == '\n':
                L = ProgramLevel()
            else:
                L = ProgramLevel()
            E = V / L
            return E
        elif givenV == "VD":
            givenVOV = input("Enter 1 if value Of Volume (V) is given else Press Enter: ")
            if givenVOV == '1':
                V = float(input("Input Volume (V): "))
            elif givenVOV == '\n':
                V = Volume()
            else:
                V = Volume()
            givenVOD = input("Enter 1 if value Of Program Difficulty (D) is given else Press Enter: ")
            if givenVOD == '1':
                D = float(input("Program Difficulty (D): "))
            elif givenVOD == '\n':
                D = ProgramDifficulty()
            else:
                D = ProgramDifficulty()
            E = V * D
            return E

    print(f"\n           Your Options What You Want\n ==============================================\n"
          f"1. Token Count (n)\n"
          f"2. Program Length (N)\n"
          f"3. Volume (V)\n"
          f"4. Program Level (L)\n"
          f"5. Program Difficulty\n"
          f"6. Effort\n")
    option = int(input("Enter Your Option: "))

    if option == 1:
        print(f"\nToken Count is {TokenCount()}")
    elif option == 2:
        print(f"\nProgram Length is {ProgramLength()}")
    elif option == 3:
        print(f"\nVolume is {Volume()}")
    elif option == 4:
        print(f"\nProgram Level is {ProgramLevel()}")
    elif option == 5:
        print(f"\nProgram Difficulty is {ProgramDifficulty()}")
    elif option == 6:
        print(f"\nEffort is {Effort()}")


option = int(input("1. Cocomo\n"
                   "2. InterCocomo\n"
                   "3. EPL\n"
                   "4. Line Of Code (LOC)\n"
                   "5. Software Matrix\n"
                   "\t\t5.1. Token Count (n)\n"
                   "\t\t5.2. Program Length (N)\n"
                   "\t\t5.3. Volume (V)\n"
                   "\t\t5.4. Program Level (L)\n"
                   "\t\t5.5. Program Difficulty\n"
                   "\t\t5.6. Effort\n\n"
                   "Note: for these 5.1 to 5.6 please First input 5 then you can go through its sub points\n\n"
                   "Enter Number of Question Type: "))
if option == 1:
    basic_cocomo()
elif option == 2:
    inter_cocomo()
elif option == 3:
    epl()
elif option == 4:
    LOC()
else:
    generalizeSoftwareMatrix()
