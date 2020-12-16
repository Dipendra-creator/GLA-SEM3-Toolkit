def pipeline():
    k = int(input('Input No. of Segments (K): '))
    n = int(input('Input No. of Instructions (N):'))
    T = int(input('Input the Execution Time (Type 1 to ignore): '))

    print(f"Non-Pipelined Execution Time: {n * k * T}")
    print(f"Pipelined Execution Time: {(k + n - 1) * T}")
    print(f"Speed-up: {(n * k) / (k + n - 1)}")


while True:
    pipeline()
