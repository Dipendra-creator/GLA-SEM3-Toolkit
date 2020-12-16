def classificationOfSecondOrderPDE():
    print(f"\nFormula ==>>  A (du^2/dx^2) + B (du^2/dx.dy) + C (du^2/dy^2)\n"
          f"So You Have To Provide Values of A,B and C respectively\n")
    A = int(input("Value of A: "))
    B = int(input("Value of B: "))
    C = int(input("Value of C: "))

    # conditions
    condition = (B ** 2) - (4 * A * C)

    if condition < 0:
        print(f"\nElliptic Because {condition} < 0")
    elif condition > 0:
        print(f"\nHyperbolic Because {condition} > 0")
    else:
        print(f"\nParabolic Because {condition} = 0")


classificationOfSecondOrderPDE()
